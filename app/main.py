from flask import Flask, request
from app.spacy_model import nlp_ner
import json
from app.date import get_date
from twilio.twiml.messaging_response import MessagingResponse
from app.myfitnesspal_db import get_info, initialize_db, get_NL_level

app = Flask(__name__)


@app.route("/bot", methods=["POST"])
def bot():

    initialize_db()

    #TODO: initiate conversation and ask for the user's name
    #TODO: ask for the user's name on MFP as well

    """ instantiate lists """
    reserved = ["DATE"]
    ner_input = []  # empty list
    
    """ get the response of the bot"""
    resp = MessagingResponse()
    msg = resp.message()
    responded = False # set the bot response to false

    """get the message of the user"""
    incoming_msg = request.values.get("Body", "").lower()  # inp
    spacy_res = nlp_ner(incoming_msg)  # process the input with spacy

    """extract entities from the spacy obj and append to empty list"""
    for ent in spacy_res.ents:
        ner_input.append(ent.label_)
    
    """if the list is not empty check which entity is missing and save it to a list"""
    nutrient = ""
    insight = "overview"
    if ner_input:
        missing = [i for i in reserved if i not in ner_input]
        if missing:
                msg.body("Can you specify for which day please?")
                #print("this is missing: {missing}")
                responded = True
        else:
            date_list = []
            for ent in spacy_res.ents:
                if ent.label_ == "DATE":            # take the user's input of date and convert it to a datetime obj.
                    date = get_date(ent.text)
                    date_list.append(date)          # add it to a list, if the user inputs multiple dates-> intends to compare
                if ent.label_ == "NUTRIENT":
                    nutrient = ent.text
                    #TODO: identify if it's any of the 5 nutrients
                if ent.label_ == "INSIGHT":
                    insight = ent.text
                    print(insight)
                    #TODO: identify if it's 'overview', 'comparison'
            
            msg.body("Let me check that for you...")

            user_name = "evaggiab"
            user_stats = get_info(user_name ,date_list ,nutrient ,insight)

            user_NL_level = get_NL_level(user_name)
        
            if (user_NL_level == 1):
                msg = resp.message()
                msg.body("You are doing great! 😁")

                msg = resp.message()
                msg.body("Protein: " + str(user_stats["protein"]) +"\n" + 
                "Carbs: " + str(user_stats["carbohydrates"]) + "\n" +
                "Fat: " + str(user_stats["fat"]) + "\n" +
                "Sugar: " + str(user_stats["sugar"]) + "\n" +
                "Sodium: " + str(user_stats["sodium"]) + "\n" +
                "Calories: " + str(user_stats["calories"]) + "\n")

                #msg.media("https://picsum.photos/200/300")

            elif (user_NL_level == 2):
                msg = resp.message()
                msg.body("medium level" + json.dumps(user_stats))
            else :
                msg = resp.message()
                msg.body("high level" + json.dumps(user_stats))
                msg.media("https://demo.twilio.com/owl.png")

            msg = resp.message()
            msg.body("Is everything clear to you?")
            responded = True
    if not responded:
        msg.body("I don't quite understand that. Can you repeat it please?")
    return str(resp)

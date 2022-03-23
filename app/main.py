from flask import Flask, request
from app.spacy_model import nlp_ner
import json
from app.date import get_date
from twilio.twiml.messaging_response import MessagingResponse
from app.myfitnesspal_db import get_date_stats, initialize_db, get_NL_level

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
            nutrient_list = []
            for ent in spacy_res.ents:
                if ent.label_ == "DATE":            # take the user's input of date and convert it to a datetime obj.
                    date = get_date(ent.text)
                    date_list.append(date)          # add it to a list, if the user inputs multiple dates-> intends to compare
                if ent.label_ == "NUTRIENT":
                    nutrient = ent.text
                    nutrient_list.append(nutrient)
                if ent.label_ == "INSIGHT":
                    insight = ent.text
                    print(insight)
                    #TODO: identify if it's 'overview', 'comparison'
            
            msg.body("Let me check that for you...")

            #user_name = "evaggiab"
            user_name = "evabot22"
            user_date_stats = get_date_stats(user_name ,date_list ,insight)
            #print(user_nutrient_stats)

            user_NL_level = get_NL_level(user_name)
        
            if (user_NL_level == 1):
                msg = resp.message()
                msg.body("You are doing great! 😁")

                msg = resp.message()
                text = "\n"
                print(nutrient_list)
                if (len(nutrient_list) > 0):
                    for i in range(len(nutrient_list)):
                        if (nutrient_list[i] == 'protein'):
                            text = text + "Protein: " + str(user_date_stats[nutrient_list[i]]) +"\n"
                        elif (nutrient_list[i] == 'carbohydrates'):
                            text = text + "Carbs: " + str(user_date_stats[nutrient_list[i]]) +"\n"
                        elif (nutrient_list[i] == 'fat'):
                            text = text + "Fat: " + str(user_date_stats[nutrient_list[i]]) +"\n"
                        elif (nutrient_list[i] == 'sugar'):
                            text = text + "Sugar: " + str(user_date_stats[nutrient_list[i]]) +"\n"
                        elif (nutrient_list[i] == 'sodium'):
                            text = text + "Sodium: " + str(user_date_stats[nutrient_list[i]]) +"\n"
                        elif (nutrient_list[i] == 'calories'):
                            text = text + "Calories: " + str(user_date_stats[nutrient_list[i]]) +"\n"
                else:
                    text = text + "Protein: " + str(user_date_stats["protein"]) + "\n" 
                    text = text + "Carbs: " + str(user_date_stats["carbohydrates"]) + "\n" 
                    text = text + "Fat: " + str(user_date_stats["fat"]) + "\n" 
                    text = text + "Sugar: " + str(user_date_stats["sugar"]) + "\n" 
                    text = text + "Sodium: " + str(user_date_stats["sodium"]) + "\n" 
                    text = text + "Calories: " + str(user_date_stats["calories"])


                msg.body(text)

                #msg.media("https://picsum.photos/200/300")

            elif (user_NL_level == 2):
                msg = resp.message()
                msg.body("medium level" + json.dumps(user_date_stats))
            else :
                msg = resp.message()
                msg.body("high level" + json.dumps(user_date_stats))
                msg.media("https://demo.twilio.com/owl.png")

            msg = resp.message()
            msg.body("Is everything clear to you?")
            responded = True
    if not responded:
        msg.body("I don't quite understand that. Can you repeat it please?")
    return str(resp)

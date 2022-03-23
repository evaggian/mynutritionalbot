from flask import Flask, request
from app.spacy_model import nlp_ner
import json
from app.date import get_date
from twilio.twiml.messaging_response import MessagingResponse
from app.myfitnesspal_db import get_date_stats, initialize_db, get_NL_level
from app.nutrientsInfo import get_more_info

app = Flask(__name__)


@app.route("/bot", methods=["POST"])
def bot():

    initialize_db()

    #TODO: initiate conversation and ask for the user's name
    #TODO: ask for the user's name on MFP as well

    """ instantiate lists """
    ner_input = []  # empty list
    
    """ get the response of the bot"""
    resp = MessagingResponse()
    responded = False # set the bot response to false

    """get the message of the user"""
    incoming_msg = request.values.get("Body", "").lower()  # inp
    spacy_res = nlp_ner(incoming_msg)  # process the input with spacy

    """extract entities from the spacy obj and append to empty list"""
    for ent in spacy_res.ents:
        ner_input.append(ent.label_)
        print(ent.text, ent.label_)

    """if the list is not empty check which entity is missing and save it to a list"""
    nutrient = ""
    insight = "overview"
    more_info_requested = False
    
    if ner_input:
        print(ner_input)
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
                
                overview_words = ["going","trend","intake","doing","update","check","go","tell","data"]
                compare_words = ["compare", "difference"]
                overview = [i for i in overview_words if i in insight]
                compare = [i for i in compare_words if i in insight]

                if overview:
                    insight = "overview"
                elif compare:
                    insight = "compare"

            if ent.label_ == "MORE_INFO":
                more_info_requested = True

        if (not date_list):                 #if the user didn't specify for which date, show him info for today
            date = get_date("today")
            date_list.append(date) 
        
        # quick fix in case the user types a synonym for carbs, change it in the nutrient_list to shoow the right nutrient
        carbs_synonyms = ["carbohydrates","carbs"]
        for j in range(len(nutrient_list)):
            carbs = [i for i in carbs_synonyms if i in nutrient_list]
            if (carbs):
                nutrient_list[j] = "carbohydrates"

        #user_name = "evaggiab"
        user_name = "evabot22"
        user_NL_level = get_NL_level(user_name)

        # if the user requested additional information
        #TODO: implement cases that the user asks for questions "Which food had the highest sugar today?"
        if (more_info_requested):
            more_info = get_more_info(nutrient_list)
            if (user_NL_level == 1):
                msg = resp.message()
                msg.body(more_info)
            elif (user_NL_level == 2):
                msg = resp.message()
                msg.body(more_info)
            else:
                msg = resp.message()
                msg.body(more_info)
        else:
            msg = resp.message()          
            msg.body("Let me check that for you...")
            user_date_stats = get_date_stats(user_name ,date_list ,insight)
            #print(user_nutrient_stats)
  
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

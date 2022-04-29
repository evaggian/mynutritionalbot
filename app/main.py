from flask import Flask, request
from app.spacy_model import nlp_ner
import time
from app.date import get_date
from twilio.twiml.messaging_response import MessagingResponse
from app.myfitnesspal_db import get_food_info
from app.nlp_nutrientsInfo import get_more_info
from app.user_info_db import *
from app.nlg import inform_overview

app = Flask(__name__)


@app.route("/bot", methods=["POST"])
def bot():

    """ instantiate lists """
    ner_input = []  # empty list
    
    """ get the response of the bot"""
    resp = MessagingResponse()
    responded = False # set the bot response to false

    initialize_db()

    # check if the user exists in the db based on the phone_number taken from Twilio
    user_name = user_exists(request.values.get('From')[-13:])
    #user_name = "evaggiab"         #enable this only for testing of NL_level 3

    if not user_name:
        msg = resp.message()
        msg.body("Sorry! You haven't signed up for this experiment.")
        responded = True
        return str(resp)

    first_time_user = first_time(user_name)
    user_first_name = get_user_first_name(user_name)

    # check if it is the first interaction of the user with the chatbot and give some self-description of the chatbot
    if first_time_user:
        msg = resp.message()
        msg.body("Hello " + user_first_name)
        time.sleep(5.0)

        msg = resp.message()
        msg.body("I am Avobot, your personal nutritionist")

        msg = resp.message()
        msg.body("I can help understand your nutrition stats from MyFitnessPal better and provide you with additional information.")

        msg = resp.message()
        msg.body("How can I help you today? ")

    # get the message of the user
    incoming_msg = request.values.get("Body", "").lower()  # inp
    spacy_res = nlp_ner(incoming_msg)  # process the input with spacy

    # extract entities from the spacy obj and append to empty list
    for ent in spacy_res.ents:
        ner_input.append(ent.label_)
        print(ent.text, ent.label_)

    # if the list is not empty check which entity is missing and save it to a list
    nutrient = ""
    insight = "overview"
    volume = "TOP"
    more_info_requested = False
    food_info_requested = False
    
    if ner_input:
        print(ner_input)
        date_list = []
        nutrient_list = []
        for ent in spacy_res.ents:
            if ent.label_ == "GREETING":      # if the user greets the chatbot and they have interacted before 
                msg = resp.message()
                msg.body("Hi " + user_first_name)

                msg = resp.message()
                msg.body("How can I help you today? ")

                responded = True
                return str(resp)
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

            if ent.label_ == "MORE_INFO":      # if the user asked for more information
                more_info_requested = True

            if ent.label_ == "FOOD":           # if the user asked for extra information about his food intake
                food_info_requested = True

            if ent.label_ == "VOLUME":         # and if the user specified if he wants to know about his top food or lowest food
                volume = ent.text

                volume_high_words = ["highest","top","high","maximum","max","most"]
                volume_low_words = ["lowest","small","smallest","minimum","min", "impacted","least"]
                volume_high = [i for i in volume_high_words if i in volume]
                volume_low = [i for i in volume_low_words if i in volume]

                if volume_high:
                    volume = "TOP"
                elif volume_low:
                    volume = "LOW"

        if (not date_list):                 #if the user didn't specify for which date, show him info for today
            date = get_date("today")
            date_list.append(date) 
        
        # fix in case the user types a synonym for some nutrient, change it in the nutrient_list to show the right nutrient
        carbs_synonyms = ["carbohydrates","carbs","carbo"]
        for j in range(len(nutrient_list)):
            carbs = [i for i in carbs_synonyms if i in nutrient_list]
            if (carbs):
                nutrient_list[j] = "carbohydrates"

        protein_synonyms = ["protein","proteins","amino acids","prot"]
        for j in range(len(nutrient_list)):
            protein = [i for i in protein_synonyms if i in nutrient_list]
            if (protein):
                nutrient_list[j] = "protein"

        fat_synonyms = ["fat","fats","fatty acids","trans"]
        for j in range(len(nutrient_list)):
            fat = [i for i in fat_synonyms if i in nutrient_list]
            if (fat):
                nutrient_list[j] = "fat"

        sodium_synonyms = ["sodium","salt"]
        for j in range(len(nutrient_list)):
            sodium = [i for i in sodium_synonyms if i in nutrient_list]
            if (sodium):
                nutrient_list[j] = "sodium"

        user_NL_level = get_NL_level(user_name)

        if (more_info_requested):                               # if the user requested additional information
            text = get_more_info(nutrient_list, user_NL_level)
            print(text)

            msg = resp.message()
            msg.body(text)
        elif (food_info_requested):                            # if the user requested which food was high in protein for a particular day
            food_info = get_food_info(user_name, date_list, nutrient_list, volume)
            if (food_info == None):
                msg = resp.message()
                msg.body("There are no entries for the specified date. Try a different date")
            else:
                if (user_NL_level == 1):
                    msg = resp.message()
                    msg.body(food_info)
                elif (user_NL_level == 2):
                    msg = resp.message()
                    msg.body(food_info)
                else:
                    msg = resp.message()
                    msg.body(food_info)
        else:
            msg = resp.message()          
            msg.body("Let me check that for you...")
            
            text = inform_overview(nutrient_list, date_list ,insight, user_NL_level, user_name, user_first_name)
            print(text)
  
            msg = resp.message()
            msg.body(text)

        responded = True
    if not responded:
        msg.body("I don't quite understand that. Can you repeat it please?")
    return str(resp)

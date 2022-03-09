from flask import Flask, request
from app.spacy_model import nlp_ner
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/bot", methods=["POST"])
def bot():
    reserved = ["DATE", "NUTRIENT"]
    ner_input = []  # empty list
    incoming_msg = request.values.get("Body", "").lower()  # inp
    spacy_res = nlp_ner(incoming_msg)  # process the input with spacy
    for ent in spacy_res.ents:
        ner_input.append(ent.label_)
    if ner_input:
        missing = [i for i in reserved if i not in ner_input]
    if missing:
        # TODO: present the missing entities in a string format
        msg.body(f"this is missing: {missing}")
    else:
        # for each enetity that we have taken from the user input
        for ent in spacy_res.ents:
            if ent.label_ == "DATE":
                date = ent.text
            if ent.label_ == "NUTRIENT":
                nutrient = ent.text
        msg.body(date, nutrient)

    resp = MessagingResponse()
    msg = resp.message()
    print(incoming_msg)
    responded = False
    if "quote" in incoming_msg:
        # return a quote
        r = requests.get("https://api.quotable.io/random")
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = "I could not retrieve a quote at this time, sorry."
        msg.body(quote)
        responded = True
    if "buongiorno" in incoming_msg:
        msg.body("buongiorno twat!")
        # return a cat pic
        msg.media("https://cataas.com/cat")
        responded = True
    if not responded:
        msg.body("I only know about famous quotes and cats, sorry!")
    return str(resp)

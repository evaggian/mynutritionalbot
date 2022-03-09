from flask import Flask, request
from app.spacy_model import nlp_ner
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/bot", methods=["POST"])
def bot():
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    reserved = ["DATE", "NUTRIENT"]
    ner_input = []  # empty list

    incoming_msg = request.values.get("Body", "").lower()  # inp
    spacy_res = nlp_ner(incoming_msg)  # process the input with spacy

    for ent in spacy_res.ents:
        ner_input.append(ent.label_)
    if ner_input:
        missing = [i for i in reserved if i not in ner_input]
        try:
            if missing:
                # TODO: present the missing entities in a string format
                msg.body(f"this is missing: {missing}")
        except:
            pass
    else:
        # for each enetity that we have taken from the user input
        for ent in spacy_res.ents:
            if ent.label_ == "DATE":
                date = ent.text
            if ent.label_ == "NUTRIENT":
                nutrient = ent.text
        msg.body(date, nutrient)
    responded = True
    if not responded:
        msg.body("I only know about famous quotes and cats, sorry!")
    return str(resp)

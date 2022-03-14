"""Train SPACY NER"""
import spacy
import json
from tqdm import tqdm
from spacy.tokens import DocBin
import subprocess


def train_model():
    nlp = spacy.blank("en")  # load a new spacy model
    db = DocBin()
    f = open("app/training/annotations.json")
    TRAIN_DATA = json.load(f)


    for text, annot in tqdm(TRAIN_DATA["annotations"]):
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is None:
                print("Skipping entity")
            else:
                ents.append(span)
        doc.ents = ents
        db.add(doc)

    db.to_disk("app/model/training_data.spacy")  # save the docbin object


def train_with_shell():
    subprocess.run(
        [
            "python",
            "-m",
            "spacy",
            "init",
            "config",
            "config.cfg",
            "--lang",
            "en",
            "--pipeline",
            "ner",
            "--optimize",
            "efficiency",
        ],
        shell=True,
    )
    # python -m spacy train config.cfg --output ./ --paths.train ./training_data.spacy --paths.dev ./training_data.spacy
    subprocess.run(
        [
            "python",
            "-m",
            "spacy",
            "train",
            "config.cfg",
            "--output",
            "./",
            "--paths.train",
            "app/model/training_data.spacy",
            "--paths.dev",
            "app/model/training_data.spacy",
        ],
        shell=True,
    )

nlp_ner = spacy.load("model-best")

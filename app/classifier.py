import spacy

from app.database import Article, Session

nlp = spacy.load("en_core_web_sm")

CATEGORIES = {
    "Terrorism / protest / political unrest / riot": [
        "terror",
        "protest",
        "riot",
        "unrest",
    ],
    "Positive/Uplifting": ["happy", "joy", "success", "uplifting"],
    "Natural Disasters": ["earthquake", "flood", "storm", "disaster"],
}


def classify_article(article):
    doc = nlp(article["content"])
    for category, keywords in CATEGORIES.items():
        if any(keyword in doc.text for keyword in keywords):
            return category
    return "Others"

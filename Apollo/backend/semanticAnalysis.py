# Emotions: 'Joy', 'Sadness', 'Anger', 'Love', 'Fear', 'Surprise'

from transformers import pipeline

emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

def analyze_sentiment(text):
    result = emotion_classifier(text)
    return result
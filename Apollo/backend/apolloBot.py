from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai
from semanticAnalysis import analyze_sentiment
import os


# Load environment variables
load_dotenv()

# Configure the Google Generative AI
genai.configure(api_key="AIzaSyBSkWzHrCEM7g0GJU09ZwY4SnHlqI3h3XQ")
model = genai.GenerativeModel("gemini-pro")

app = Flask(__name__)
CORS(app)

@app.route('/gemini', methods=['POST'])
def gemini():
    data = request.get_json()
    message = data.get('message', '')
    chat_history = data.get('history', [])

    try:
        # Generate poem response
        response = model.start_chat(history=chat_history).send_message(f"write a poem on {message}")
        poem = ''.join([chunk.text for chunk in response])

        # Sentiment analysis
        sentiment_result = analyze_sentiment(poem)

        # Send back the poem
        return jsonify({
            "poem": poem,
            "sentiment": sentiment_result
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=8000)

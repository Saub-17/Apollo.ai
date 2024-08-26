from dotenv import load_dotenv
from semanticAnalysis import analyze_sentiment

load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    poem_prompt = f"Please write a poem on the following topic: {question}"
    response = chat.send_message(poem_prompt, stream=True)
    return response

st.set_page_config(page_title="Apollo.ai")
st.header("Generate poetry through the blessings of the great Greek God of poetry, drama, and art!")

input = st.text_input("Input: ", key="input")
submit = st.button("Describe the topic from which you would like to generate a poem!")

if submit and input:
    response = get_gemini_response(input)
    st.subheader("The response is")

    
    poem_placeholder = st.empty()
    poem_text = ""  

    for chunk in response:
        poem_text += chunk.text  
        poem_placeholder.write(poem_text) 
    
    sentiment_result = analyze_sentiment(poem_text)

    st.subheader("Sentiment Analysis")
    for sentiment in sentiment_result:
        st.write(f"Emotion: {sentiment['label']}, Score: {sentiment['score']:.2f} / 1.00")
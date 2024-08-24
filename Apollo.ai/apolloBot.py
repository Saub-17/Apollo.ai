from dotenv import load_dotenv
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

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input: ", key="input")
submit = st.button("Describe the topic from which you would like to generate a poem!")

if submit and input:
    response = get_gemini_response(input)
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
st.subheader("The chat history is: ")

for role, text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")
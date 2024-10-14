import streamlit as st
from utils import clear_data, send_cancel_buttons
from dotenv import dotenv_values
import google.generativeai as genai

for key, default in [('text', ''), ('file', None), ('disable', False), ('audio', None)]:
    if key not in st.session_state:
        st.session_state[key] = default

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

st.session_state['text'] = st.text_area(label='Prompt', value=st.session_state['text'])
st.session_state['audio'] = st.experimental_audio_input("Record a voice message", on_change=None)

google_api_key = dotenv_values()['gemini_api_key']
genai.configure(api_key=google_api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

if st.session_state['audio']:
    st.audio(st.session_state['audio'])

if st.session_state['audio'] and st.session_state['text']:
    send, clear = send_cancel_buttons(clear_data)
    myfile = genai.upload_file(st.session_state['audio'], mime_type="audio/mp3")
    if send:
        result = model.generate_content([myfile, "\n\n", st.session_state['text']])
        st.write(result.text)
    if clear:
        st.rerun()
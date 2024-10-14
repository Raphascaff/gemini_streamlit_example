import streamlit as st

def clear_data():
    st.session_state['text'] = ''
    st.session_state['file'] = None
    st.session_state['disable'] = False
    st.session_state['audio'] = None

def send_cancel_buttons(on_cancel_callback):
    collumn1, collumn2 = st.columns([2, 36])
    with collumn1:
        enviar = st.button("Send", type="primary", disabled=st.session_state['disable'])
    
    with collumn2:
        clear = st.button("clear", type="secondary", on_click=on_cancel_callback)
    return enviar, clear
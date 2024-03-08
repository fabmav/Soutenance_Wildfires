import streamlit as st

st.set_page_config(page_title="Conclusion & perspectives", page_icon="Fire_logo.png",layout="wide",)

with open('Texte/conclusion.md', 'r',encoding='UTF-8') as f:
    conclusion = f.read()

st.write(conclusion)
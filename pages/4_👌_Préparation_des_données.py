
import streamlit as st

st.set_page_config(page_title="Présentation du jeu de données", page_icon="Fire_logo.png")

pages=["Nettoyage et sélection","Web Scrapping"]

page = st.sidebar.radio("Cliquez sur la partie à afficher", pages)


if page == pages[0] :
    st.write("## Nettoyage et sélection")
    st.write('###Titre')
    st.write('blablabla')
    st.divider()
if page == pages[1] :
    st.write("## Webscraping")
    st.write('###Titre')
    st.write('blablabla')
    st.divider()

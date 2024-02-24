import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

import gdown

# Replace 'FILE_ID' with the actual ID of your Google Drive file
file_id = '1m73Ot3M2O2YPPH1urzuTejOaOEQuDi2P'

# Google Drive API endpoint to download the file
url = f'https://drive.google.com/uc?id={file_id}'



file = gdown.download(url,output="wildfire_base_clean.zip")

# Convert the downloaded file bytes to a BytesIO object
# file_in_memory = BytesIO(file_bytes)

df=pd.read_csv(file,compression='zip')
st.set_page_config(page_title="Data Visualisation", page_icon="Fire_logo.png",)


pages=["Data Viz' générale","Data Viz' régionale","Data Viz' temporelle"]

page = st.sidebar.radio("Cliquez sur la partie à afficher", pages)


if page == pages[0] :
    tab1, tab2, tab3 = st.tabs(["Taille des feux","Dichotomie des feux", "Focus sur les Mégafeux"])
    with tab1:
        st.header("Focus sur la variable Taille des feux")
        st.dataframe(df.taille_feu.describe())
   

if page == pages[1] :
    st.write("## Préparation des données : complétude des données")
    st.write('###Titre')
    st.write('blablabla')
    st.divider()








        
    with tab2:
        col1, col2, col3 = st.columns([1,3,1])
        col1.write("")
        col2.write("## La dichotomie des feux")
        col3.write("")
        st.write("Nous pouvons observer dans le jeu de données, 2 « tendances », illustrées par une série de 2 graphiques sur la même variable")
        col1, col2 = st.columns(2)
        col1.write("Les feux nombreux, de petite taille,  de cause humaine")
        col2.write("Les feux plus rares, de taille importante, de cause naturelle")
        st.divider()
        st.image("Variable_Cause.png",width=1100)
        st.divider()
        st.image("Variable_Classe.png",width=1100)
        st.divider()
        st.image("Variable_mois.png", width=1100)
        st.divider()
        st.image("Variable_année.png", width=1100)
        st.divider()
        st.image("Variable_region.png", width=1100)
        st.divider()
        st.image("Variable_vegetation.png", width=1100)

    with tab3:
        st.header("Focus sur les mégafeux")

if page == pages[1] :
    st.write("## Régionale")
    st.write('###Titre')
    st.write('blablabla')
    st.divider()

if page == pages[2] :
    st.write("## Temporelle")
    st.write('###Titre')
    st.write('blablabla')
    st.divider()


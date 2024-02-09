import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
url="https://drive.google.com/uc?export=download&id=10R41W-YfpWcFoc-D-PvKWmtGuayjWxZB"
df=pd.read_csv(url)
st.title("Analyse des feux de forêts aux USA")
st.sidebar.title("Feux de forêts aux USA")
st.sidebar.header("Déroulé du projet")
pages=["Présentation du jeu de données", "Préparation des données", "Data Visualisation", "Modélisation"]
page=st.sidebar.radio("Allez vers", pages)
if page == pages[0] :
    st.write("## Présentation du jeu de données : première exploration")
    st.divider()
    st.write("https://www.fs.usda.gov/rds/archive/catalog/RDS-2013-0009.6")
    st.divider()
    st.image("SweetCrk-Milepost2Fire-Marcus-Kauffman.jpg")
    st.dataframe(df.loc[:, ["taille_feu"]].describe())
if page == pages[1] :
    st.write("## Préparation des données : complétude des données")
st.sidebar.header("L'équipe")

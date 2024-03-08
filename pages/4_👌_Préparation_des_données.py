
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# les fichiers dont on a besoin pour l'appli
with open('Pickle/head.pkl', 'rb') as f:
    df_head = pickle.load(f)
with open('Pickle/data_na.pkl', 'rb') as f:
    data_na = pickle.load(f)

with open('Texte/dataset_presentation.md', 'r',encoding='UTF-8') as f:
    pres = f.read().split('---')

df_data = pd.read_csv('Texte/_variable_descriptions.csv')

with open('Texte/dataset_cleaning.md', 'r',encoding='UTF-8') as f:
    preprocessing = f.read().split('---')

with open('code_example/code_comte.txt', 'r',encoding='UTF-8') as f:
    code_comte = f.read()

with open('code_example/code_meteo.txt', 'r',encoding='UTF-8') as f:
    code_meteo = f.read()

with open('code_example/code_meteo part2.txt', 'r',encoding='UTF-8') as f:
    code_meteo_pt2 = f.read()

with open('code_example/code_vegetation.txt', 'r',encoding='UTF-8') as f:
    code_vegetation= f.read()

with open('code_example/code_vegetation part2.txt', 'r',encoding='UTF-8') as f:
    code_vegetation_pt2= f.read()
    
st.set_page_config(page_title="Présentation du jeu de données", page_icon="Fire_logo.png", layout="wide",)

with st.expander("voir le dataset finalisé") :
    st.write(df_head)
st.divider()

st.markdown(pres[0])
with st.expander("voir les champs du dataset d'origine") :
    st.write(df_data)

st.markdown(pres[1])
with st.expander("voir Nan du dataset d'origine") :
    st.write(data_na)
st.divider()
st.markdown(preprocessing[0])
st.markdown(preprocessing[1])
st.markdown(preprocessing[2])
st.markdown(preprocessing[3])
st.markdown(preprocessing[4])

st.divider()
st.markdown(preprocessing[5])
st.markdown(preprocessing[6])
st.markdown(preprocessing[7])
with st.expander("voir le code") :
    st.code(code_comte,language='python')
    st.divider()
st.markdown(preprocessing[8])
with st.expander("voir le code") : 
        st.code(code_meteo,language='python')
        st.code(code_meteo_pt2,language='python')
st.divider()
st.markdown(preprocessing[9])
with st.expander("voir le code") :
    st.code(code_vegetation,language='python')
    st.code(code_vegetation_pt2,language='python')
st.divider()


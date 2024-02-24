
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# les fichiers dont on a besoin pour l'appli
with open('head.pkl', 'rb') as f:
    df_head = pickle.load(f)

with open('Texte/dataset_description.md', 'r',encoding='UTF-8') as f:
    desc = f.read()

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
  
st.set_page_config(page_title="Présentation du jeu de données", page_icon="Fire_logo.png",)
st.write("## Compréhension du jeu de données : première exploration")
st.divider()
st.image("https://www.fs.usda.gov/sites/default/files/users/user3824/Photos/CWDG/SweetCrk-Milepost2Fire-Marcus-Kauffman.jpg")
    
display = st.radio('Que souhaitez-vous montrer ?', ('Head', 'Plot'))
if display == 'Head' :
  st.write(df_head)
elif display == 'Plot' : 
        st.image('plot.png')

st.markdown(desc)
st.write("https://www.fs.usda.gov/rds/archive/catalog/RDS-2013-0009.6")
st.divider()





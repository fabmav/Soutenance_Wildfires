import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import gdown

with open("stat_méga.pkl", "rb") as fichier_pickle:
    description_feux = pickle.load(fichier_pickle)
    description_Mégafeux = pickle.load(fichier_pickle)
    description_Hors_Méga = pickle.load(fichier_pickle)
    Surf_Total = pickle.load(fichier_pickle)
    Surf_méga= pickle.load(fichier_pickle)
    Part_méga_NB = pickle.load(fichier_pickle)
    Part_méga_surf= pickle.load(fichier_pickle)

with open("Texte/Dispersions.md", "r", encoding="utf-8") as fichier_markdown:
    Com_Dispersions = fichier_markdown.read()

st.set_page_config(page_title="Data Visualisation", page_icon="Fire_logo.png",)
pages=["Data Viz' générale","Data Viz' régionale","Data Viz' temporelle"]

page = st.sidebar.radio("Cliquez sur la partie à afficher", pages)

if page == pages[0]:
    tab1, tab2, tab3 = st.tabs(["Taille des feux","Dichotomie des feux", "Focus sur les Mégafeux"])

    with tab1:
        
        # Centrer le titre
        st.markdown("<h2 style='text-align: center;background: linear-gradient(to right, orange, red); -webkit-background-clip: text; color: transparent;'>Dispersion statistique comparative des feux selon leur taille (Mégafeux est >= 10 000 Ha)</h2>", unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns([2,6,2,2])
        col1.markdown("<h4 style='text-align: center;'>Ensemble des feux</h4>", unsafe_allow_html=True)
        col2.markdown("<h4 style='text-align: center; background: linear-gradient(to right, navy, orange, red); -webkit-background-clip: text; color: transparent;'>Principales observations</h4>", unsafe_allow_html=True)
        col3.markdown("<h4 style='text-align: center;'>Hors Mégafeux</h4>", unsafe_allow_html=True)
        col4.markdown("<h4 style='text-align: center;'>Mégafeux</h4>", unsafe_allow_html=True)
        col1, col2, col3,col4 = st.columns([2,6,2,2])
        col1.table(description_feux)
        col2.markdown(Com_Dispersions, unsafe_allow_html=True)
        col3.table(description_Hors_Méga)
        col4.table(description_Mégafeux)
        col1, col2, col3 = st.columns([2,8,2])
        col1.write("")
        col2.image("Graphes/Boxplot_Taille.png", width=1000)
        col3.write("")
        


    with tab2:
        st.markdown("<h2 style='text-align: center; background: linear-gradient(to right, orange, red); -webkit-background-clip: text; color: transparent;'>La dichotomie des feux</h2>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center;'>Les observations précédentes nous ont conduit à faire une analyse des variables en fonction du nombre de feux et de la surface brûlée</h4>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        st.divider()
        col1.markdown("<h3 style='text-align: center; background: linear-gradient(to right, orange, red); -webkit-background-clip: text; color: transparent;'>Les feux nombreux, de petite taille,  de cause humaine</h3>", unsafe_allow_html=True)
        col2.markdown("<h3 style='text-align: center; background: linear-gradient(to right, orange, red); -webkit-background-clip: text; color: transparent;'>Les feux plus rares, de taille importante, de cause naturelle</h3>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1,4,1])
        col1.write("")
        col2.image("Graphes/Variable_Classe.png",width=1200)
        col3.write("")
        st.divider()
        col1, col2, col3 = st.columns([1,4,1])
        col1.write("")
        col2.image("Graphes/Variable_Cause.png",width=1200)
        col3.write("")
        st.divider()
        col1, col2, col3 = st.columns([1,4,1])
        col1.write("")
        col2.image("Graphes/Variable_mois.png",width=1200)
        col3.write("")
        st.divider()
        col1, col2, col3 = st.columns([1,4,1])
        col1.write("")
        col2.image("Graphes/Variable_region.png",width=1200)
        col3.write("")
        st.divider()
        col1, col2, col3 = st.columns([1,4,1])
        col1.write("")
        col2.image("Graphes/Variable_vegetation.png",width=1200)
     




    with tab3:
        st.header("Focus sur les mégafeux")

if page == pages[1] :

    st.write("###Relation entre nombre de feux et données géographiques")
    st.write("##Les régions Southeast et Southwest représentent le plus grand nombres de feux entre 1992 et 2020.") 
    st.divider()
    st.image("Nombre_de_Feux_par_Régions.gif")
    st.divider()
    st.write('Cette carte affiche les mégafeux principalement situés à l’ouest du continent. ils sont liés a des cause Naturelles')
    st.divider()
    st.image("Carto_Megafeux.png")
    st.divider()
    st.write("#Relation entre température, précipitation et taille des feux")
    st.divider()
    st.image("TempMoy_classG_feu.png")
    st.write("Elles sont significatives entre 2005 et 2015 mais c’est surtout dans la région de SouthEast ou la température a un impact sur le nombre des Mégafeux.")
    st.image("Evol_tempMoyenn_sur_Megafeu_southeast.png")
    st.divider()
    st.write("#Relation entre végétation et taille des feux")
    st.write("Les végétations Boreal Evergreen (feuillage persistant de la forêt boréale) et shrubland (arbustes) sont les végétations du continent les plus touchées.")
    st.image("Moy_Taille_Feu_par_Veget.png")
    st.divider()
    st.write("#Relation entre cause et taille des feux")
    st.write("La taille des feux augmente significativement jusqu’en 2006 et reste stable jusqu’en 2020. La cause Natural est la plus importante depuis 2006.")
    st.divider()
    st.image("Relation_cause_taille_feux_par_année.png")
    st.divider()

if page == pages[2] :
    st.write("## Temporelle")
    st.write('###Titre')
    st.write('blablabla')
        st.image("Graphes/Variable_année.png", width=1100)
    st.divider()


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
pages=["Data Viz' générale","Data Viz' régionale","Data Viz' temporelle", "Focus sur les Mégafeux"]

page = st.sidebar.radio("Cliquez sur la partie à afficher", pages)

if page == pages[0]:
    tab1, tab2 = st.tabs(["Taille des feux","Dichotomie des feux"])

    with tab1:
        
        # Centrer le titre
        st.markdown("<h2 style='text-align: center;background: linear-gradient(to right, orange, red); -webkit-background-clip: text; color: transparent;'>Dispersion statistique des feux selon leur taille (Mégafeux est >= 10 000 Ha)</h2>", unsafe_allow_html=True)
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
        col1, col2, col3 = st.columns([1,2,1])
        col1.markdown("   ")
        col1.markdown("   ")
        col1.markdown("   ")
        col1.markdown("   ")
        col1.markdown("   ")
        col1.markdown("   ")
        col1.markdown("   ")
        col1.markdown("97% des feux appartiennent aux classes de taille A-C (soit moins de 40.5 Ha) mais représentent moins de 7% de la surface brûlée")
        col2.image("Graphes/Variable_Classe.png",width=700)
        col3.markdown("   ")
        col3.markdown("   ")
        col3.markdown("   ")
        col3.markdown("   ")
        col3.markdown("   ")
        col3.markdown("   ")
        col3.markdown("   ")
        col3.markdown("Inversement les feux de taille G (plus de 2020 Ha) représentent 0.18% du nombre de feux pour 70% de la surface brûlée!")
        st.divider()
        col1, col2, col3 = st.columns([1,2,1])
        col1.markdown("   ")
        col1.markdown("   ")
        col1.markdown("   ")
        col1.markdown("   ")
        col1.markdown("   ")
        col1.markdown("   ")
        col1.markdown("   ")
        col1.markdown("   ")
        col1.markdown("   ")
        col1.markdown("   ")
        col1.write("Les causes naturelles provoquent 14% des feux mais représentent 50% de la surface brûlé")
        col2.image("Graphes/Variable_Cause.png",width=700)
        col3.markdown("    ")
        st.divider()
        col1, col2, col3 = st.columns([1,2,1])
        col1.write("")
        col2.image("Graphes/Variable_region.png",width=700)
        col3.write("")
        st.divider()
        col1, col2, col3 = st.columns([1,2,1])
        col1.write("")
        col2.image("Graphes/Variable_vegetation.png",width=700)

if page == pages[1] :

    st.write("### Relation entre nombre de feux et données géographiques")
    st.write("## Les régions Southeast et Southwest représentent le plus grand nombres de feux entre 1992 et 2020.") 
    st.divider()
    st.image("Nombre_de_Feux_par_Régions.gif")
    st.divider()
    st.write('Cette carte affiche les mégafeux principalement situés à l’ouest du continent. ils sont liés a des cause Naturelles')
    st.divider()
    st.image("Carto_Megafeux.png")
    st.divider()
    st.write("# Relation entre température, précipitation et taille des feux")
    st.divider()
    st.image("TempMoy_classG_feu.png")
    st.write("Elles sont significatives entre 2005 et 2015 mais c’est surtout dans la région de SouthEast ou la température a un impact sur le nombre des Mégafeux.")
    st.image("Evol_tempMoyenn_sur_Megafeu_southeast.png")
    st.divider()
    st.write("# Relation entre végétation et taille des feux")
    st.write("Les végétations Boreal Evergreen (feuillage persistant de la forêt boréale) et shrubland (arbustes) sont les végétations du continent les plus touchées.")
    st.image("Moy_Taille_Feu_par_Veget.png")
    st.divider()
    st.write("# Relation entre cause et taille des feux")
    st.write("La taille des feux augmente significativement jusqu’en 2006 et reste stable jusqu’en 2020. La cause Natural est la plus importante depuis 2006.")
    st.divider()
    st.image("Relation_cause_taille_feux_par_année.png")
    
    
    
if page == pages[2] : 

    st.markdown("<h2 style='text-align: center; background: linear-gradient(to right, orange, red); -webkit-background-clip: text; color: transparent;'>Notre dataset représente 29 ans de collecte de données</h2>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["Mois","Trimestre", "Année", "Décennie"])
    
    with tab1:
        st.markdown("<h3 style='text-align: center; background: linear-gradient(to right, orange, red); -webkit-background-clip: text; color: transparent;'>Observations mensuelles</h3>", unsafe_allow_html=True)
        st.divider()
        col1, col2 = st.columns([1,2])
        col1.markdown("   ")
        col1.markdown("   ")
        col1.markdown("   ")
        col1.markdown("   ")
        col1.markdown("   ")
        col1.markdown("   ")
        col1.markdown("   ")
        col1.markdown("   ")
        col1.markdown("   ")
        col1.markdown("   ")
        col1.write("Proportionnellement plus fréquents en juillet (12.9%), en avril (12.5%), en mars (12.3%) et en août (11%) ; les 2 mois d'été représentent près de 50% de la surface brûlée")
        col2.image("Graphes/Mois_Nb_Surf.png", width=900)
        st.divider()


    with tab2:
        st.markdown("<h3 style='text-align: center; background: linear-gradient(to right, orange, red); -webkit-background-clip: text; color: transparent;'>Observations trimestrielles</h3>", unsafe_allow_html=True)
        st.write("Près des 2/3  des feux ont lieu au 2ième et 3ième trimestre et représentent 82% de la surface brûlée. Un point étonnant 25% des feux ont lieu au 1er trimestre")
        st.image("Graphes/Trimestre_Nb_Surf.png", width=1200)


    with tab3:
        st.markdown("<h3 style='text-align: center; background: linear-gradient(to right, orange, red); -webkit-background-clip: text; color: transparent;'>Observations annuelles</h3>", unsafe_allow_html=True)
        st.write("Le nombre de feux semble agir par 'pics' avec dans les années 90, deux pics en 1994 et en 1996, dans les années 00, deux pics en 2000 et en 2006, la décennie 2010 se caractérise par un pic en 2011, puis un pic de 3 ans de 2016 à 2018. Le nombre et la taille des feux semblent décorrélés. L'évolution de la taille moyenne des feux ne suit pas toujours la même tendance, notamment lorsque le nombre de feu décroit fortement, la taille moyenne ne décroit pas de la même façon et inversement")
        st.image("Graphes/Nbre_surf_paran.png", width=1100)
        st.image("Graphes/Nbre_taille_par an.png", width=1100)
        st.image("Graphes/Année_Nb_Surf.png", width=1100)

    with tab4:
        st.markdown("<h3 style='text-align: center; background: linear-gradient(to right, orange, red); -webkit-background-clip: text; color: transparent;'>Observations décennales</h3>", unsafe_allow_html=True)
        st.write("La décennie (2001-2010) est légèrement plus importante en % du nombre de feux et reflète le profil général de notre dataset. Bien qu'un peu moins importante en % du nombre de feux, la dernière décennie (2011-2020) pèse 45% dans la surface brûlée des 29 années observées. Les décades 90's et 10's tendent à s’opposer en terme de caractéristiques")
        st.image("Graphes/Décennie_Nb_Surf.png", width=600)
        st.write("Les feux de classe G sont presque deux fois moins présents dans les années 90 que durant la dernière décade avec respectivement 24 et 43% ")
        st.image("Graphes/Tri_Classe_Décennie.png")
        st.write("Les mégafeux sont relativement moins importants dans les années 1992 et 2000 et beaucoup plus au cours de la dernière décennie")
        st.image("Graphes/Tri_Méga_Décennie.png")
        st.write("Régionnalement le 'Southeast est plus représenté dans les années 90's et moins lors de la dernière décennie. Nous constatons exactement l'inverse dans le Norh Central qui est plus présent dans les années 2011-2020 ")
        st.image("Graphes/Tri_Région_Décennie.png")




if page == pages[3] :
    st.markdown("<h2 style='text-align: center; background: linear-gradient(to right, orange, red); -webkit-background-clip: text; color: transparent;'>Focus sur les mégafeux</h2>", unsafe_allow_html=True)
    st.divider()

    col1, col2 = st.columns(2)
    col1.markdown("   ")
    col1.markdown("   ")
    col1.markdown("   ")
    col1.markdown("   ")
    col1.markdown("   ")
    col1.markdown("   ")
    col1.markdown("<h4 style='text-align: justify;background: linear-gradient(to right, orange, red); -webkit-background-clip: text; color: transparent;'>Comme vu précédemment les feux à 10 00 ha et plus sont très peu nombreux sur le jeu de données, 952 soit 0.04% du dataset et pourtant ils représentent 48% de la surface brûlée, raison pour laquelle ils mériteraient une attention particulière</h4>", unsafe_allow_html=True)
    col2.image("Graphes/Mégafeux_Nb_Surf.png",width=700)
    st.divider()

    col1, col2, col3 = st.columns([1,2,1])
    col1.write("blabla")
    col2.image("Graphes/Cause_mégafeux_NB.png",width=500)
    col3.write("")
    st.divider()

    col1, col2, col3 = st.columns([1,2,1])
    col1.write("blabla")
    col2.image("Graphes/Mois_mégafeux.png",width=500)
    col3.write("")
    st.divider()

    col1, col2, col3 = st.columns([1,2,1])    
    col1.write("blabla")
    col2.image("Graphes/Trimestre_mégafeu_NB.png",width=500)
    col3.write("")
    st.divider()

    col1, col2, col3 = st.columns([1,2,1])
    col1.write("blabla")
    col2.image("Graphes/Année_Mégafeux.png",width=500)
    col3.write("")
    st.divider()

    col1, col2, col3 = st.columns([1,2,1])
    col1.write("blabla")
    col2.image("Graphes/Décennie_Mégafeu_NB.png",width=500)
    col3.write("")
    st.divider()
    
    col1, col2, col3 = st.columns([1,2,1])
    col1.write("blabla")
    col2.image("Graphes/Végétation_mégafeu.png",width=900)
    col3.write("")
    st.divider()
        


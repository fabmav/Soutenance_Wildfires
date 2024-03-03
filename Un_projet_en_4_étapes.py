import streamlit as st

st.set_page_config(page_title="Analyse des feux de forêts aux USA", page_icon="Fire_logo.png",)



col1, col2, col3= st.columns([1,10,1])
col1.write("")
col2.title("Analyse des feux de forêts aux USA : un projet en 4 étapes")
col3.write("")
st.write("")
col1, col2, col3, col4,col5 = st.columns([2,2,3,2,3])
col1.subheader("🔎 Exploration")
col2.subheader("👌Préparation")
col3.subheader("📊 Data Visualisation")
col4.subheader("🤖 Modélisation")
col5.subheader("🔥 Conclusion & perspectives")
st.write("")
st.divider()

col1, col2, col3, col4= st.columns([2,1,6,2])
col1.write("")
col2.image("logofs.gif")
col3.write("© Short, Karen C. 2022. Spatial wildfire occurrence data for the United States, 1992-2020 [FPA_FOD_20221014]. 6th Edition. Fort Collins, CO: Forest Service Research Data Archive. https://doi.org/10.2737/RDS-2013-0009.6")
col4.write("")

st.divider()

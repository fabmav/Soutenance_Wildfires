import streamlit as st

st.set_page_config(page_title="Modélisation", page_icon="Fire_logo.png",)

pages=["Classification","Time Series"]
page = st.sidebar.radio("Cliquez sur la partie à afficher", pages)

if page == pages[0] : 

    st.write('## Modèle de classification')
    tab1, tab2= st.tabs(["Modèles de classification","Tests Statistiques"])
    with tab1:
         # Boutons pour chaque modèle
        st.write('##### Dataset : <span style="color:red;">[2018, 2019, 2020]</span>', unsafe_allow_html=True)
        st.write('**Proportion du jeu de test :** <span style="color:red;">**25%**</span>', unsafe_allow_html=True)
        test_size_percentage = st.slider("Le pourcentage du jeu de test", 20, 30, 25)
        selected_model = st.radio("Sélectionnez un modèle", ["LogisticRegression", "DecisionTreeClassifier", "RandomForestClassifier", "SVM", "Gradient Boosting", "knn"])

        if selected_model == "LogisticRegression":
            col1, col2 = st.columns(2)
            col1.metric("Score X_test", "0.6471896781847842")
            col2.metric("Score X_train", "0.6525264009985726")
            # Ajoutez les autres métriques spécifiques à LogisticRegression ici
    
        elif selected_model == "DecisionTreeClassifier":
            col1, col2 = st.columns(2)
            col1.metric("Score X_test", "0.5963221118196649")
            col2.metric("Score X_train", "0.9997713664254686")
            # Ajoutez les autres métriques spécifiques à DecisionTreeClassifier ici
    
        elif selected_model == "RandomForestClassifier":
            col1, col2 = st.columns(2)
            col1.metric("Score X_test", "0.6554204360077117")
            col2.metric("Score X_train", "0.9997342907106797")
            
            # Matrice de confusion et Classification Report
            st.write('Classification Report & Matrice de Confusion du RandomForestClassifier :')
            st.image("Matrice de confusion et Classification Report.png")
    
            # Features Importances
            st.write('Features Importances du RandomForestClassifier (20 premières fonctionnalités) :')
            st.image("FeatImportance.png")
    
            # Ajustement des hyperparamètres
            st.write('#### Ajustement des hyperparamètres du RandomForestClassifier : <span style="color:blue;">Grid Search</span>', unsafe_allow_html=True)   
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("max_depth", "None")
            col2.metric("min_samples_leaf", "1")
            col3.metric("min_samples_split", "10")
            col4.metric("n_estimators", "200")
               
            st.metric("Score X_test", "0.6778140293637847")
            st.write("Le modèle RandomForest performe mieux sans limitation de la profondeur des arbres.")
            st.write("L'optimisation des hyperparamètres a contribué à améliorer la performance du RandomForest par rapport à ses paramètres par défaut. Il semble mieux généraliser aux données non vues dans l'ensemble de test.")
               
            st.write('Classification Report & Matrice de Confusion du RandomForestClassifier après ajustement des hyperparamètres :')
            st.image("Matrice Confusion et Classification Report après optimisation.png")
            st.write('Le modèle semble bien performant pour les classes A et B, mais a des difficultés avec les autres classes.')
            st.write('Défis potentiels dans la classification des classes moins fréquentes ou moins bien représentées.')
            st.write("Rappel sur la distribution des classes de feu :")
            st.image("DistNormalClass.png")  
            st.write("La distribution des classes prédite par le RandomForestClassifier :")
            st.image("Distribution des classes predites.png") 
            st.write('Les classes moins fréquentes (F et G) présentent des difficultés plus importantes pour le modèle.')
            st.write('Quelques prédictions du RandomForestClassifier (15 premières lignes) :')
            st.image("Tableau des valeurs réelles et prédites.png")
            st.write('#### Rééquilibrage de classe : <span style="color:blue;">SMOTE</span>', unsafe_allow_html=True)
            st.write("<span style='color:blue;'>Synthetic Minority Over-sampling Technique :</span> Technique de suréchantillonnage des minorités synthétiques :", unsafe_allow_html=True)
            st.write("L'objectif principal de SMOTE est de générer des exemples synthétiques de la classe minoritaire, de manière à équilibrer le nombre d'exemples entre les classes.")

        # svm
        elif selected_model == "SVM":
            col1, col2, col3 = st.columns(3)
            col1.metric("Score X_test", "0.6731054426812991")
            
            # Gradient Bosting 
    
        elif selected_model == "Gradient Boosting":
            col1, col2, col3 = st.columns(3)
            col1.metric("Score X_test", "0.6499147263829156")
            
            #  KNN
    
        elif selected_model == "knn":
            col1, col2, col3 = st.columns(3)
            col1.metric("Score X_test", "0.6440753373869198")
      
    with tab2:
        selected_test = st.radio("Sélectionnez un test", ["Kruskal-Wallis", 
                                                      "Corrélation Pearson", 
                                                      "Corrélation Spearman"])
        if selected_test == "Kruskal-Wallis":
            st.write("#### Végétation régionale & Taille des feux")
            st.write("H0 : Il n'y a pas d'effet significatif de la végétation sur la Taille des feux.")
            col1, col2 = st.columns(2)
            col1.metric("KruskalResult(statistic)", "97811.02482749475")
            col2.metric("pvalue", "0.0")
            st.write("On rejette H0 : Il y a un effet statistique significatif de la végétation sur la taille des feux.")
            st.write("#### Cause & Taille des feux")
            st.write("H0 : Il n'y a pas d'effet significatif de la cause sur la Taille des feux.")
            col1, col2 = st.columns(2)
            col1.metric("KruskalResult(statistic)", "29011.246268456314")
            col2.metric("pvalue", "0.0")
            st.write("On rejette H0 : la cause des feux semble bien avoir un impact significatif sur la taille des feux : cas des causes naturelles en majorité dans le Sud Ouest et Nord Ouest.")
    
        
    
        elif selected_test == "Corrélation Pearson":
            st.write("#### Précipitation moy. mens. & Taille des feux")
            st.write("H0 : Il n'y a pas de corrélation significative entre la précipitation et la Taille des feux.")
            col1, col2 = st.columns(2)
            col1.metric("Corrélation de Pearson(précipitation moy.mens.)", "-0.02047855970785961")
            col2.metric("pvalue", "3.49452e-207")
            st.write("On rejette H0 : corrélation statistiquement significative entre Précipitation moy. mens. et Taille des feux, mais une corrélation négative très faible et proche de 0 (-0,02).")
            st.write('#### Température moy. mens. & Taille des feux')
            st.write("H0 : Il n'y a pas de corrélation entre la Température moy.mens. et la Taille des feux.")
            col1, col2 = st.columns(2)
            col1.metric("Corrélation de Pearson(température moy.mens.)", "0.011750792216244654")
            col2.metric("pvalue", "1.61714208e-69")
            st.write("On rejette H0 : Il existe une faible relation monotone entre la taille des feux et la température moyenne mensuelle. Même si la corrélation est statistiquement significative (p-value = 0), la variation de la température moyenne mensuelle ne semble pas expliquer d’une manière significative la taille des feux.")
    
        elif selected_test == "Corrélation Spearman" :
            st.write('#### Précipitation moy. mens. & Taille des feux')
            st.write("H0 : Il n'existe pas de relation monotone significative entre la précipitation et la Taille des feux.")
            col1, col2 = st.columns(2)
            col1.metric("Corrélation de Spearman", "0.15550443118114127")
            col2.metric("pvalue", "0.0")
            st.write("On rejette H0 : Le test de Spearman confirme qu’il existe bien une relation statistique significative entre ces 2 variables.")
            st.image("Relation entre precipitation et taille des feux.png")
            st.image("Correlation entre preicipitation et taille feu.png")
    
            st.write("#### Température moy. mens. & Taille des feux")
            st.write("H0 : Il n'existe pas de relation monotone significative entre la Température et la Taille des feux.")
            col1, col2 = st.columns(2)
            col1.metric("Corrélation de Spearman", "-0.04421683488823663")
            col2.metric("pvalue", "0.0")
            st.write("On rejette H0 : le test de Spearman confirme le rejet de notre hypothèse nulle selon laquelle il n’y a pas de corrélation entre ces 2 variables.")
            st.image("Relation entre température et taille des feux.png")
            st.image("Correlation entre temperature et taille feu.png")
    
            st.write("Plusieurs facteurs peuvent expliquer la taille des incendies (végétation de la région, cause, précipitation moyenne, température moyenne).")
    

if page == pages[1] : 

    st.header('Time Series avec Prophet')


    st.write('Notre base de données comportant plusieurs variables temporelles, il était logique de s’intéresser aux séries temporelles ou Time Series. Nous nous sommes tournés vers la librairie Prophet de Meta (ou Facebook Prophet), librairie open source et facile d’utilisation, pour mettre en œuvre cette Time Series. Nous avons testé le modèle multiplicatif et le modèle additif de Facebook Prophet et nous avons vu que le premier correspond mieux à nos données. Notre objectif est d’essayer de prédire la décennie suivante (2021-2030) par rapport à la dernière décennie (2011-2020) du jeu de données.')
    st.write('Premières tendances sur le jeu de données filtré :')

    st.image("Tendances.png")


    st.write('On crée alors un dataset qui contient la décennie retenue et la décennie à prédire. Puis Prophet calcule la prédiction sur les feux pour la décennie suivante.')

    st.image('Première prédiction.png')

    st.write('La prédiction, qui commence en 2021 sur ce graphique, montre des feux en croissance régulière, mais constante.')

    st.write('On peut vérifier les tendances et la saisonnalité en affichant les composantes de la prédiction.')

    st.image('Composantes de la prédiction.png')

    st.write('Le premier graphique montre que la tendance est croissante. Le deuxième graphique indique que les feux sont constants et plus fréquents en avril et en juillet, ce qui confirme nos premières observations.')

    st.write('Les change points (points de changements) sont les points dans le temps où les séries temporelles présentent des changements abrupts dans la trajectoire.')


    st.image('Première prédiction avec change points.png', caption = 'Première prédiction avec change points' )

    st.write('Premières métriques')
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Horizon", "37 jours",  "365 jours")
    col2.metric("RMSE", "106.38", "-51.93")
    col3.metric("MAE", "77.48", "-36.85")
    col4.metric("MAPE", "54%", "57%")

    st.write('Prédiction avec ajustement des hyperparamètres')

    st.image('Prédiction avec hyperparamètres ajustés.png')

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Horizon", "37 jours",  "365 jours")
    col2.metric("RMSE", "104.8", "-52.86")
    col3.metric("MAE", "76.42", "-37.22")
    col4.metric("MAPE", "82%", "-58%")


    st.write('L’ajustement des hyperparamètres n’a pas permis d’obtenir de meilleurs résultats sur les métriques. Bien au contraire, les pourcentages d’erreurs dans la prédiction sont plus élevés.')

    st.write('Si Prophet est adapté à la prévision de données contenant des outliers, les métriques telles que la RMSE et la MAE ne le sont pas. Elles y sont, au contraire, très sensibles, ce qui peut expliquer que notre modèle échoue à prédire la prochaine décennie. Le même problème s’est présenté sur le modèle de classification qui a échoué à prédire les classes D, E, F et G.')

    st.write('Pour aller plus loin : nous pourrions envisager de travailler sur une autre Time Series, mais en supprimant certaines classes de feux.')


## Présentation du projet : 


:red[*__L'ONU prédit une augmentation du nombre de feu de forêt de 50% d'ici l'année 2100.__*]
L'organisation cite le changement climatique et la transformation des éco-systèmes comme causes principales de cette dynamique.\
[source](https://www.unep.org/news-and-stories/press-release/number-wildfires-rise-50-2100-and-governments-are-not-prepared)


Nous avons pu, à travers l'étude d'un dataset contenant des données sur les feux de forêt ayant eu lieu aux états-unis de 1992 à 2020, essayer de mieux comprendre ce qui déclenche les feux de forêts, leur évolution au cours des 30 dernières années et tester des modèles prédictifs.\
[jeu de donnée Kaggle Wildfire 1992 à 2020](https://www.kaggle.com/datasets/behroozsohrabi/us-wildfire-records-6th-edition)

## Quelques chiffres clés : 
*(données nettoyées)*

    - 2,2 millions de feux de forêt répertoriés dans la base
    - 58 millions d'hectares brûlés sur 30 ans
    - la surface brulée augmente d'environ 47% par décénnie
    - 0.04% des incendies font plus de 10 000 ha et représentent à eux seuls 
    48% de la surface brulée.

L'évolution de la surface brulée ainsi que le fait qu'un petit nombre d'incendies puissent avoir un tel impact nous a interpelé. :red[**Ces chiffres nous ont incité à orienter notre travail l'analyse et la prédiction de la taille des incendies.**]



Nous avons organisé notre travail de la façon suivante : 
* Analyse du jeu de donnée brut
* Nettoyage du dataset d'origine et et ajout de données complémentaires
* Dataviz & statistiques
* Machine Learning



## Difficultés & limites : 

L'analyse des incendies et des feux de forêts est un domaine à la croisée de la climatologie, de la géographie, de la sociologie et de bien d'autres domaines.

La quantité de donnée devient vite gigantesque. Manipuler ces données devient vite un défit et les temps de calculs peuvent devenir vite très long.

Il nous a également fallu apprendre à maîtriser des modules non étudiés dans les cours comme GeoPandas, ...
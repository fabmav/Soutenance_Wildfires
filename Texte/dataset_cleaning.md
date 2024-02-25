## Nettoyage du jeu de donnée : 

les principales étapes du pre processing ont été les suivantes : 
---
1.  :red[**suppression des données non pertinantes ou avec trop de na**] : 
    de nombreuses colonnes correspondaient à des codes d'identifications d'agences américaines (régionales, office des feux et forêts...). Nous avons supprimés ces variables car elles présentaient beaucoup de na et n'allaient pas nous servir pour l'analyse.
---
2. :red[**la problématique des dates**] : 
    Nous avons envisagé au début de l'analyse de nous intéresser à la durée des incendies. Cependant la variable "fin de l'incendie" présentait elle aussi trop de na pour être exploitable. Nous n'avons pas non plus pu corréler ces na à un facteur précis (source de l'info, période spécifique etc...). Nous avons au final également supprimé cette colonne
---
3. :red[**Périmètre d'analyse**] : 
    Nous avons supprimé les donnés qui ne correspondaient pas aux états contigües américains (Alaska, Hawaï et Puerto Rico). Nous avons en effet estimé que ces territoires avaient leurs problématiques spécifiques.
---
4. :red[**transformations usuelles**] : 
    mise au format des champs de date, conversions des données numériques en valeur métrique etc...
---
## Ajout de donnée : 

Nous avons rapidement constaté que le jeu de donnée ne contenait aucune donnée météorologique ni sur la végétation Par ailleurs, les données géographiques était incomplètes : il manquait certains nom de comtés, enfin, il nous a semblé utile de regrouper les états par grande région pour simplifier les analyses
---
1. :red[**les régions**] : 
    Nous avons utilisé la carte disponible [ici]( https://www.usgs.gov/programs/climate-adaptation-science-centers/casc-network-and-region-maps#:~:text=The%20CASCs%20are%20divided%20into,%2C%20South%20Central%2C%20and%20Southeast) pour regrouper les états américains par région.
---
2. :red[**les comtés**] :
    [lien databse comté](https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html)
    le but était d'avoir le nom du comté pour l'ensemble des lignes du dataset. Avec geoPandas, il a été possible de mapper les coordonnées des incendies avec les limites géographiques (lat,long) des comtés.
---
3. :red[**La Météo**] : 
    Le but était d'ajouter au dataset des informations sur les précipitations et la température moyenne. L'hypothèse étant que ces données ont une influence sur l'occurence et la taille des incendies. Nous aurions pu  Nous sommes passé par l'api des services météo us. La difficulté a été de gérer la quantité de donnée généré (temps de calcul et déconnexions régulière de l'api).
    Les données extraites correspondaient à des stations météo dont les coordonnées géoraphiques étaient renseignées. A partir de là, il était possible avec GeoPandas de trouver le point 
    Il eût été possible d'extraire plus d'informations (vent, humidité etc...). Cependant extraire la quantité de donnée nous a semblé trop importante.
---
4. :red[**Végétation**] : 
    Les feux de forêts ne prennent pas la même ampleur en fonction de la végétation (forêts de résineux, forêt à feuillage caduc, prairie, zone humide...). Il semblait donc intéressant de récupérer des données sur la végétation.
    Les données étaient disponibles ici et là.
    La méthode a consisté en ... et en travaillant avec GeoPandas
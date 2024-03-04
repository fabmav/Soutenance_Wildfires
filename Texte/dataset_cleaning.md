## Nettoyage du jeu de donnée : 

Les principales étapes du pre processing ont été les suivantes : 
---
1.  :red[**suppression des données non pertinentes ou avec trop de na**] : 
    de nombreuses colonnes correspondaient à des codes d'identifications d'agences américaines (agences régionales, office des feux et forêts...). Nous avons supprimé ces variables car elles présentaient beaucoup de Nan et n'allaient pas nous servir pour l'analyse.
---
2. :red[**la problématique des dates et de la durée des incendies**] : 
    Nous avons envisagé au début de l'analyse de nous intéresser à la durée des incendies. Cependant la variable "containment date" qui indiquait la date de maîtrise de l'incendie présentait elle aussi trop de Nan pour être exploitable. Nous n'avons pas non plus pu corréler ces Nan à un facteur précis (source de l'info, période spécifique etc...). Nous avons au final également supprimé cette colonne.
---
3. :red[**Périmètre d'analyse**] : 
    Nous avons supprimé les données qui ne correspondaient pas aux états contigus américains (Alaska, Hawaï et Puerto Rico). Nous avons en effet estimé que ces territoires avaient leurs problématiques spécifiques.
---
4. :red[**transformations usuelles**] : 
    Mise au format des champs de date, conversions des données numériques en valeur métrique etc...
---
## Ajout de donnée : 

Nous avons rapidement constaté que le jeu de donnée ne contenait aucune donnée météorologique ni sur la végétation. Par ailleurs, les données géographiques étaient incomplètes : il manquait certains noms de comtés, enfin, il nous a semblé utile de regrouper les états par grandes régions pour simplifier les analyses
---
1. :red[**les régions**] : 
    Nous avons utilisé la carte disponible [ici]( https://www.usgs.gov/programs/climate-adaptation-science-centers/casc-network-and-region-maps#:~:text=The%20CASCs%20are%20divided%20into,%2C%20South%20Central%2C%20and%20Southeast) pour regrouper les états américains par région.
---
2. :red[**les comtés**] :
    [lien databse comté](https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html)
    le but était d'avoir le nom du comté pour l'ensemble des lignes du dataset. Avec geoPandas et shapely, il a été possible de mapper les coordonnées des incendies avec les limites géographiques des comtés.
---
3. :red[**La Météo**] : 
    Le but était d'ajouter au dataset des informations sur les précipitations et la température moyenne à la date du déclenchement de l'incendie.
    L'hypothèse étant que ces données exercent une influence sur l'occurrence et la taille des incendies.\
    Nous sommes passé par l'api des services météo us. La source des données est [disponible ici](https://www.ncei.noaa.gov/access).\
    Il eût été possible d'extraire plus d'informations (vent, humidité de l'air etc.), cependant la quantité de donnée à extraire, et les temps de calculs nous ont semblé trop importants.\
     La difficulté a été de gérer la quantité de donnée généré (temps de calcul et déconnexions régulière de l'api).\
    Les données extraites correspondaient à des stations météo dont les coordonnées géographiques étaient renseignées. A partir de là, il était possible avec GeoPandas de trouver le point 

---
4. :red[**Végétation**] : 
    Les feux de forêts ne prennent pas la même ampleur en fonction de la végétation (forêts de résineux, forêt à feuillage caduc, prairie, zone humide...). Il semblait donc intéressant de récupérer des données sur la végétation.
    Nous avons utilisé deux sources de données :\
    Une avec un niveau de précision fin [disponible ici :](https://water.usgs.gov/GIS/dsdl/ds240/index.html)\
    Une autre avec un niveau macro (précision de 0.5° de latitude/longitude)  [disponible là :](https://www.ncei.noaa.gov/erddap/griddap/areaveg_hyde_by_time_latitude_longitude.html)\
    Tout comme pour les données météo, il a fallu, grâce à GeoPandas et Shapely identifier la végétation correspondant aux coordonnées d'un incendie.
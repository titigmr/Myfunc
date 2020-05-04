from scipy.stats import kruskal
from scipy.stats import f_oneway
import numpy as np
import pandas as pd


def quali_quanti(data,quali,quanti, parametric=True):
    """
    Applique un test entre une variable quantitative et une ou plusieurs variables 
    qualitatives.
    
    Paramètres : 
    -----------
    data : jeu de données sous forme d'un dataframe
    quali : données des variables qualitatives 
    quanti : variable quantitative
    parametric : booléan (True par défaut) pour appliquer un test 
                non-paramétrique (Kruskal) ou paramétrique (ANOVA)
                
    Retour : 
    --------
    Dataframe : statistique de test et p-value associée pour chaque variable  
    
    """
    
    if parametric :
        func = f_oneway
    else : 
        func = kruskal
    
    list_stats = []
    list_pval = []

    for variable in list(quali.columns) :

        liste_var = []

        for i in list(np.unique(data[variable])):
            col = data[[quanti,variable]][data[variable] == i]
            liste_var.append(col[quanti])

        list_stats.append(func(*liste_var).statistic)
        list_pval.append(func(*liste_var).pvalue)

        list_var = []
    
    feature_names = list(quali.columns)
    return pd.concat([pd.Series(list_stats, index=feature_names, name="Stats"), 
                      pd.Series(list_pval, index=feature_names, name="P-valeur")], axis=1)


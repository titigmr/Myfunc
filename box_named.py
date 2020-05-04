 def box_named(data, colums, vertical=True, fsize=12):
    """
    Box-plot affichant les index des valeurs outliers.

    Paramètres 
    -----------
    
    data : dataframe contenant les données
    colums : chaine de caractère du nom de la colonne 
    vertical : orientation des box-plot (vertical par défaut)
    fsize : taille de la police des index des valeurs outliers
    """
    
    B = plt.boxplot(data[colums], vert=vertical, patch_artist=True, 
                    flierprops={'marker':"D",'markersize':'3','markerfacecolor':'b'}, medianprops={'color':'grey', 'lw':'2'}, 
                    boxprops={'color':'grey','lw':'2'}, whiskerprops={'color':'grey','lw':'2'},
                   capprops={'color':'grey','lw':'2'})
    
    if vertical == True : 
        fliers = B["fliers"][0].get_ydata()

        for f in fliers :
            xpos = B["medians"][0].get_xdata()[0]
            name = list(data[colums].index[data[colums] == f])[0]
            plt.text(xpos + 0.1, f,name, fontsize=fsize)
    else :
        fliers = B["fliers"][0].get_xdata()

        for f in fliers :
            ypos = B["medians"][0].get_ydata()[0]
            name = list(data[colums].index[data[colums] == f])[0]
            plt.text(f, 0.2 + ypos, name, fontsize=fsize, rotation='vertical')
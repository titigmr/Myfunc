from wordcloud import WordCloud
import matplotlib.pyplot as plt


def plot_word_cloud(text, masque=None, background_color = "black", stop_words=None) :
    """
    Créer des WordCloud avec un masque au choix.

    Paramètres 
    ----------
	text : le texte brute
	masque : le chemin d'une image 
	background_color : choisir le fond

    Retour 
    -------
	WordCloud 
    """


    if masque != None :
    	mask_coloring = np.array(Image.open(str(masque)))
    else : 
    	mask_coloring = None
   
    wc = WordCloud(background_color=background_color, 
    	max_words=200, stopwords=stop_words, 
    	mask = mask_coloring, 
    	max_font_size=50, random_state=42)

    plt.figure(figsize= (20,10))
    wc.generate(text)
    plt.imshow(wc)
    plt.show()


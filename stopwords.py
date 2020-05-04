


import pandas as pd 

def stopwords():
	stopwords_csv = pd.read_csv('stopwords.csv', delimiter=';',encoding="ISO-8859-1").iloc[:,:2]
	stopwords_csv.MOT = stopwords_csv.MOT.apply(lambda x : x.replace('\x92',"\'"))
	stopwords = set(stopwords_csv.MOT)
	return stopwords
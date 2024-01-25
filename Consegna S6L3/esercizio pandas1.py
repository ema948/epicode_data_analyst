# Esercizio 1
# Andiamo a questo link: https://www.kaggle.com/datasets/ahmettezcantekin/beginner-datasets e scaricare wine.csv; 
# Calcoliamo le informazioni statistiche base (numerosità, modie, mode, mediane, quartili, ecc) sulle colonne numeriche 

import pandas as pd 
# carica il dataset
wine = pd.read_csv("wine.csv")

# visualizza la dimensione del file (righe e colonne)
print(wine.shape)
dimensions = wine.shape
print("Righe:", dimensions[0], "colonne", dimensions[1])

# visualizza le prime righe del dataset per esaminare i dati
print(wine.head())

# informazioni statistiche di base sulle colonne numeriche (count, min, media - mediana, quartili, max)
s = wine.describe()
print("Informazioni statistiche di base:\n", s)

# informazioni sulla moda
mode = wine.mode()
#mode = wine.mode(axis = 0, numeric_only = True)
print("Informazioni sulla moda: \n", mode)


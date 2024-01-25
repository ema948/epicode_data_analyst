# Esercizio 2
# Scarichiamo l'Iris dataset da qui: https://archive.ics.uci.edu/dataset/53/iris 
# Troveremo un file .data, che è un CSV, e un file .names con i metadati; 
# questa versione del dataset non ha i nomi di colonna. 
# Leggiamo il file e carichiamolo in un DataFrame mediante pd.read_csv() senza utilizzare altri parametri 
# Stampiamo le prime cinque righe 
# Stampiamo i nomi di colonna: cosa c'è nella colonna relativa?

import pandas as pd 
# carica dataset 
file_name = "data.csv"
data = pd.read_csv(file_name)

# stampa le prime 5 righe
print(data.head())

# mostra righe e colonne
print(data.shape)

# nomi colonne aggiunte
data = pd.read_csv(file_name, 
                   header = 0,
                   names = ["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "class"])

print(data)

# mostra solo l'ultima colonna
"""data = pd.read_csv(file_name, 
                   usecols = [4], 
                   names = ["class"])
print(data)

mode = data.mode()
print(mode)"""

# salvare file in Excel (con estensione "pip install openpyxl")
#data.to_excel("Iris.xlsx", sheet_name="Class Iris")

# stampa le ultime tre righe
"""print("Ultime tre righe")
print(data.tail(3))"""

# stampare da 100 a 110
"""print(data[100:111])

# calcolo statistico di base 
s = data[100:110].describe()
print(s)
s = data.iloc[100:110].describe()
print(s)"""

#print(data.columns)
#print(data.index)
#print(data.values)





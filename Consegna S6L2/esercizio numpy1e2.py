# Esercizio 1
# Abbiamo una lista di liste: mat = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]] 
# Che tipo di struttura dati o matematica potrebbe rappresentare? 
# Notare che tutte le liste "interne" sono della stessa dimensione Come facciamo per accedere ad un elemento in particolare?

# matrice: lista di liste
mat = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]

# per accedere all'elemento 7 che si trova nella seconda lista in terza posizione
elemento = mat[1, 2]
print(elemento)

#Esercizio 2
# trasformiamo la lista in un array NumPy
import numpy as np
mat = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
mat = np.array(mat)

elemento = mat[1, 2]
print(elemento)
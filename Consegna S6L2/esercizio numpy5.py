# Esercizo 5
# Creiamo un ndarray con gli stessi valori. 
# Ci sono due modalità: inizializzare un array e poi inserire i valori nelle posizioni adatte, 
# oppure creare una lista di liste e poi effettuare un casting

import numpy as np 

lista = [[1, 1, 1, 1], [5, 1, 1, 1,], [20 , -4, 0, 42]]

# inizializzare un array
matrice = np.array([[1, 1, 1, 1],
                    [5, 1, 1, 1],
                    [20, -4, 0, 42]])

array = np.array(matrice)
print(array)

# lista di liste e casting
array = np.array(lista)
print(array)
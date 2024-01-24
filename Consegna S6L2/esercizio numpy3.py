# Esercizio 3
# Abbiamo il seguente array NumPy: 
# linear_data = np.array([x for x in range(27)]) 
# Lo ridimensioniamo mediante il metodo .reshape(): reshaped_data = linear_data.reshape((3, 3, 3)) 
# Quante dimensioni ha il nuovo array? Come facciamo per accedere ai singoli elementi?

import numpy as np
linear_data = np.array([x for x in range(27)])

# ridimensioniamo mediante il metodo .reshape(): 
reshaped_data = linear_data.reshape((3, 3, 3)) 

print(linear_data.reshape(3, 3, 3))

# per accedere all'elemento 15: seleziono la seconda matrice (1), la terza riga (2) e prima colonna (0)
elemento = reshaped_data[1, 2, 0]
print(elemento)


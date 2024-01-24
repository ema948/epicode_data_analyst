# Esercizio 4
# In una catena di montaggio abbiamo una struttura metallica di 28.75 cm di lunghezza; 
# per assicurarne la stabilità, è necessario inserire 15 rivetti, dei quali uno all'inizio e uno alla fine, 
# e tutti quanti separati dalla stessa distanza; come possiamo calcolare i punti esatti in cui inserire i rivetti tramite NumPy?

import numpy as np 

lunghezza = 28.75
rivetti = 15

distanza_rivetti = lunghezza / (rivetti - 1)

inserimento = np.arange(0, 28.75, distanza_rivetti)

print(inserimento)

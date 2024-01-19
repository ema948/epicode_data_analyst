# Esercizio 3
# creazione di una classe Cerchio con un attributo raggio e metodi per calcolare l'area e la circonferenza
    
class Cerchio:
    def __init__(self, raggio):
        self.raggio = raggio

# metodo per calcolare l'area e la circonferenza del cerchio
           
    def calcolo_area(self):
        return 3.14 * self.raggio**2
    
    def calcolo_circonferenza(self):
        return 2 * self.raggio * 3.14
        
       
# testiamo l'algoritmo 
    
raggio = 5
cerchio = Cerchio(raggio)

area = cerchio.calcolo_area()
circonferenza = cerchio.calcolo_circonferenza()
print("Se il raggio è", raggio, ", l'area e la circonferenza del cerchio sono rispettivamente:", area, "e", circonferenza)

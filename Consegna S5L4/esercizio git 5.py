# Esercizio 5
# crea una classe Prodotto con attributi: nome, prezzo e quantità disponibile. 
# Aggiungi metodi per calcolare il costo totale e verificare la disponibilità

class Prodotto:
    def __init__(self, nome, prezzo, quantitàdisponibile):
        self.nome = nome
        self.prezzo = prezzo
        self.quantitàdisponibile = quantitàdisponibile

# metodo per calcolare il costo totale
        
    def costo_totale(self, quantitàacquistata):
        return self.prezzo * quantitàacquistata
        
# metodo per verificare la disponibilità

    def disponibilità(self, quantitàacquistata):
        if quantitàacquistata > self.quantitàdisponibile:
            return False
        return True
    print("Quantità disponibile in magazzino inferiore alla quantità richiesta")

# testiamo l'algoritmo 

prodotto = Prodotto(quantitàdisponibile = 5, nome = "iPhone 12 mini", prezzo = 560)
quantità_acquisto = 10
importo_totale = prodotto.costo_totale(quantità_acquisto)
disponibile = prodotto.disponibilità(quantità_acquisto)

if disponibile:
   print("Spendi complessivamente:", importo_totale, "euro")
else:
    print("Acquisto non possibile!")

    
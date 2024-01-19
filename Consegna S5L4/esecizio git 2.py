# Esercizio 2
# creare una classe Libro con attributi: titolo, autore e anno di pubblicazione. 
# Aggiungi un metodo per verificare se il libro è recente
        
class Libro:
    def __init__(self, titolo, autore, anno_pubblicazione):
        self.titolo = titolo
        self.autore = autore
        self.anno_pubblicazione = anno_pubblicazione

# metodo per stampare
        
    def stampa(self):
        print(self.titolo, self.autore, self.anno_pubblicazione, sep = ", ")
        
# metodo per verificare se il libro è recente
        
    def libro_recente(self, anno_corrente):
        return anno_corrente - self.anno_pubblicazione <= 3

# testiamo l'algorirmo 
    
libro1 = Libro(titolo = "Introduzione alla psicoanalisi", autore = "Freud", anno_pubblicazione = 2023)
anno_corrente = 2024
libro1.stampa()

if libro1.libro_recente(anno_corrente):
        print("Il libro è stato pubblicato di recente")


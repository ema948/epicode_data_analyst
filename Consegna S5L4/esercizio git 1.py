# Esercizio 1
# crea una classe Persona con attributi: nome, cognome e età. 
# Inserisci un metodo per stampare le informazioni della persona

class Persona:
    def __init__(self, nome, cognome, età):
        self.nome = nome
        self.cognome = cognome
        self.età = età

# metodo per stampare le informazioni della persona
        
    def stampa(self):
        print(self.nome, self.cognome, "età", self.età, "anni")

# testiamo l'algoritmo 

persona = Persona(cognome = "Emanuela", nome = "Cannarella", età = 29)
persona.stampa()
    


            
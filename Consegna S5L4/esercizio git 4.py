# Esercizio 4
# crea una classe ContoBancario con attributi: saldo e metodo per depositare e prelevare denaro

class ContoBancario:
    def __init__(self, saldo):
        self.saldo = saldo

# metodo per depositare e prelevare denaro 

    def deposito(self, quantità):
        self.saldo += quantità
    
    def prelievo(self, quantità):
        if quantità <= self.saldo:
            self.saldo -= quantità
        else:
            print("Mi dispiace, fondi insufficienti. Impossibile effettuare la richiesta. Operazione annullata")

    def saldo_contabile(self):
        return self.saldo 
    
# testiamo l'algoritmo 
    
conto = ContoBancario(1500)
print("Saldo iniziale:", conto.saldo)

deposito_denaro = 450
conto.deposito(deposito_denaro)
print("Saldo dopo il deposito:", conto.saldo)

prelievo_denaro = 200
conto.prelievo(prelievo_denaro)
print("Saldo dopo il prelievo:", conto.saldo)

# tentativo di prelevare più di quanto disponibile

prelievo_denaro2 = 2000
print("Si sta cercando di prelevare:", prelievo_denaro2)
conto.prelievo(prelievo_denaro2)
print("Saldo finale:", conto.saldo)

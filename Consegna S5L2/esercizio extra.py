# Esercizio 2:  Chiedere all’utente di inserire un numero intero compreso tra 1 e 10. 
# Se il numero inserito dall’utente è compreso in questo intervallo, stampare “Numero valido”, 
# altrimenti stampare “Numero non valido”.
    
n = int(input("Inserisci un numero da 1 a 10: "))

if n >= 1 and n <= 10:
    print("Numero valido")
else:
    print("Numero non valido")
""" Esercizio 10: Abbiamo una lista con i guadagni degli ultimi 12 mesi: 
guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50] 
usando un costrutto while, calcolare la media dei guadagni e stamparla a video """

guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]
indice = 0
somma = 0

while indice < len(guadagni):
    somma += guadagni[indice]
    indice += 1
print("La media è: ", somma / len(guadagni))

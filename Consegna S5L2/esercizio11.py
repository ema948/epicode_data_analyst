""" Esercizio 11: abbiamo una lista di codici fiscali: 
lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", 
"XYZABC01D05A789F", "DEFGHI95J06A987G"] 
Trovare i codici fiscali che contengono "95", metterli in una lista, e alla fine stamparla;
Inoltre, per ognuno di essi, stampare a video i caratteri relativi al nome e quelli relativi al cognome """

lista = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"] 
selezionati = []
indice = 0
find = "95"

while indice < len(lista):
    if find in lista[indice]:
        selezionati.append(lista[indice])
    indice += 1 

print("Persone nate nel '95: ", selezionati)

while lista in selezionati:
    nome = selezionati[4:7]
    cognome = selezionati[:4]
    
print("Caratteri relativi al nome: ", nome, "quelli al cognome: ", cognome)
    
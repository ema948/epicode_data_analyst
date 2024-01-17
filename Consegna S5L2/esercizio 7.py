""" scriviamo un programma che chiede in input all'utente una stringa e visualizza i primi 3 caratteri, 
seguiti da 3 punti di sospensione e quindi gli ultimi 3 caratteri (Stavolta facciamo attenzione a tutti 
i casi particolari, ovvero implementare soluzioni ad hoc per stringhe di lunghezza inferiore a 6 caratteri) """

stringa = input("Inserisci una parola: ")

while len(stringa) < 6:
    print(stringa, " --> ", stringa[:3], "...", stringa[-3:])
    stringa *= 2
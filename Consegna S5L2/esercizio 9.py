""" calcolare (ma non stampare) le prime N potenze di K; ognuna di esse andrà memorizzata in coda a una lista. 
Alla fine, stampare la lista risultante. Proviamo con diversi valori di K, oppure facciamola inserire all'utente """

k = int(input("Dimmi un numero? "))
n = int(input("Elevato a ? "))
p = n
potenza = []

while(n >= 0):
    potenza.append(k**n)
    n -= 1
potenza.sort()
print("Prime ", p, " potenze di ", k, " => ", potenza)

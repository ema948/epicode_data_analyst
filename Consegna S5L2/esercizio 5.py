# Esercizio 4: calcolare e stampare tutte le potenze di 2 minori di 25000

n = 0
potenza = 1

while n <= 14 and potenza < 25000:
    print(2, "^", n, "=", 2**n)
    n += 1
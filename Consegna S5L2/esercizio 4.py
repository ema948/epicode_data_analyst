# Esercizio 3: calcolare e stampare tutte le prime N potenze di 2 utilizzando un ciclo while, domandando all'utente di inserire N

n = int(input("Quante potenze ^2 vuoi calcolare? "))
x = 0

while x <= n:
    print(2, "^", x, "=", 2**x)
    x += 1 
# Esercizio 7: memorizza e stampa tutti i divisori di un numero dato in input

n = num
d = 2
while n > 1:
    d = 2
    while d <= n and n > 1:
        if n % d == 0:
            divisori.append(d)
            n //= d
        d += 1
print("Divisori di", num, " = ", divisori)

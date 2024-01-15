-- Determina la quantità media disponibile per categoria di prodotto.
SELECT Categoria, AVG(QuantitaDisponibile) AS MediaPerCategoria
FROM buildweek1.prodotti_dataset
GROUP BY Categoria;
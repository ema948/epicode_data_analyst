-- Determina la categoria di prodotto con il maggior numero di vendite.
SELECT p.Categoria, SUM(t.QuantitaAcquistata) QuantitaVenduta
FROM buildweek1.prodotti_dataset p
INNER JOIN buildweek1.transazioni_dataset t ON p.ProdottoID=t.ProdottoID
GROUP BY p.Categoria
ORDER BY SUM(t.QuantitaAcquistata) DESC LIMIT 1;

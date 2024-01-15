-- Identifica i tre prodotti più venduti e la loro quantità venduta.
SELECT p.NomeProdotto, p. Categoria, t.QuantitaAcquistata
FROM buildweek1.prodotti_dataset p
INNER JOIN buildweek1.transazioni_dataset t ON p.ProdottoID=t.ProdottoID
ORDER BY t.QuantitaAcquistata DESC LIMIT 3;
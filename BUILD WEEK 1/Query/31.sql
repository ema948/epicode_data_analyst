-- Recensioni di prodotti piu venduti 'Prodotto 3485', 'Prodotto 4360', 'Prodotto 1154'
SELECT  NomeProdotto, AVG(Rating)
FROM ratings_dataset r
RIGHT JOIN prodotti_dataset p ON r.ProductID = p.ProdottoID
WHERE p.NomeProdotto IN ('Prodotto 3485', 'Prodotto 4360', 'Prodotto 1154')
GROUP BY p.NomeProdotto;

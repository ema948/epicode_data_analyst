-- Trova il prodotto con la recensione media più alta.
SELECT p.NomeProdotto, AVG(r.Rating) RecensioneMigliore, COUNT(RatingID) NumeroRecensioni
FROM buildweek1.prodotti_dataset p 
INNER JOIN buildweek1.ratings_dataset r ON p.ProdottoID=r.ProductID
GROUP bY p.NomeProdotto
ORDER BY AVG(r.Rating) DESC, COUNT(RatingID) DESC LIMIT 1; 
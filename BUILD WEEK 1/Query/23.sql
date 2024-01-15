-- Numero di clienti che hanno scritto recensioni
SELECT COUNT(DISTINCT(CustomerID)) NumeroClientiRecensori
FROM buildweek1.ratings_dataset;
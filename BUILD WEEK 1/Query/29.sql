-- Recensioni: clienti che hanno fatto almeno un ordine  
SELECT AVG(Rating)
FROM ratings_dataset
WHERE CustomerID IN (
        	SELECT DISTINCT(ClienteID)
        	FROM buildweek1.transazioni_dataset);

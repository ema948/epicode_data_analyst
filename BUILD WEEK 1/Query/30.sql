-- Recensioni: clienti che NON hanno fatto almeno un ordine 
SELECT AVG(Rating) 
FROM ratings_dataset
WHERE CustomerID NOT IN (
        	SELECT DISTINCT(ClienteID)
        	FROM buildweek1.transazioni_dataset);

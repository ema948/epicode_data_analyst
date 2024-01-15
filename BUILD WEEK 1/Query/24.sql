-- Media delle recensioni dei clienti che hanno effettuato transazioni sono più elevate delle recensioni medie totali
SELECT AVG(Recensioni.Rating) AS MediaReceAcquirenti
FROM (SELECT *
		FROM buildweek1.ratings_dataset
		WHERE CustomerID IN(SELECT DISTINCT(ClienteID) FROM buildweek1.transazioni_dataset)) Recensioni;
        
        
-- Media delle recensioni degli iscritti che non hanno effettuato acquisti
SELECT AVG(Recensioni.Rating) AS MediaReceIscritti
FROM (SELECT *
		FROM buildweek1.ratings_dataset
		WHERE CustomerID NOT IN(SELECT DISTINCT(ClienteID) FROM buildweek1.transazioni_dataset)) Recensioni;


-- Media generale dei rating
SELECT AVG(Rating) MediaReceGenerale
FROM buildweek1.ratings_dataset;
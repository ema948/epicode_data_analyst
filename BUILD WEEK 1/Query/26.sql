-- Numero di prodotti con una quantità disponibile inferiore alla media.
SELECT COUNT(Conteggio.NomeProdotto) NumeroProdotti
FROM (SELECT NomeProdotto, Categoria, QuantitaDisponibile
		FROM buildweek1.prodotti_dataset 
		WHERE QuantitaDisponibile<
			(SELECT AVG(QuantitaDisponibile)
			FROM buildweek1.prodotti_dataset)) Conteggio;
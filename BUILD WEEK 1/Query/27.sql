-- Numero di prodotti con una quantità disponibile inferiore alla media per categoria
SELECT Categoria, Count(NomeProdotto) NumeroProdotti
FROM buildweek1.prodotti_dataset
where QuantitaDisponibile < 
    (SELECT AVG(QuantitaDisponibile)
    FROM buildweek1.prodotti_dataset)
GROUP BY Categoria;
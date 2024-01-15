-- Calcola il totale delle vendite per ogni anno.
SELECT YEAR(DataTransazione) Anno, SUM(QuantitaAcquistata) TotaleAnnuale
FROM buildweek1.transazioni_dataset
GROUP BY YEAR(DataTransazione);
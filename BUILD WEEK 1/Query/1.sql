-- Trova il totale delle vendite per ogni mese
SELECT MONTH(DataTransazione) Mese, SUM(QuantitaAcquistata) QuantitaVendute
FROM buildweek1.transazioni_dataset
GROUP BY MONTH(DataTransazione)
ORDER BY MONTH(DataTransazione);
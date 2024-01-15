-- Calcola la variazione percentuale nelle vendite rispetto al mese precedente.
SELECT MONTH(DataTransazione) AS Mese, SUM(QuantitaAcquistata) AS TotVendMeseCorrente,
	SUM(QuantitaAcquistata)-LAG(SUM(QuantitaAcquistata),1,0) OVER (ORDER BY MONTH (DataTransazione)) AS Variazione,
    (SUM(QuantitaAcquistata)-LAG(SUM(QuantitaAcquistata), 1,0) OVER (ORDER BY MONTH(DataTransazione)))/LAG(SUM(QuantitaAcquistata), 1,0) OVER (ORDER BY MONTH(DataTransazione))*100 AS VariazionePercentuale
    FROM buildweek1.transazioni_dataset
    GROUP BY Mese
    ORDER BY Mese;
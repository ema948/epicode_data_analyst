-- Identifica il mese con il maggior importo totale delle vendite.
SELECT MONTH(DataTransazione) Mese, SUM(ImportoTotaleTransazione) MaggiorImporto
FROM buildweek1.transazioni_dataset
GROUP BY MONTH(DataTransazione)
ORDER BY SUM(ImportoTotaleTransazione) DESC LIMIT 1;
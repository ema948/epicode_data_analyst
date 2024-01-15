-- Calcola la percentuale di spedizioni con "Consegna Riuscita".
SELECT (COUNT(CASE WHEN StatusConsegna='Consegna Riuscita' THEN 1 END)/COUNT(*))*100 AS PercentualeConsegnaRiuscita
FROM buildweek1.spedizioni_dataset
WHERE IDTransazione<"501";
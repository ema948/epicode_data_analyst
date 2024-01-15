-- Trova la percentuale di spedizioni con "In Consegna" rispetto al totale.
SELECT (COUNT(CASE WHEN StatusConsegna='In Consegna' THEN 1 END)/COUNT(*))*100 AS PercentualeInConsegna
FROM buildweek1.spedizioni_dataset
WHERE IDTransazione<"501";


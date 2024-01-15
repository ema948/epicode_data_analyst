-- Trova il metodo di spedizione più utilizzato.
SELECT MetodoSpedizione, COUNT(MetodoSpedizione) AS Conteggio
FROM buildweek1.spedizioni_dataset
WHERE IDTransazione<"501"
GROUP BY MetodoSpedizione
ORDER BY COUNT(MetodoSpedizione) DESC LIMIT 1;
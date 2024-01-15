-- Calcola il numero medio di clienti registrati al mese.
SELECT ROUND (AVG (Conta.Conteggio)) AS NumeroMedio
FROM (SELECT MONTH(DataRegistrazione), COUNT(ClienteID) AS Conteggio
		FROM buildweek1.clienti_dataset
		GROUP BY MONTH(DataRegistrazione)) Conta;
-- Numero di clienti che non hanno effettuato transazioni
SELECT COUNT(Conteggio.NomeCliente) NumeroClientiSenzaTransazioni
FROM (SELECT c.NomeCliente
	FROM buildweek1.clienti_dataset c
	LEFT JOIN buildweek1.transazioni_dataset t ON c.ClienteID=t.ClienteID
	WHERE t.IDTransazione IS NULL) Conteggio;
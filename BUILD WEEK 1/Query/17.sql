-- Identifica i clienti che non hanno effettuato alcun acquisto.
SELECT c.NomeCliente
	FROM buildweek1.clienti_dataset c
	LEFT JOIN buildweek1.transazioni_dataset t ON c.ClienteID=t.ClienteID
	WHERE t.IDTransazione IS NULL;


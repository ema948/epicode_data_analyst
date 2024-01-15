-- Trova il cliente che ha effettuato il maggior numero di acquisti.
SELECT c.NomeCliente, COUNT(t.IDTransazione) NumeroTransazioni
FROM buildweek1.clienti_dataset c
INNER JOIN buildweek1.transazioni_dataset t ON c.ClienteID=t.ClienteID
GROUP BY c.NomeCliente
ORDER BY COUNT(t.IDTransazione) DESC LIMIT 2;

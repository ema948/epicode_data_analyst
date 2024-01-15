-- Clienti che hanno effettuato più di una transazione
SELECT c.NomeCliente, COUNT(t.IDTransazione) NTransazioni
FROM buildweek1.clienti_dataset c 
INNER JOIN buildweek1.transazioni_dataset t ON c.ClienteID=t.ClienteID
GROUP BY c.NomeCliente
HAVING COUNT(t.IDTransazione)>1;
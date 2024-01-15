-- Identifica il cliente con il maggior valore totale di acquisti.
SELECT c.NomeCliente, SUM(t.ImportoTotaleTransazione) ImportoSpeso, SUM(QuantitaAcquistata) QuantitaAcquistata, COUNT(IDTransazione) NumeroTransazioni
FROM buildweek1.clienti_dataset c
INNER JOIN buildweek1.transazioni_dataset t ON c.ClienteID=t.ClienteID
GROUP BY c.NomeCliente
ORDER BY SUM(t.ImportoTotaleTransazione) DESC LIMIT 1;
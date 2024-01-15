-- Per ogni cliente, elenca i prodotti acquistati e il totale speso.
SELECT c.NomeCliente, p.NomeProdotto, p.Categoria, t.ImportoTotaleTransazione
FROM buildweek1.clienti_dataset c
INNER JOIN buildweek1.transazioni_dataset t ON c.ClienteID=t.ClienteID
INNER JOIN buildweek1.prodotti_dataset p ON p.ProdottoID=t.ProdottoID
ORDER BY c.NomeCliente;
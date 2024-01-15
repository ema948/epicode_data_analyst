-- Tempo di preparazione del’ordine
SELECT AVG(datediff(DataSpedizione,DataTransazione)) as media,
        	MAX(datediff(DataSpedizione,DataTransazione)) as max,
        	MIN(datediff(DataSpedizione,DataTransazione)) as min
 FROM transazioni_dataset;

-- Media delle recensioni per categoria
SELECT p.Categoria, AVG(r.Rating)
FROM buildweek1.prodotti_dataset p 
INNER JOIN buildweek1.ratings_dataset r ON p.ProdottoID=r.ProductID
GROUP BY p.Categoria;
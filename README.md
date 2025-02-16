# ProbabilityAnalitics 🔎
Trabalho de Matemática aplicada a dados

<h1>
  Propósito
</h1>
<p>
  Fazer uma analise da base de orders para achar a probabilidade de recomendação de acordo com o carinho de um cliente
  (Usar Somente as colunas Order ID e Sub-Category para o dado da probabilidade)
</p>
<h1>
  Demandas
</h1>
<p>
Faça um programa que receba um dataset de N produtos e apresente a melhor combinação de recomendações para clientes. Para isso:
  
1. Defina o formato de inserção de dados (Padrões nas tabelas, nomes e etc.);
2. Apresente um relatório com as probabilidades de recomendação tendo em vista cada um dos produtos
(A, B, C ...) e cenários possíveis;
3. Considere os cenários possíveis:
1. Cliente sem produto no carrinho;
2. Cliente com 1 produto no carrinho;
3. Cliente com até N-1 produtos no carrinho;
4. Apresente a melhor escolha para cada um dos cenários;
</p>
<h1>
  Como foi feito
</h1>
<p>
  Primeiramente, lemos o .xlsx para manipularmos ele, removemos os dados duplicados que poderiam atrapalhar no calculo da probabilidade e transformamos em binario, ou seja, transformando as categorias em coluna e os id's em linhas, assim facilitando no calculo.
  Caso o carrinho esteja vazio, aparece o produto mais vendido, mas caso já exista um produto no carrinho, a tabela é filtrada, assim só mostrando os registros de id's que obrigatóriamente compraram aquela categoria. Após isso, pegamos as intersecções e vemos qual a maior para a proxima recomendação;
</p>
<h1>
  Data de entrega
</h1>
<p>
  20/02/2025
</p>

<h1>
  Participantes
</h1>
<p>
  Miguel Araujo de Sousa
  
  João Vitor Vargas
</p>

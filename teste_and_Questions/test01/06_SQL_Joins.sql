-- INNER JOIN - Selecionando todos os clientes com seus rescpectivos produtos
SELECT cliente.nome, pedido.produto
FROM cliente
INNER JOIN pedido
ON cliente.id = pedido.cliente_id;

-- LEFT JOIN - Selecionando todos os clientes mesmo se não tiver produtos
SELECT cliente.nome, pedido.produto
FROM cliente
LEFT JOIN pedido
ON cliente.id = pedido.cliente_id;

-- RIGHT JOIN - Selecionando todos os clientes mesmo se não tiver cliente (Ou não tenham sido pedidos por ninguém)
SELECT cliente.nome, pedido.produto
FROM cliente
LEFT JOIN pedido
ON cliente.id = pedido.cliente_id;

-- FULL OUTER JOIN - Selecionando todos os clientes mesmo se não tiver cliente (Ou não tenham sido pedidos por ninguém)
SELECT cliente.nome, pedido.produto
FROM cliente
LEFT JOIN pedido
ON cliente.id = pedido.cliente_id;
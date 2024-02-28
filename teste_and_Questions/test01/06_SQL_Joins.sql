-- INNER JOIN - Selecionando todos os clientes com seus rescpectivos Pedidos
SELECT cliente.nome, pedido.id
FROM cliente
INNER JOIN pedido
ON cliente.id = pedido.cliente_id;

-- LEFT JOIN - Selecionando todos os clientes mesmo se não tiver produtos
SELECT cliente.nome, pedido.id
FROM cliente
LEFT JOIN pedido
ON cliente.id = pedido.cliente_id;

-- RIGHT JOIN - Selecionando todos os Pedidos mesmo se não tiver cliente (Ou não tenham sido pedidos por ninguém)
SELECT cliente.nome, pedido.id
FROM cliente
RIGHT JOIN pedido
ON cliente.id = pedido.cliente_id;

-- FULL OUTER JOIN - Selecionando todos os clientes e pedidos mesmo se não tiver conrrespondência entre elas
SELECT cliente.nome, pedido.id
FROM cliente
FULL OUTER JOIN pedido
ON cliente.id = pedido.cliente_id;
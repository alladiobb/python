-- A table named prices contains prices for various items in inventory.
-- The table has columns named item_id, item_name, item_price and item_qty.
-- You need to find item names that have quantity of the item with an id of 10.
-- Which of the following queries is most suitable for this task?

SELECT item_name 
FROM prices 
WHERE item_qty > (SELECT item_qty FROM prices WHERE item_id = 10);

SELECT item_name 
FROM prices 
WHERE item_qty <> (SELECT item_qty FROM prices WHERE item_id = 10);

SELECT item_name 
FROM prices 
WHERE item_qty >= (SELECT item_qty FROM prices WHERE item_id = 10);
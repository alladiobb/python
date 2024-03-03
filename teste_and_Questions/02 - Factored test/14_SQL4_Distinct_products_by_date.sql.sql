-- You have a table named products_sold with columns named prod_id, prod_name, qty_sold and date_sold.
-- You need to report the number of distinct products sold by date.

-- Which of the following queries is the most suitable for this task?

SELECT date_sold, COUNT(qty_sold)
FROM products_sold
GROUP BY date_sold;

SELECT date_sold, AVG(qty_sold)
FROM products_sold
GROUP BY date_sold;

SELECT date_sold, COUNT(qty_sold)
FROM products_sold

SELECT date_sold, SUM(qty_sold)
FROM products_sold
GROUP BY date_sold;
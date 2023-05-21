CREATE TABLE items (
	item_id SERIAL PRIMARY KEY,
	item_name VARCHAR(100) NOT NULL,
	price SMALLINT NOT NULL DEFAULT 0
);

INSERT INTO items 
(item_name, price)
VALUES 
('Small desk', 100),
('Large desk', 300),
('Fan', 80)

CREATE TABLE customers (
	client_id SERIAL PRIMARY KEY,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL
);

INSERT INTO customers
(first_name, last_name)
VALUES 
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson')

SELECT * FROM ITEMS

SELECT * FROM ITEMS WHERE PRICE > 80

SELECT * FROM ITEMS WHERE PRICE < 300

SELECT * FROM CUSTOMERS WHERE LAST_NAME ILIKE 'SMITH'

SELECT * FROM CUSTOMERS WHERE LAST_NAME ILIKE 'JONES'

SELECT * FROM CUSTOMERS WHERE FIRST_NAME NOT ILIKE 'SCOTT'
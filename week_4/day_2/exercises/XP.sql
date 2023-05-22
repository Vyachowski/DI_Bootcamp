-- DATA FROM PREVIOUS LESSON AS A START POINT / SOLUTION IS BELOW

-- CREATE TABLE items (
-- 	item_id SERIAL PRIMARY KEY,
-- 	item_name VARCHAR(100) NOT NULL,
-- 	price SMALLINT NOT NULL DEFAULT 0
-- );

-- INSERT INTO items 
-- (item_name, price)
-- VALUES 
-- ('Small desk', 100),
-- ('Large desk', 300),
-- ('Fan', 80)

-- CREATE TABLE customers (
-- 	client_id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR(100) NOT NULL,
-- 	last_name VARCHAR(100) NOT NULL
-- );

-- INSERT INTO customers
-- (first_name, last_name)
-- VALUES 
-- ('Greg', 'Jones'),
-- ('Sandra', 'Jones'),
-- ('Scott', 'Scott'),
-- ('Trevor', 'Green'),
-- ('Melanie', 'Johnson')

-- OUTPUT

SELECT * FROM ITEMS

SELECT * FROM ITEMS ORDER by PRICE ASC

SELECT * FROM ITEMS WHERE PRICE <= 80 ORDER by PRICE DESC

SELECT FIRST_NAME, LAST_NAME  FROM CUSTOMERS ORDER BY FIRST_NAME ASC LIMIT 3

SELECT LAST_NAME  FROM CUSTOMERS ORDER BY LAST_NAME DESC
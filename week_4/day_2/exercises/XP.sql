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

-- PART II / Five lines are missing, still learning a topic/

SELECT * FROM customer;

SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM customer;

SELECT DISTINCT create_date FROM customer;

SELECT * FROM customer ORDER BY first_name DESC;

SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate;

SELECT address, phone FROM address WHERE district='Texas';

SELECT * FROM film WHERE film_id=15 OR film_id=150;

SELECT film_id, title, description, length, rental_rate FROM film WHERE title='Kiss Glory';

SELECT film_id, title, description, length, rental_rate FROM film WHERE title LIKE 'Ki%';


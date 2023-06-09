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

SELECT * FROM items

SELECT * FROM items ORDER by price ASC

SELECT * FROM items WHERE price <= 80 ORDER by price DESC

SELECT first_name, last_name  FROM customers ORDER BY first_name ASC LIMIT 3

SELECT last_name  FROM customers ORDER BY last_name DESC

-- PART II / Five lines are missing, still learning a topic/

-- In the dvdrental database write a query to select all the columns from the “customer” table.

SELECT * FROM customer

-- Write a query to display the names (first_name, last_name) using an alias named “full_name”.

SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM customer;

-- Lets get all the dates that accounts were created. Write a query to select all the create_date from the “customer” table (there should be no duplicates).

SELECT DISTINCT create_date FROM customer;

-- Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.

SELECT * FROM customer ORDER BY first_name DESC;

-- Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.

SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate;

-- Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.

SELECT address, phone FROM address WHERE district='Texas';

-- Write a query to retrieve all movie details where the movie id is either 15 or 150.

SELECT * FROM film WHERE film_id=15 OR film_id=150;

-- Write a query which should check if your favorite movie exists in the database. Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.

SELECT film_id, title, description, length, rental_rate FROM film WHERE title='samurai lion';

-- No luck finding your movie? Maybe you made a mistake spelling the name. Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.

SELECT film_id, title, description, length, rental_rate FROM film WHERE title ILIKE 'samurai%';

-- Write a query which will find the 10 cheapest movies.

SELECT * FROM film ORDER BY rental_rate ASC LIMIT 10

-- Not satisfied with the results. Write a query which will find the next 10 cheapest movies.

SELECT * FROM film ORDER BY rental_rate ASC LIMIT 10 OFFSET 10

-- Bonus: Try to not use LIMIT.

-- Write a query which will join the data in the customer table and the payment table. You want to get the first name and last name from the custtomer table, as well as the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).

SELECT customer.first_name, customer.last_name, payment.amount, payment.payment_date FROM customer JOIN payment ON customer.customer_id = payment.customer_id ORDER BY customer.customer_id

-- You need to check your inventory. Write a query to get all the movies which are not in inventory.

SELECT DISTINCT film.title
FROM film
LEFT JOIN inventory ON film.film_id = inventory.film_id

-- Write a query to find which city is in which country.

SELECT city.city, country.country
FROM city
JOIN country on city.country_id = country.country_id;


















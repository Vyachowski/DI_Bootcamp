CREATE DATABASE bootcamp;

CREATE TABLE students (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
  birth_date DATE NOT NULL
);

INSERT INTO items 
(first_name, last_name, birth_date)
VALUES 
('Marc', 'Benichou', '02/11/1998'),
('Yoan', 'Cohen', '03/12/2010'),
('Lea', 'Benichou', '27/07/1987'),
('Amelia', 'Dux', '07/04/1996'),
('David', 'Grez', '14/06/2003'),
('Omer', 'Simpson', '03/10/1980')
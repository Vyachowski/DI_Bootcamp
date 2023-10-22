-- Result of the output:
--    SELECT COUNT(*) 
--    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )
-- ANSWER: 0, because we can't have a null as a condition

-- Result of the output:
--    SELECT COUNT(*) 
--    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
-- ANSWER: 2, all values except null and 5

-- Result of the output:
--    SELECT COUNT(*) 
--    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
-- ANSWER: 2, same as previous

-- Result of the output:
--    SELECT COUNT(*) 
--    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
-- ANSWER: 2, same as previous

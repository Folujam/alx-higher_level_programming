-- 3 first students in the Batch ID=3
-- because Batch 3 is th best!
-- lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states
WHERE name = "California")
ORDER BY id;

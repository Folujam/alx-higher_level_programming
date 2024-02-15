-- 3 first students in the Batch ID=3
-- because Batch 3 is th best!
-- lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name FROM cities
INNER JOIN states ON cities.state_id=states.id
ORDER BY id;

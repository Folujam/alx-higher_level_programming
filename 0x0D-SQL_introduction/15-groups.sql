-- 3 first students in the Batch ID=3
-- because Batch 3 is th best!
--lists the number of records with the same score in th table st
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY score DESC;

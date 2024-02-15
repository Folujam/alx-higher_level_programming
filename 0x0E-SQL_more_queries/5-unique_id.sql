-- 3 first students in the Batch ID=3
-- because Batch 3 is th best!
--  creates the table unique_id on your MySQL serve
CREATE TABLE IF NOT EXISTS `unique_id` (`id` INT DEFAULT 1,	UNIQUE INDEX (id), `name` VARCHAR(256));

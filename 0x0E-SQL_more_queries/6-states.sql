-- 3 first students in the Batch ID=3
-- because Batch 3 is th best!
-- creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	`id` INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	`name` VARCHAR(256) NOT NULL);

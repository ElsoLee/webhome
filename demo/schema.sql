-- Copyright 2013 webhome
--
-- changhong contest
--

-- To create the database:
-- CREATE DATABASE webhome;
-- GRANT ALL PRIVILEGES ON webhome. * TO 'blog'@'localhost' IDENTIFIED BY 'webhome';
--
-- To reload the tables:
-- mysql --user=webhome --password=blog --database=blog < schema.sql

DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(100) NOT NULL UNIQUE,
	name VARCHAR(100) NOT NULL UNIQUE,
	password VARCHAR(100) NOT NULL
);

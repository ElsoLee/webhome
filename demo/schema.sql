-- Copyright 2013 webhome
--
-- changhong software contest
--

DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(100) NOT NULL UNIQUE,
	name VARCHAR(100) NOT NULL UNIQUE,
	password VARCHAR(100) NOT NULL
 );

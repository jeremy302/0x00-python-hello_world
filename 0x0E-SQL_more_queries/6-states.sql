-- creates a db and a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- switch to db
USE hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS states
(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL );

-- States table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Selecciona la base de datos que recién cree
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE PRIMARY KEY NOT NULL,
    name VARCHAR(256) NOT NULL
);
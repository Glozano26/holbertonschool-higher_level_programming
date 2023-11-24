-- Cities table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT UNIQUE PRIMARY KEY NOT NULL,
    state_id INT NOT NULL FOREIGN KEY(id),
    name VARCHAR(256)
)
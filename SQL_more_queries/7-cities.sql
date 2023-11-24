-- Cities table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT UNIQUE PRIMARY KEY NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
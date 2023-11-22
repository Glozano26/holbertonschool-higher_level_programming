-- Full creation
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score)
VALUES
    (1, 'Juan', 10),
    (2, 'Álex', 3),
    (3, 'Bob', 14),
    (4, 'Jorge', 8);
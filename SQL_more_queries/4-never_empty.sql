-- A script that creates the table id_not_null on your MySQL server
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL,
    name VARCHAR(256),
    score INT
);
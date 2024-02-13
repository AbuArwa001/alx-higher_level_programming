-- creates a table called second_table in the current database and set values
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT IGNORE  INTO second_table (id,name,score) values(1,"john", 10);
INSERT IGNORE  INTO second_table (id,name,score) values(2,"Alex", 3);
INSERT IGNORE  INTO second_table (id,name,score) values(3,"Bob", 14);
INSERT IGNORE  INTO second_table (id,name,score) values(4,"George", 8);

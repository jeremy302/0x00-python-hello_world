-- creates a table: `second_table`
-- creatse a new table
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
-- inserts records
INSERT INTO second_table (id, name, score) VALUE (1, "John", 10),
(2, "Alex", 3), (3, "Bob", 14), (4, "George", 8);

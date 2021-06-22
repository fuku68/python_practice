CREATE TABLE tb1(id VARCHAR(10), name VARCHAR(10),  age INTEGER);

INSERT INTO tb1 VALUES(‘A101’, ‘佐藤’, 40);

INSERT INTO tb1(id, name, age) VALUES(‘A102’, ‘鈴木’, 32);

SHOW variables LIKE '%time_zone%';


-- ALTER

ALTER TABLE tb1 MODIFY name VARCHAR(100);
ALTER TABLE tb1 ADD birthday DATETIME;

ALTER TABLE tb1 CHANGE birthday birthday_year INT;

ALTER TABLE tb1 DROP birthday_year;

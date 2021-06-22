-- primary key
CREATE TABLE itii(a INT PRIMARY KEY,b VARCHAR(10));
DESC itii;

INSERT INTO itii VALUES(1, 'あ');

-- uniq
CREATE TABLE uniq(a INT, b VARCHAR(10) UNIQUE);

-- auto increment
CREATE TABLE renzoku (a INT AUTO_INCREMENT PRIMARY KEY, b VARCHAR(10));
DESC renzoku;


ALTER TABLE renzoku AUTO_INCREMENT=1;

-- default
CREATE TABLE tblG(bang VARCHAR(10), name VARCHAR(10), tosi INT);

ALTER TABLE tblG MODIFY name VARCHAR(10) DEFAULT '氏名を入力';
DESC tblG;

-- copy
CREATE TABLE renzoku_cp1 SELECT * FROM renzoku

CREATE TABLE renzoku_cp2 LIKE renzoku;
INSERT INTO renzoku_cp2 SELECT FROM renzoku;

INSERT INTO renzoku_cp2(b) SELECT b FROM renzoku;

-- drop
DROP TABLE renzoku_cp1;
DROP TABLE IF EXISTS renzoku_cp1;

DELETE FROM renzoku_cp2;

-- select
CREATE TABLE tb(bang VARCHAR(10), uria INT, tuki INT);

INSERT INTO tb VALUES('A103', 101, 4),
  ('A102', 54, 5),
  ('A104', 181, 4),
  ('A101', 184, 4),
  ('A103', 17, 5),
  ('A101', 300, 5),
  ('A102', 205, 6),
  ('A104', 93, 5),
  ('A103', 12, 6),
  ('A107', 87, 6);

SELECT uria, bang FROM tb;

SELECT uria * 10000 as 売上 FROM tb;

SELECT AVG(uria) FROM tb;


-- func

SELECT PI();
SELECT VERSION();
SELECT DATABASE();
SELECT USER();
SELECT CHARSET('この文字');

--str 
SELECT CONCAT(id, name, 'さん') FROM tb1;

SELECT RIGHT(bang, 2) FROM tbl;
SELECT LEFT(bang, 2) FROM tbl;
SELECT SUBSTRING(bang, 2, 3) FROM tbl;
SELECT REPEAT ('.', age) FROM tbl;
SELECT REVERSE(nama) FROM tbl;

-- now
CREATE TABLE ima(a INT AUTO_INCREMENT PRIMARY KEY,  b DATETIME);
INSERT INTO ima (b) VALUES (NOW());
SELECT * FROM ima;




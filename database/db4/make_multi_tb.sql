DROP TABLE IF EXISTS tb1;
CREATE TABLE tb1(
  bang VARCHAR(20),
  name VARCHAR(20),
  tosi INT
);
INSERT INTO tb1 VALUES
  ('A101', '佐藤', 40),
  ('A102', '高橋', 28),
  ('A103', '中川', 20),
  ('A104', '渡辺', 23),
  ('A105', '西沢', 35);

DROP TABLE IF EXISTS tb2;
CREATE TABLE tb2(
  bang VARCHAR(20),
  name VARCHAR(20),
  tosi INT
);
INSERT INTO tb2 VALUES
  ('A106', '中村', 26),
  ('A107', '田中', 24),
  ('A108', '鈴木', 23),
  ('A109', '村井', 25),
  ('A110', '吉田', 27);

DROP TABLE IF EXISTS tb3;
CREATE TABLE tb3(
  bang VARCHAR(20),
  ken  VARCHAR(20)
);
INSERT INTO tb3 VALUES
  ('A101', '東京都'),
  ('A102', '埼玉県'),
  ('A103', '神奈川県'),
  ('A104', '北海道'),
  ('A105', '静岡県');

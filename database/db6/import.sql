-- import
mysql -h mysql -u root -p DB --local-infile=1

SELECT @@global.secure_file_priv;
LOAD DATA LOCAL INFILE '/import.csv' INTO TABLE tb1 FIELDS TERMINATED BY ',';

SELECT * INTO OUTFILE '/tmp/out.csv' FROM tb1;

SOURCE /exec.sql

mysql -h mysql -u root -p test3 -e 'SELECT * FROM tb;'

-- redirect
mysql -h mysql -u root -p DB --proot > log.txt

-- tee
tee log3.txt
notee


-- dump
mysqldump -h mysql -u root -p --skip-column-statistics

 mysql -h mysql -u root -p < dump.sql

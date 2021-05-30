#!/bin/bash


sudo docker exec -it postgres_a psql -U postgres -c "create database database_a"
sudo docker exec -it postgres_b psql -U postgres -c "create database database_b"


git clone https://github.com/gregrahn/tpch-kit
sudo docker cp ./tpch-kit/dbgen/dss.ddl postgres_a:/dss.dll
sudo docker exec -it postgres_a psql -U postgres database_a -f dss.dll
sudo docker cp ./tpch-kit/dbgen/dss.ddl postgres_b:/dss.dll
sudo docker exec -it postgres_b psql -U postgres database_b -f dss.dll


sudo make -C ./tpch-kit/dbgen MACHINE=LINUX DATABASE=POSTGRESQL
cd ./tpch-kit/dbgen
./dbgen -vf -s 1


sudo docker cp ./customer.tbl postgres_a:/customer.tbl
sudo docker cp ./lineitem.tbl postgres_a:/lineitem.tbl
sudo docker cp ./nation.tbl postgres_a:/nation.tbl
sudo docker cp ./orders.tbl postgres_a:/orders.tbl
sudo docker cp ./part.tbl postgres_a:/part.tbl
sudo docker cp ./partsupp.tbl postgres_a:/partsupp.tbl
sudo docker cp ./region.tbl postgres_a:/region.tbl
sudo docker cp ./supplier.tbl postgres_a:/supplier.tbl


sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy customer FROM PROGRAM 'head -10000 /customer.tbl' CSV DELIMITER '|'"
sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy lineitem FROM PROGRAM 'head -10000 /lineitem.tbl' CSV DELIMITER '|'"
sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy nation FROM PROGRAM 'head -10000 /nation.tbl' CSV DELIMITER '|'"
sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy orders FROM program 'head -10000 /orders.tbl' CSV DELIMITER '|'"
sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy part FROM PROGRAM 'head -10000 /part.tbl' CSV DELIMITER '|'"
sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy partsupp FROM PROGRAM 'head -10000 /partsupp.tbl' CSV DELIMITER '|'"
sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy region FROM PROGRAM 'head -10000 /region.tbl' CSV DELIMITER '|'"
sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy supplier FROM PROGRAm 'head -10000 /supplier.tbl' CSV DELIMITER '|'"


sudo docker exec -it postgres_b psql -U postgres database_b -c "ALTER TABLE customer ADD COLUMN launch_id int;"
sudo docker exec -it postgres_b psql -U postgres database_b -c "ALTER TABLE customer ADD COLUMN effective_dttm date DEFAULT now();"

sudo docker exec -it postgres_b psql -U postgres database_b -c "ALTER TABLE lineitem ADD COLUMN launch_id int;"
sudo docker exec -it postgres_b psql -U postgres database_b -c "ALTER TABLE lineitem ADD COLUMN effective_dttm date DEFAULT now();"

sudo docker exec -it postgres_b psql -U postgres database_b -c "ALTER TABLE nation ADD COLUMN launch_id int;"
sudo docker exec -it postgres_b psql -U postgres database_b -c "ALTER TABLE nation ADD COLUMN effective_dttm date DEFAULT now();"

sudo docker exec -it postgres_b psql -U postgres database_b -c "ALTER TABLE orders ADD COLUMN launch_id int;"
sudo docker exec -it postgres_b psql -U postgres database_b -c "ALTER TABLE orders ADD COLUMN effective_dttm date DEFAULT now();"

sudo docker exec -it postgres_b psql -U postgres database_b -c "ALTER TABLE part ADD COLUMN launch_id int;"
sudo docker exec -it postgres_b psql -U postgres database_b -c "ALTER TABLE part ADD COLUMN effective_dttm date DEFAULT now();"

sudo docker exec -it postgres_b psql -U postgres database_b -c "ALTER TABLE partsupp ADD COLUMN launch_id int;"
sudo docker exec -it postgres_b psql -U postgres database_b -c "ALTER TABLE partsupp ADD COLUMN effective_dttm date DEFAULT now();"

sudo docker exec -it postgres_b psql -U postgres database_b -c "ALTER TABLE region ADD COLUMN launch_id int;"
sudo docker exec -it postgres_b psql -U postgres database_b -c "ALTER TABLE region ADD COLUMN effective_dttm date DEFAULT now();"

sudo docker exec -it postgres_b psql -U postgres database_b -c "ALTER TABLE supplier ADD COLUMN launch_id int;"
sudo docker exec -it postgres_b psql -U postgres database_b -c "ALTER TABLE supplier ADD COLUMN effective_dttm date DEFAULT now();"

sudo docker exec -it postgres_b psql -U postgres database_b -c """
create table statistic (
       table_name     text
     , column_name    text
     , cnt_nulls      int
     , cnt_all        int
     , load_date      date
)
"""

sudo docker exec -it postgres_b psql -U postgres database_b -c """
create table log (
       source_launch_id    int
     , target_schema       text
     , target_table        text  
     , target_launch_id    int
     , processed_dttm      timestamp default now()
     , row_count           int
     , duration            interval
     , load_date           date
)
"""

cd ..
cd ..


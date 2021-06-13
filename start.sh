#!/bin/bash

# go to dbgendir
cd ./tpch-kit/dbgen

# copy initial table gen script to container
sudo docker cp ./dss.ddl postgres_a:/dss.dll

# cope data generation script to container
sudo docker cp ./customer.tbl postgres_a:/customer.tbl
sudo docker cp ./lineitem.tbl postgres_a:/lineitem.tbl
sudo docker cp ./nation.tbl postgres_a:/nation.tbl
sudo docker cp ./orders.tbl postgres_a:/orders.tbl
sudo docker cp ./part.tbl postgres_a:/part.tbl
sudo docker cp ./partsupp.tbl postgres_a:/partsupp.tbl
sudo docker cp ./region.tbl postgres_a:/region.tbl
sudo docker cp ./supplier.tbl postgres_a:/supplier.tbl


# return to starting dir
cd ..
cd ..

# create requiered databases
sudo docker exec -it postgres_a psql -U postgres -c "create database database_a"
sudo docker exec -it postgres_b psql -U postgres -c "create database database_b"
sudo docker exec -it postgres_c psql -U postgres -c "create database database_c"

# create initial tables in postgres_a
sudo docker exec -it postgres_a psql -U postgres database_a -f dss.dll

# fill those tables
sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy customer FROM PROGRAM 'head -10000 /customer.tbl' CSV DELIMITER '|'"
sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy lineitem FROM PROGRAM 'head -10000 /lineitem.tbl' CSV DELIMITER '|'"
sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy nation FROM PROGRAM 'head -10000 /nation.tbl' CSV DELIMITER '|'"
sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy orders FROM program 'head -10000 /orders.tbl' CSV DELIMITER '|'"
sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy part FROM PROGRAM 'head -10000 /part.tbl' CSV DELIMITER '|'"
sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy partsupp FROM PROGRAM 'head -10000 /partsupp.tbl' CSV DELIMITER '|'"
sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy region FROM PROGRAM 'head -10000 /region.tbl' CSV DELIMITER '|'"
sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy supplier FROM PROGRAm 'head -10000 /supplier.tbl' CSV DELIMITER '|'"

# run script creating schemas and tables for postgres_b and _c
python3 create_tables.py

# start scheduler
# sudo docker exec airflow airflow scheduler
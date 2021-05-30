#!/bin/bash


sudo docker exec -it postgres_b psql -U postgres -c 'SELECT pg_terminate_backend(pid) FROM pg_stat_activity;'

sudo docker exec -it postgres_b psql -U postgres -c 'drop database database_b'

sudo docker exec -it postgres_b psql -U postgres -c "create database database_b"

sudo docker exec -it postgres_b psql -U postgres database_b -f dss.dll

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

sudo docker exec -it postgres_b psql -U postgres database_b -c "ALTER TABLE supplier ADD COLUMN launch_id int ;"
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
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


sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy customer FROM '/customer.tbl' CSV DELIMITER '|'"
sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy lineitem FROM '/lineitem.tbl' CSV DELIMITER '|'"
sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy nation FROM '/nation.tbl' CSV DELIMITER '|'"
sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy orders FROM '/orders.tbl' CSV DELIMITER '|'"
sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy part FROM '/part.tbl' CSV DELIMITER '|'"
sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy partsupp FROM '/partsupp.tbl' CSV DELIMITER '|'"
sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy region FROM '/region.tbl' CSV DELIMITER '|'"
sudo docker exec -it postgres_a psql -U postgres database_a -c "\copy supplier FROM '/supplier.tbl' CSV DELIMITER '|'"


cd ..
cd ..


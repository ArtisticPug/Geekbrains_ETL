#!/bin/bash

# update/upgrade/install dependencies
sudo apt update -y
sudo apt upgrade -y
sudo apt install docker docker-compose python3-pip -y
pip install psycopg2-binary pandas apache-airflow great_expectations sqlalchemy

# clone dbgen repo
git clone https://github.com/gregrahn/tpch-kit

# start compose
sudo docker-compose up -d

# generate data
sudo make -C ./tpch-kit/dbgen MACHINE=LINUX DATABASE=POSTGRESQL
cd ./tpch-kit/dbgen
./dbgen -vf -s 1

# return to starting dir
cd ..
cd ..
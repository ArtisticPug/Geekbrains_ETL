#!/bin/bash


sudo apt update -y
sudo apt upgrade -y
sudo apt install docker docker-compose python3-pip -y
pip install psycopg2-binary pandas


sudo docker-compose up -d

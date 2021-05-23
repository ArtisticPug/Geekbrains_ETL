#!/bin/bash


sudo docker exec -it postgres_a psql -U postgres -c 'SELECT pg_terminate_backend(pid) FROM pg_stat_activity;'
sudo docker exec -it postgres_a psql -U postgres -c 'drop database database_a'
sudo docker exec -it postgres_b psql -U postgres -c 'SELECT pg_terminate_backend(pid) FROM pg_stat_activity;'
sudo docker exec -it postgres_b psql -U postgres -c 'drop database database_b'


sudo docker-compose down


sudo rm -R tpch-kit

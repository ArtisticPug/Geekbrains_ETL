#!/bin/bash

# drop databases from postgres_a container
sudo docker exec -it postgres_a psql -U postgres -c 'SELECT pg_terminate_backend(pid) FROM pg_stat_activity;'
sudo docker exec -it postgres_a psql -U postgres -c 'drop database database_a'

# drop databases from postgres_b container
sudo docker exec -it postgres_b psql -U postgres -c 'SELECT pg_terminate_backend(pid) FROM pg_stat_activity;'
sudo docker exec -it postgres_b psql -U postgres -c 'drop database database_b'

# drop databases from postgres_c container
sudo docker exec -it postgres_c psql -U postgres -c 'SELECT pg_terminate_backend(pid) FROM pg_stat_activity;'
sudo docker exec -it postgres_c psql -U postgres -c 'drop database database_c'

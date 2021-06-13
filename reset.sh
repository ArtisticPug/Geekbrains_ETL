#!/bin/bash

# delete downloaded dbgen
sudo rm -R tpch-kit

# remove docker-compose containers
sudo docker-compose down
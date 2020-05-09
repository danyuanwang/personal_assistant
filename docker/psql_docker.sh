#!/bin/bash
default_docker_name=docker_postgres_1
sudo docker ps | grep $default_docker_name
echo docker container name: [$default_docker_name]
read docker_name
if test -z $docker_name
then 
docker_name=$default_docker_name
fi
sudo docker exec -it $docker_name psql -h localhost -p 5432 -d personal_assistant_db -U personal_assistant_db_admin -W

# psql -h localhost -p 5433 -d personal_assistant_db -U personal_assistant_db_admin -W

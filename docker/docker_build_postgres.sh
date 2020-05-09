#!/bin/bash
if test -e Dockerfile_postgres
then
   pushd ../
fi
sudo docker volume rm postgresvolume
sudo docker build -f docker/Dockerfile_postgres . -t danyuanwang/xuanwugame:postgres

popd

#!/bin/bash
if test -e Dockerfile_assistant
then
   pushd ../
fi
cp config.yml docker/
cp endpoints.yml docker/
cp domain.yml docker/
cp credentials.yml docker/
sed -i 's/localhost:8000/duckling:8000/g' docker/config.yml
sed -i 's/localhost:5055/action:5055/g' docker/endpoints.yml
rm models/*
rasa train -c docker/config.yml -vv --debug
sudo docker build -f docker/Dockerfile_assistant . -t danyuanwang/xuanwugame:assistant

rm docker/config.yml
rm docker/endpoints.yml
rm docker/domain.yml
rm docker/credentials.yml

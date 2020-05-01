#!/bin/bash
sudo docker-compose build
sudo docker-compose -f docker-compose.yml -f docker-compose-production.yml up -d

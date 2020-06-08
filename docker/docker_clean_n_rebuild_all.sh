#!/bin/bash
source docker_clean.sh
source docker_build_rasa_full.sh  
source docker_build_assistant.sh 
source docker_build_action.sh
source docker_build_postgres.sh 


#!/bin/bash

docker stop $(docker ps -qa)
docker rm $(docker ps -qa)
docker rmi -f $(docker images | tail -n+2 | awk '{print $3}')
docker volume rm $(docker volume ls | tail -n+2 | awk '{print $2}')
docker network rm $(docker network ls | tail -n+2 | awk '{print $1,$2}' | grep -v bridge | grep -v host | grep -v none | cut -d' ' -f1)

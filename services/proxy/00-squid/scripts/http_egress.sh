#!/bin/bash
source ./bin/activate

container="$1"

if [[ $(container_exists $container) -eq 1 || $(container_exists squid) -eq 1 ]]
then
  docker network create http_egress_${container}
  docker network connect http_egress_${container} ${container} squid
fi


#!/bin/bash
source ./bin/activate

container="$1"
hostname="$2"
port="$3"

if [[ $(container_exists $container) -eq 1 && $(container_exists nginx) -eq 1 ]]
then
  docker network create http_ingress_${container}
  docker network connect http_ingress_${container} ${container} nginx
fi

cat >${VOLUMES}/nginx/_data/conf.d/${hostname}.conf <<EOF
location / {
  proxy_pass http://${container}:${port};
  proxy_set_header Host \$host;
  proxy_set_header X-Real-IP \$remote_addr;
}
EOF

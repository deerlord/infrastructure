#!/bin/bash

source ./bin/activate

container="${1}"
if [ -z ${2} ]
then
  port="${2}"
else
  port="8080"
fi
network="${container}_http_ingress"

if [[ $(docker network ls | awk '{print $2}' | grep -c $network) -eq 0 ]]
then
  docker network create $network --internal
fi

if [[ $(container_exists nginx) -eq 1 && $(container_exists $container) -eq 1 ]]
then
  conf="${VOLUMES}/nginx/_data/conf.d/${container}.conf"
  cat > $conf <<'EOF'
server {
  listen 443 ssl;
  server_name ${container}.${HOST_DOMAIN};
  location / {
    proxy_pass http://${container}:${port}/;
    proxy_set_header Host \$host;
    proxy_set_header X-Real-IP \$remote_addr;
    proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto \$scheme;
    proxy_set_header Request-URI \$request_uri;
  }
}
EOF
  chown nginx $conf
  docker network connect $network $container
  docker network connect $network nginx
  docker restart nginx
fi

#!/bin/bash

set -euo pipefail

if [[ ! -f ./CONFIG ]]
then
  echo 'No CONFIG file found,'
  echo '$ cp CONFIG.sample CONFIG'
  echo 'then edit it accordingly.'
  exit 1
fi
source ./CONFIG

apt update -y
apt upgrade -y
apt install -y docker.io
systemctl start docker
systemctl enable docker

docker network create --subnet=${EGRESS_SUBNET} egress

# firewall rules
#/usr/sbin/iptables -A INPUT -p icmp --icmp-type echo-request -j REJECT

build_exclude_sphinx() {
  for image in $(ls ./containers/build | grep -v 61-sphinx)
  do
    ./containers/build/${image}
  done
}

full_openhab() {
  ./containers/build/00-squid
  ./containers/build/50-nginx
  ./containers/build/60-openhab
}

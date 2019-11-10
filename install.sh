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

docker network create --subnet=172.20.0.0/24 egress

# firewall rules
#/usr/sbin/iptables -A INPUT -p icmp --icmp-type echo-request -j REJECT

build_all() {
  for image in $(ls ./containers/build)
  do
    ./containers/build/${image}
  done
}

build_all

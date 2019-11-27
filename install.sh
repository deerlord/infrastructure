#!/bin/bash

set -euo pipefail

if [[ ! -f ./conf.d/CONFIG ]]
then
  echo 'No CONFIG file found,'
  echo '$ cp ./conf.d/CONFIG{.sample,}'
  echo 'then edit it accordingly.'
  exit 1
fi

source ./bin/activate

apt update -y
apt upgrade -y
apt install -y docker.io
systemctl start docker
systemctl enable docker

# firewall rules
#/usr/sbin/iptables -A INPUT -p icmp --icmp-type echo-request -j REJECT


blackhole_testing() {
  ./containers/00-dnsmasq/build
  ./containers/00-dnsmasq/create
  ./containers/01-ntpd/build
  ./containers/01-ntpd/create
  ./containers/10-squid/build
  ./containers/10-squid/create
  ./containers/11-nginx/build
  ./containers/11-nginx/create
  ./containers/20-openhab/build
  ./containers/20-openhab/create
}

all() {
  for image in $(ls ./containers/)
  do
    containers/$image/build
    containers/$image/create
  done
}

blackhole_testing

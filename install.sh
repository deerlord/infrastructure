#!/bin/bash

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

build_all() {
  for image in $(ls ./containers/*/build)
  do
    $image
  done
}

create_all() {
  for image in $(ls ./containers/*/create)
  do
    $image
  done
}

build_all
create_all

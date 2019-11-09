#!/bin/bash

source ./CONFIG

apt update -y
apt upgrade -y
apt install -y docker.io
systemctl start docker
systemctl enable docker

# firewall rules
#/usr/sbin/iptables -A INPUT -p icmp --icmp-type echo-request -j REJECT

build_all() {
  for image in $(ls ./containers/build)
  do
    ./containers/build/${image}
  done
}

build_all

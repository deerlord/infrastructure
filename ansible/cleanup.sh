#!/bin/bash

docker stop dnsmasq
docker rm dnsmasq
docker rmi dnsmasq
docker stop ntpd
docker rm ntpd
docker rmi ntpd
docker stop squid
docker rm squid
docker rmi squid

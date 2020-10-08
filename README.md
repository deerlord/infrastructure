### NETWORKING SERVICES ON SMALL MACHINES

This repository aims to provide a centralized networking resource. These services are run in Docker containers and each shares a similar file structure to prepare, create, and deploy the service in a container. Currently these services include:
- dhcp and dns; dhcp provided by dnsmasq. dns provided by dnsmasq for dhcp clients, stubby upstream for DNS over TLS.
- ntpd; a local time daemon for keeping your network in sync

Future services:
- ???

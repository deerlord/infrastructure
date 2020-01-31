#!/bin/bash

apt install -y install --no-install-recommends qemu-kvm libvirt-clients libvirt-daemon-system
useradd minikube -m -s /bin/bash
adduser minikube libvirt
echo "export LIBVIRT_DEFAULT_URI='qemu:///system'" > ~minikube/.profile
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
chmod +x minikube
mkdir -p /usr/local/bin/
install minikube /usr/local/bin/

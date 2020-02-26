# CURRENTLY BEING ANSIBLE-IZED

## dnsmasq

Notes:
Docker typically needs `--cap-add=NET_ADMIN` to run a dnsmasq container. However, this seems to work in ansible without explicitly declaring this option. The TCP ports are accessible on the host OS, however this container has not been tested in production to confirm it truly works. If `NET_ADMIN is required, you should be able to add this with `capabilities: NET_ADMIN` in the docker/dnsmasq/main.yml file.


## dnsmasq

Notes:
Docker typically needs `--cap-add=NET_ADMIN` to run a dnsmasq container. However, this seems to work in ansible without explicitly declaring this option. The TCP ports are accessible on the host OS, however this container has not been tested in production to confirm it truly works. If `NET_ADMIN` is required, you should be able to add this with `capabilities: NET_ADMIN` in the docker/dnsmasq/main.yml file.

```
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                                                        NAMES
3c7363161a71        dnsmasq             "/usr/sbin/dnsmasq -k"   About a minute ago   Up 56 seconds       0.0.0.0:53->53/udp, 0.0.0.0:53->53/tcp, 0.0.0.0:67->67/udp   dnsmasq
```

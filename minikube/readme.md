run `setup.sh`. You can edit `.minikube/config/config.json` to set parameters for the VM.

To disable libvirt's built in dhcp/dns servers
```
$ virsh
virsh # net-destroy default
virsh # net-edit default
>>> remove dhcp option, add: <dns enabled='no'/>
virsh # net-start default
```

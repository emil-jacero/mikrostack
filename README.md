# mikrostack

**THIS PROJECT IS AN EXPERIMENT**

**THIS PROJECT IS A PLAYGROUND FOR MY CRAZY IDEAS :)**


## The Project Scope
The scope is simple yet complex. First of all it needs to accomplish the basics.

Mikrostack is for the serious homelab nerd. It takes inspiration from the OpenStack projects, and tries to consolidate and simplify the good ideas.


### The Basics
Provide a compute resource, in this case using KVM. Tie in networking in the form of simple network bridges and interfaces in libvirt.
Provide storage in the form plain QCOW2 on local/central storage (initially). Provide all these while being able to scale up and down.

### The complex
#### Master
It's main functionality is to keep track of the whole infrastructure to be able to quickly give the user a response to a request while still know what to do with that request afterwards.
Basically, the master knows everything and therefore can tell in advance if a request is going to work or not. 

The idea is for the master to keep track of everything from network (subnets, vlans, ipam, etc), storage (storage utilization and location, etc) and compute (memory and cpu utilization, etc)

The system relies on a master node (single node for now). A API is served from the master. The frontend is served separately but utilizes the API.
The master node acts as an orchestrator pushing instructions into a queue that the agents subscribe to and act on.
Because everything that is tightly related to the virtual machine is done on the compute node all this work is pushed to the agent and therefore leaving the orchestration to the master.

**Note:** The master can be installed on one of the compute nodes.

#### Agent
Because the focus of this project is only to provide you (the consumer) with virtual machines (and everything that a virtual machine need), the agent will handle a lot of the quality of life stuff that the virtual machines need.
For example, the agent will provide a simple web server serving cloud-init with what it needs. Yes that is right, mikrostack will support cloud-init.

It will also handle the network setup for each virtual machine. It will be accomplished by controlling the compute node's physical connection and the virtual interfaces.
First implementation will be using VLAN.

The storage will be handled by the agent as well. It can utilize local storage or central storage over NFS.
When using local storage the live migration becomes much slower as it will have to migrate all the disks of the virtual machine.


## Features
#### Compute
- [ ] Instance create / modify / delete (KVM)
- [ ] Instance snapshot
- [ ] Instance groups
- [ ] Instance group snapshot
- [ ] Cloud-init - Initially provided by configdrive (presenting an ISO with the json blob to the virtual machine)
- [ ] Support for cloud images using cloud-init
- [ ] SSH keys management (RSA & ed25519)
- [ ] Live migration / Cold migration
- [ ] Images - à la Glance :)

#### Storage
- [ ] Volume create / modify / delete (Local & NFS)
- [ ] Volume snapshot
- [ ] Volume groups
- [ ] Volume group snapshot
- [ ] Storage migration

#### Network
- [ ] Bridged network create / modify / delete (Linux Bridge)


## Dependencies
- MAAS (Metal As A Service) - Utilized for full control of the different nodes.
- JuJu - Used for mikrostack deployment


## Future
**Future OVN / OVS**
- [ ] IPAM
- [ ] Builtin DHCP
- [ ] Builtin L3 Router
- [ ] cloud-init web provider. Serve the instance with cloud-init data from a central webservice

**Future Ceph**
- [ ] 

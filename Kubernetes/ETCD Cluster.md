# ETCD Cluster
<span style = "color:lightblue">ETCD</span> is a distributed, reliable key-value storage store that keeps information about the nodes.
> [!INFO]
> Tabular or relational databases store entries in a tabular format, where all entries have the same attributes, while each entry in key-value databases have one or more key-value pairs.

Key-value databases are great for storing configuration settings.

## Installation
The following steps explain how to install ETCD.
1. Download binaries. The code block below downloads the `${ETCD_VER}` version of ETCD.
   ```bash
   curl -L https://github.com/etcd-io/etcd/releases/download/${ETCD_VER}/etcd-${ETCD_VER}-linux-amd64.tar.gz -o etcd-${ETCD_VER}-linux-amd64.tar.gz
	```
2. Extract the zip file.
   ```bash
   tar xzvf etcd-v3.3.11-linux-amd64.tar.gz
	```
1. Verify installation.
   ```bash
   ./etcd --version
   ./etcdctl version
	```

## Basic Commands
When ETCD is run, it listens on port `2379` by default and can store key-value information.
- `./etcd`: run service
- `./etcdctl`: command line interface
- `./etcdctl set key1 value1`: store `key1` with `value1` in the database

## Kubernetes Integration
ETCD stores the following information about the cluster.
- Nodes
- PODs
- Configs
- Secrets
- Accounts
- Roles
- Bindings
- *and other information*

Modifications to the ETCD server will cause changes to the cluster. ETCD will run as a service that is part of the Kubernetes cluster.

ETCD can be set up <span style = "color:lightblue">manually</span> or using the `kubeadm` command.
- manually: must configure ETCD to the correct IP (*correspond with kube-apiserver*)
- `kubeadm`:  service is run as a pod

Multiple ETCD instances can be created as found in a <span style = "color:lightblue">high avalability (HA) environment</span>.

## Commands
`etcdctl` is the command line interface (CLI) tool used to interact with ETCD.

> [!INFO]
> Run `kubectl get pods -n kube-system` to list pods.
> 
> Run `kubectl exec etcd-master -n kube-system` and `etcdctl get / --prefix -keys-only` to get a list of keys stored in ETCD.


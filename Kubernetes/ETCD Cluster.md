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

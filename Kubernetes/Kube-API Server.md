# Kube-API Server
It allows communication in between nodes and components and from outside requests.

The `kubectl` command is sent to the API server which then **performs** the necessary functions and **relays** the command to required nodes and/or components. 

Alternatively, a `POST` request can be sent to the API server to perform the same command.
1. Authenticate user.
2. Validate request.
3. Retrieve data.
4. Update ETCD.

The cluster's kube-scheduler and nodes' kublets rely on the API server to update and manage the ETCD cluster.

## Installation
The kube-api server can be installed, run, and configured as a binary file.
```bash
wget https://storage.googleapis.com/kubernetes-release/release/v1.13.0/bin/linux/amd64/kube-apiserver
```

The server's options can be located using the following commands for a kube admin and non-kube admin setup respectively.

```bash
cat /etc/kubernetes/manifests/kube-apiserver.yaml
```

```bash
cat /etc/systemd/system/kube-apiserver.service
```

Run the following to list the processes to see the options as well.

```bash
ps -aux | grep kube-apiserver
```


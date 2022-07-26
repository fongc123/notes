# Kube Proxy
A kube proxy allows communication between pods to form a <span style = "color:lightblue">pod network</span>. When a new service is created, it forwards traffic heading to a service (*of a pod*) to the backend pods (*which contain those services*).

An <span style = "color:lightblue">IP table rule</span> is created to configure pod networking.

## Installation
```bash
wget https://storage.googleapis.com/kubernetes-release/release/v1.13.0/bin/linux/amd64/kube-proxy
```

`kube-proxy.service`

Kube Admin deploys kube proxies as a pod on each node as a <span style = "color:lightblue">daemonset</span>. 
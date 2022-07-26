# Kublet
A kublet controls all activities on a node and communicates with the master node through the Kube API server.
- register node
- create pods
- monitor node and pods

## Installation
Kube admin (`kubeadm`) does not deploy kubelets. **A kubelet must be manually installed on the worker nodes by installing the kublet and running it as a service.** The service can be viewed by listing the processes.

```bash
ps -aux | grep kubelet
```


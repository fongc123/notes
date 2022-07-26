# Scheduler
It is responsible for deciding which pod is assigned to which node; however, it is the kublet on each node that *actually* creates a pod on its node.

Each pod has a set of resource requirements (i.e., CPU and memory), and each node has different specifications. To decide which node a pod must be scheduled on, the scheduler goes through the following steps.
1. Filter nodes that do not match a pod's requirements.
2. Assign a score to each node. [^1]

There are also other requirements.
- taints and tolerations
- node selectors & affinity

## Installation
The kube-scheduler can be installed using the following command.

```bash
wget https://storage.googleapis.com/kubernetes-release/release/v1.13.0/bin/linux/amd64/kube-scheduler
```

In a kube admin setup, the scheduler will be run as a pod. Its options can be shown using the following command.

```bash
cat /etc/kubernetes/manifests/kube-scheduler.yaml
```

In a non-kube admin setup, the service's options can be shown using the following command.

```bash
cat /etc/systemd/system/kube-scheduler.service
```

Run the following to list the processes to see the options as well.

```bash
ps -aux | grep kube-scheduler
```


[^1]: How much resources would the node have left after the pod is assigned?
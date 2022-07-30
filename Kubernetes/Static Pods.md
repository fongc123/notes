# Static Pods
A <span style = "color:lightblue">static pod</span> is a pod that is manually run on a node. The kubelet will occassionally check the `/etc/Kubernetes/manifests` path in a node for new pod definitions even without a master node or scheduling components. Pod definition files placed in this path will be automatically create

Replica sets or deployments cannot be created with this method.
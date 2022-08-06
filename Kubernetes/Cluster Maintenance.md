# Cluster Maintenance
Cluster maintenance covers the upgrade, backup, and restore process of the components in a Kubernetes cluster (*not the applications*).

The <span style = "color:lightblue">pod eviction timeout</span> is the amount of time until a pod is considered offline. It can be set by the controller manager and is set to **5 minutes by default**.

Pods that were originally assigned to an offline node but were part of a replica set will be assigned to other available nodes. However, pods that were not part of a replica set will be lost.

## OS Upgrades

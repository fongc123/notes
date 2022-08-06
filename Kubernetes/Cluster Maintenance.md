# Cluster Maintenance
Cluster maintenance covers the upgrade, backup, and restore process of the components in a Kubernetes cluster (*not the applications*).

## OS Upgrades
When operating system upgrades are required on a node, it may be rebooted, causing it to be offline on the Kubernetes cluster.

The <span style = "color:lightblue">pod eviction timeout</span> is the amount of time until a pod is considered offline. It can be set by the controller manager and is set to **5 minutes by default**.

Pods that were originally assigned to an offline node but were part of a replica set will be assigned to other available nodes. However, pods that were not part of a replica set will be lost.

When the node is online again, it will be in a "blank state" (i.e., no scheduled nodes) and will be unschedulable. The original pods on the node prior to rebooting will not be rescheduled.

```bash
kubectl drain <NODE_NAME>
```

The `drain` command will terminate all pods running on a node, so that they can be scheduled on other nodes.

The `--ignore-daemonsets` will ignore daemonsets, as they cannot be evicted from a node. The `--force` can be used to forcefully evict pods **that are not part of a replica set** from the node (*the pod will be deleted permanently*).

```bash
kubectl cordon <NODE_NAME>
```

```bash
kubectl uncordon <NODE_NAME>
```

The `cordon` and `uncordon` commands will restrict and allow scheduling of pods on a node respectively.

> [!INFO]
> The `uncordon` command will not terminate running pods.

## Kubernetes Software Versions

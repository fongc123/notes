# Cluster Maintenance
Cluster maintenance covers the upgrade, backup, and restore process of the components in a Kubernetes cluster (*not the applications*).

## OS Upgrades
^OSUPGRADES

When operating system upgrades are required on a node, it may be rebooted, causing it to be offline on the Kubernetes cluster.

The <span style = "color:lightblue">pod eviction timeout</span> is the amount of time until a pod is considered offline. It can be set by the controller manager and is set to **5 minutes by default**.

Pods that were originally assigned to an offline node but were part of a replica set **will be assigned to other available nodes**. However, pods that were not part of a replica set will be lost.

When the node is online again, it will be in a "blank state" (i.e., no scheduled nodes) and will be unschedulable. The original pods on the node prior to rebooting will not be rescheduled.

```bash
kubectl drain <NODE_NAME>
```

The `drain` command will terminate all pods running on a node, so that they can be scheduled on other nodes. It will also restrict scheduling on the node.

```bash
kubectl drain <NODE_NAME> --ignore-daemonsets
```

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

## Kubernetes Releases
Similar to other software platforms, the Kubernetes development follows a standard version release process. A Kubernetes cluster will have its respective version.

A Kubernetes release consists of major, minor, and patch versions.
$$
\underbrace{1}_{major}. \underbrace{22}_{minor}. \underbrace{3}_{patch}
$$
Kubernetes releases can be found in the [releases page](https://github.com/kubernetes/kubernetes/releases) on the Kubernetes GitHub repository. The download file will contain executables for each cluster component.

A cluster's components **must never exceed** the version of the API server. The controller manager and the scheduler can be **one** version lower than the API server, while the kubelet and the kube proxy can be **two** versions lower than the API server. The `kubectl` command-line tool can be **within one** version of the API server.

Kubernetes supports only up to the **three recent minor versions**. It is recommended to upgrade the cluster by **one minor version at a time**, instead of upgrading immediately to the latest version.

In a hosted cloud service, cluster upgrades are supported and can be easily done by the service. In a cluster installed by `kubeadm`, there are convenient commands for upgrading. In a manually installed cluster, all upgrades are done manually.

### Upgrades
The master node is upgraded first. During the upgrade process, all cluster management functions done by the API server (e.g., scheduling, rescheduling) will not be performed.

The worker nodes are upgraded next. To ensure that <span style = "color:lightblue">end users</span> do not experience application downtime, nodes are upgraded sequentially with the process described in [[#^OSUPGRADES]].

Alternatively, new nodes can be "created" (*applicable to cloud servers*) with the desired version. Then, applications are transferred to the new nodes, while the old nodes are deleted.

The [Kubernetes documentation](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/) is especially useful during the upgrade procedure (e.g., latest stable release, commands to execute).

#### Master Components
The process for upgrading with `kubeadm` is detailed below.

```bash
apt-get upgrade -y kubeadm=<VERSION>
```

The above command will upgrade `kubeadm` to retrieve a new version.

```bash
kubeadm upgrade plan
```

The above command will plan the upgrade for the cluster and display the results. It will also show the upgrade command to execute.

```bash
kubeadm upgrade apply <VERSION>
```

Lastly, the above command will pull the necessary images and upgrade the cluster's components.

#### Worker Kubelet
Kubelet versions of all nodes, including the master node and the worker nodes, are not upgraded by `kubeadm`. It is done manually.

```bash
apt-get upgrade -y kubelet=<VERSION>
```

The `kubectl` configuration may also be needed to be upgraded.

```bash
kubeadm upgrade node
```

```bash
kubeadm upgrade node config --kubelet-version <VERSION>
```

The kubelet and relevant services are restarted.

```bash
systemctl daemon-reload
systemctl restart kubelet
```

> [!INFO]
> The version shown for each node in the `kubectl get nodes` command displays **the version of the kubelet**.

As detailed in [[#^OSUPGRADES]], pods will need to be moved to ensure no application downtime.

> [!INFO]
> All `kubectl` commands (i.e., commands for cluster management) are run on the master (controlplane) node.

### Backup & Restore
A cluster can be backed up from <span style = "color:lightblue">resource configurations</span>, the <span style = "color:lightblue">ETCD cluster</span>, or a simple <span style = "color:lightblue">persistent volume</span> with sufficient storage.

#### Resource Configurations
It is recommended to store resource configuration files in a source code repository such as GitHub.

In the case that some resources were run using a command (*thus, no configuration file*), the following command will get the configurations of all running resources in the cluster.

```bash
kubectl get all --all-namespaces -o yaml > <FILENAME>.yml
```

#### ETCD Cluster
By default, the <span style = "color:lightblue">ETCD data directory</span> of the ETCD cluster is `/var/lib/etcd`. This path can be used to obtain stored information of the ETCD.

> [!INFO]
> The command-line tool for ETCD is `etcdctl`.
> 
> It is important to set the ETCD API version before use.
> ```bash
> export ETCDCTL_API=3
> etcdctl version
> ```
> **If the API version is not set, some commands (e.g., `snapshot`) will not be available.**
> 
> To view additional options for commands and sub-commands, the `-h` or `--help` flag can be added.

The `save` and `status` commands will save and view a backup file respectively.

```bash
etcdctl snapshot save <FILENAME>.db
```

```bash
etcdctl snapshot status <FILENAME>.db
```

In a TLS-enabled ETCD database, it is mandatory to specify the following options when using the `save` command.
- `--endpoints`: endpoint (default: `127.0.0.1:2379`)
- `--cacert`: CA bundle to verify certificates of TLS-enabled secure servers (default: `ca.crt`)
- `--cert`: TLS certificate file (default: `server.crt`)
- `--key`: TLS key file (default: `server.key`)

```bash
etcdctl snapshot save backup.db \
--endpoints=127.0.0.1:2379 \
--cacert=/etc/kubernetes/pki/etcd/ca.crt \
--cert=/etc/kubernetes/pki
```

Details can be found under `etcd-certs` with the `describe` command.

To restore the cluster, the API server service must first be stopped before restoring the file.

```bash
service kube-apiserver stop
```

```bash
etcdctl snapshot restore <FILENAME>.db --data-dir /var/lib/etcd-from-backup
```

A new data directory is provided to avoid confusion. When starting the ETCD cluster service again, the data directory is modified to the new path with the `--data-dir` option. Lastly, the relevant services are restarted.

```bash
systemctl daemon-reload
```

```bash
service etcd restart
```

```bash
service kube-apiserver start
```


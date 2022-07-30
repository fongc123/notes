# Static Pods
A <span style = "color:lightblue">static pod</span> is a pod that is run manually on a node. Typically, in a cluster, the kubelet will listen for requests from the API server for new pod assignments. However, the kubelet will also check the `/etc/Kubernetes/manifests` path in a node for pod definitions even without a master node or scheduling components. Pod definition files placed in this path will be automatically created and managed by the kubelet.

The `--pod-manifest-path` option with a new path changes the default path.

```bash
--pod-manifest-path="/path/to/files"
```

The `--config` option with a YAML file containing the `staticPodPath` key and a path value also changes the default path.

```bash
--config=kubeconfig.yml
```

```yaml
# FILE: kubeconfig.yml
staticPodPath: "/path"
```

Replica sets or deployments cannot be created with this method. Run the following command and look for the config path specified in the `--config` option to view the config file and the static pod path.

```bash
ps -aux | grep kubelet
```

When there is no Kubernetes cluster, the `kubectl` command will not work. Instead, the `docker ps` command is used to view running static pods.

In a Kubernetes cluster, static pods are shown on the Kubernetes API as a **read-only** mirror image. Modification of static pods is not possible.

Control plane components are deployed as static pods on the master node (*shown as `-controlplane` in their names*). Their pod definition files are found in the static pod path.
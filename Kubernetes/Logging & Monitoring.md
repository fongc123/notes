# Logging & Monitoring

There are several methods for logging and monitoring cluster components and hosted applications.

## Cluster Components
Currently, Kubernetes does not come with built-in monitoring solutions. The following are some open source monitoring software.
- Metrics Server (*updated from Heapster*)
- Prometheus
- Elastic Stack
- DATADOG
- Dynatrace

The Metrics Server add-on only stores monitoring information **in-memory**. For more advanced features, the other softwares should be considered.

### Metrics Server
The <span style = "color:lightblue">container advisor (cAdvisor)</span> component, which is part of a kubelet, retrieves metrics data and sends it to the Metrics Server through the API.

If `minikube` is installed, the metrics server can be added with the `addons` command.

```bash
minikube addons enable metrics-server
```

Otherwise, the metrics server should be cloned from its repository link and created with the `kubectl` command.

```bash
git clone <METRICS_SERVER_LINK>
```

```bash
kubectl create -f <METRICS_SERVER_PATH>
```

The commands below show resource usage by nodes and by pods respectively.

```bash
kubectl top node
```

```bash
kubectl top pod
```

## Applications
The `logs` command can be used to stream the logs to the standard output (i.e., the terminal).

```bash
kubectl logs -f <POD_NAME>
```

If there are multiple container in a pod, the name of the container, as denoted in the pod definition file, **must** also be specified.

```bash
kubectl logs -f <POD_NAME> <CONTAINER_NAME>
```


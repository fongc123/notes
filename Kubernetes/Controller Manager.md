# Controller Manager
A process that continuously **monitors the state of the components of the system** and **works to bring the system to a desired functioning state**.

The node controller monitors the health and status of various nodes.
- monitor period: 5 seconds
- grace period: 40 seconds (*period before node is determined to be **unreachable***)
- eviction timeout: 5 minutes (*assign pods to other nodes*)

The replication controller monitors the status of replica sets.

## Installation
The kube-controller-manager can be installed by the following command.

```bash
wget https://storage.googleapis.com/kubernetes-release/release/v1.13.0/bin/linux/amd64/kube-controller-manager
```

Options can be specified in the `kube-controller-manager.service` file.

In a kube admin setup, the controller manager will be run as a pod. Its options can be shown using the following command.

```bash
cat /etc/kubernetes/manifests/kube-controller-manager.yaml
```

In a non-kube admin setup, the service's options can be shown using the following command.

```bash
cat /etc/systemd/system/kube-controller-manager.service
```

Run the following to list the processes to see the options as well.

```bash
ps -aux | grep kube-controller-manager
```

# Scheduler
It is responsible for deciding which pod is assigned to which node; however, it is the kublet on each node that *actually* creates a pod on its node.

Each pod has a set of resource requirements (i.e., CPU and memory), and each node has different specifications. To decide which node a pod must be scheduled on, the scheduler goes through the following steps.
1. Filter nodes that do not match a pod's requirements.
2. Assign a score to each node.

The score is determined by **how much resources would a node have left after a pod is assigned**.

There are also other requirements.
- taints and tolerations
- node selectors & affinity

## Installation
The kube-scheduler can be installed using the following command.

```bash
wget https://storage.googleapis.com/kubernetes-release/release/v1.13.0/bin/linux/amd64/kube-scheduler
```

In a kube admin setup, **the scheduler will be run as a pod**. Its options can be shown using the following command.

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

## Manual Scheduling
Typically, Kubernetes will handle scheduling automatically.
- What pod to schedule?
- Which node to schedule the pod to?

Pods that are scheduled will have the `nodeName` field in the pod definition.

Manually specifying the `nodeName` field on pod creation will assign the pod to the specified node.

```yaml
# FILE: pod-definition.yml
apiVersion: v1
kind: Pod
metadata:
	name: nginx
	labels:
		name: nginx
spec:
	containers:
	- name: nginx
	  image: nginx
	  ports:
	  - containerPort: 8080

	nodeName: node02
```

To manually schedule an existing pod, a `Binding` object can be defined, where the target node is specified.

```yaml
# FILE: pod-bind-definition.yml
apiVersion: v1
kind: Binding
metadata:
	name: nginx
target:
	apiVersion: v1
	kind: Node
	name: node02
```

Then, similar to what the scheduler automatically does, a `POST` request containing the `Binding` object definition **in a JSON format** is sent to the pod's binding API.

```bash
curl --header "Content-Type:application/json" --request POST --data '{ "apiVersion" : "v1", "kind" : "Binding" ... }' http://$SERVER/api/v1/namespaces/default/pods/$PODNAME/binding/
```

The command `kubetcl get nodes` will display the nodes in the Kubernetes cluster.

## Taints & Tolerations
A set of rules that restrict which pods can be scheduled to which nodes.

A <span style = "color:lightblue">taint</span> specifies which nodes have restricted scheduling.

A <span style = "color:lightblue">toleration</span> specifies which pods can *tolerate* a taint, allowing those pods to be scheduled on restricted nodes.

Taints are applied to nodes using the `taint` command.

```bash
kubectl taint nodes <NODE_NAME> <KEY>=<VALUE>:<TAINT_EFFECT>
```
- `NODE_NAME`: name of the node
- `KEY` and `VALUE`: key-value pair of a taint
- `TAINT_EFFECT`: effect of the taint if pod is not tolerant
	- `NoSchedule`: will not schedule
	- `PreferNoSchedule`: only *prefer* to not schedule
	- `NoExecute`: stop pre-existing pods running on the node as well

To untain a node, run the `taint` command with `-` at the end.

```bash
kubectl tain nodes <NODE_NAME> <KEY>=<VALUE>:<TAINT_EFFECT>-
```

Tolerations are applied to pods under the `tolerations` field in the definition file.

```yaml
# FILE: pod-definition.yml
apiVersion: v1
kind: Pod
metadata:
	name: myapp-pod
spec:
	containers:
	- name: nginx-container
	  image: nginx
	tolerations:
	- key: "app"
	  operator: "Equal"
	  value: "blue"
	  effect: "NoSchedule"
```

Values in the `tolerations` field are specified with **double quotation marks**.

> [!INFO]
> Taints and tolerations will not directly assign a particular pod to a particular node. Instead, it will only specify which pods **cannot** be assigned to a node. This is controlled by **Node Affinity**.

A taint is set up on the master node to not accept **any nodes**. The `describe` command can be used to view the details of a node (*and its taints*).

```bash
kubectl describe node <NODE_NAME>
```

```bash
kubectl describe node <NODE_NAME> | grep Taints
```

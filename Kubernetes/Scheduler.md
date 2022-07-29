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

A <span style = "color:lightblue">taint</span> specifies 
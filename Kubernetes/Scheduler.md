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
	- `NoExecute`: stop pre-existing pods running on the node as well (*the pod would have to be recreated*)

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
> Taints and tolerations will not directly assign a particular pod to a particular node. Instead, it will only specify which pods **cannot** be assigned to a node. This is controlled by **node affinity**.

A taint is set up on the master node to not accept **any nodes**. The `describe` command can be used to view the details of a node (*and its taints*).

```bash
kubectl describe node <NODE_NAME>
```

```bash
kubectl describe node <NODE_NAME> | grep Taints
```

## Labeling Nodes
Labels, which are used in <span style = "color:lightblue">node selectors</span> and <span style = "color:lightblue">node affinities</span>, can be added to nodes to classify them (e.g., based on hardware resources). To label a node, a key-value pair must be provided.

```bash
kubectl label nodes <NODE_NAME> <KEY>=<VALUE>
```

## Node Selectors
A <span style = "color:lightblue">node selector</span> is a specifies which nodes a particular pod can be run on. The `nodeSelector` field in the pod definition specifies the node based on a label.

```yaml
# FILE: pod-definition.yml
apiVersion: v1
kind: Pod
metadata:
	name: myapp-pod
spec:
	containers:
	- name: data-processor
	  image: data-processor
	nodeSelector:
		size: Large
```

In the above code block, the pod only runs on nodes with the label with the `size` key equal to `Large`.

## Node Affinity
A <span style = "color:lightblue">node affinity</span> allows more control over pod-node scheduling. Advanced expressions, such as `OR` or `NOT`, are not supported in node selectors.

The `affinity` field is added to specify node affinity.

```yaml
# FILE: pod-definition.yml
apiVersion: v1
kind: Pod
metadata:
	name: myapp-pod
spec:
	containers:
	- name: data-processor
	  image: data-processor
	affinity:
		nodeAffinity:
			requiredDuringSchedulingIgnoredDuringExecution:
				nodeSelectorTerms:
				- matchExpressions:
				  - key: size
				    operator: In
				    values:
				    - Large
				    - Medium
```

The pod with the above specifications will be placed in nodes with labels `Large` and `Medium`. Other operators include the following.
- `NotIn`: label is **not in** values
- `Exists`: label exists

There are three (two available, one planned) types of node affinity.
- `requiredDuringSchedulingIgnoredDuringExecution`: affinity rules required when *first* scheduled but ignored while running
- `preferredDuringSchedulingIgnoredDuringExecution`: affinity rules preferred when *first* scheduled but ignored while running
- `requiredDuringSchedulingRequiredDuringExecution`: affinity rules required when *first* scheduled *and* while running

> [!INFO]
> Node selectors and node affinities only control where certain **pods** can be scheduled on. **Other nodes can still be assigned to labeled pods which may be taking up resources intended for the pods with node affinity.**

These types will determine scheduling behaviour when a suitable node was not found.

A possible summarization could be: taints and tolerations specify **blacklisted nodes**, while node selectors and node affinities specify **whitelisted nodes**. Generally, a combination of taints, tolerations, and node affinities are used together to accomplish a desired scheduling configuration.

## Resource Requirements
Each pod has its own resource requirements. If there are no nodes with available resources, a pod will in a `Pending` state (*not scheduled*).

By default, Kubernetes assumes that each pod has a <span style = "color:lightblue">resource requests</span> of **0.5 CPU** and **256 Mi**. Resource requirements can be changed in the pod definition file.

One CPU is equivalent to one AWS vCPU, one GCP Core, one Azure Core, or one hyperthread.

## Resource Limits
By default, Kubernetes sets a limit of **1 vCPU** and **512 Mi RAM** to pods.

A pod cannot exceed its CPU limits. On the other hand, a pod can exceed its memory limits; however, if it exceeds it for too long, the pod will be **terminated**.

Resource requirements and limits can be modified in the pod definition file.

```yaml
# FILE: pod-definition.yml
apiVersion: v1
kind: Pod
metadata:
	name: simple-webapp
spec:
	containers:
	- name: simple-webapp
	  image: simple-webapp
	  ports:
	  - containerPort: 8080
	  resources:
		  requests:
			  memory: "1Gi"
			  cpu: 1
		  limits:
			  memory: "2Gi"
			  cpu: 2
```


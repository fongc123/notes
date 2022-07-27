# Replica Sets
A <span style = "color:lightblue">replica set</span> achieves <span style = "color:lightblue">high avalability (HA)</span> by **creating new instances of a pod** to ensure that the specified number of pods are running. It is also used for load balancing and scaling.

> [!INFO]
> The **replication controller** is old technology which is currently replaced by the **replica set**. Both work towards achieving the same objectives mentioned above. This document will use replica sets.

<span style = "color:lightblue">High avalability</span> refers to the constant avalability of an application to users.

## YAML Configuration
Similar to pods, a replica set can be configured in a YAML file. All replica set files must have the same required fields as a pod configuration. There are three additional **children fields** of the `spec` field that must be added as well.
- `template`: template of a pod (*copied from a pod configuration*)
- `replicas`: the number of instances to create
- `selector`: other pods that are also considered (*specified using labels*)

The `selector` field allows other pre-existing pods specified using their labels to be considered in the replication as well.

```yaml
# FILE: replicaset-definition.yml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
	name: myapp-replicaset
	labels:
		app: myapp
		type: front-end
spec:
	template:
		metadata:
			name: myapp-pod
			labels:
				app: myapp
				type: front-end
		spec:
			containers:
			- name: nginx-container
			  image: nginx
	replicas: 3
	selector:
		matchLabels:
			type: front-end
```

The command `kubectl create -f <FILENAME>.yml` is used to create the replica set. The command `kubectl get replicaset` will show details about a replica set and the number of desired replicas. Pods will be started based on the replica set specifications which can be viewed in `kubectl get pods`.

The command `kubectl delete replicaset <REPLICA_SET>` is used to delete a replica set.

The replica set can be updated with the command `kubectl edit replicaset <REPLICA_SET>`.

For reference, the configuration file and relevant commands for a replication controller are shown below.

```yaml
# FILE: replicacontroller-definition.yml
apiVersion: v1
kind: ReplicationController
metadata:
	name: myapp-rc
	labels:
		app: myapp
		type: front-end
spec:
	template:
		metadata:
			name: myapp-pod
			labels:
				app: myapp
				type: front-end
		spec:
			containers:
			- name: nginx-container
			  image: nginx
	replicas: 3
```

Run `kubectl get replicationcontroller` to view the replication controller.

> [!INFO]
> The main difference between a replication controller and a replica set is that the replica set has an extra `selector` field that can be specified.

## Scaling
The number of replicas can be scaled by changing the `replicas` field in the configuration file.

```bash
kubectl replace -f <FILENAME>.yml
```

The `replace` command will update the replica set in the cluster. Alternatively, the `scale` command can be used.

```bash
kubectl scale --replicas=6 -f <FILENAME>.yml
```

```bash
kubectl scale --replicas=6 <KIND> <NAME>
```

The filename *or* the kind (i.e., `replicaset`) and name can be specified.

> [!INFO]
> When using the `scale` command, the configuration file itself won't be updated to the new number of replicas.

## Auto-scaling


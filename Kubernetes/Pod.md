# Pod
A pod is a single instance of a Docker container (*application*) and is the smallest object that can be created in Kubernetes.
$$
App \rightarrow Container \rightarrow Pod
$$
As workload increases, more pods will be created to share the workload between multiple Docker-containerized applications.

Additional nodes with pods can be added to the cluster to balance the workload as well.

<span style = "color:lightblue">Scaling up</span> creates more pods, while <span style = "color:lightblue">scaling down</span> deletes existing pods.

<span style = "color:lightblue">Multi-container pods</span> are pods that have multiple containers in them. Typically, only one container is in a pod; however, it may be beneficial for <span style = "color:lightblue">helper containers</span> to exist alongside with the main container. Since they exist in the same pod, these containers refer to each other using `localhost`.

## Deployment
To start an instance of an application, run the following command.

```bash
kubectl run <NAME> --image <IMAGE_NAME>
```

The cluster will create a pod and will pull the `IMAGE_NAME` image from <span style = "color:lightblue">Docker Hub</span>. To view running pods, run the following command.

```bash
kubectl gets pods
```

The status of each pod can be viewed.

## Configuration with YAML
A pod can be configured with a YAML file. All pod files must have four required fields.
- `apiVersion`: Kubernetes API version (e.g., `v1` or `apps/v1`)
- `kind`: the type of the object (e.g., `Pod`, `Service`, `ReplicaSet`, or `Deployment`)
- `metadata`: user-defined information about the pod
- `spec`: pod specifications

> [!INFO]
> The `metadata` field does **not** specify the containers to be run on the pod. Pod specifications are specified in the `specs` field.

A sample configuration file for a single-container pod named `myapp-pod` that runs an `nginx` application is shown below.

```yaml
# FILE: pod-definition.yaml
apiVersion: v1
kind: Pod
metadata:
	name: myapp-pod
	labels:
		app: myapp
		type: front-end
spec:
	containers: # array (one or more containers)
	- name: nginx-container
	  image: nginx
```

The command `kubectl create -f <FILE_NAME>.yaml` is used to create a pod in the Kubernetes cluster. The command `kubectl describe pod <POD_NAME>` will show details about a pod.


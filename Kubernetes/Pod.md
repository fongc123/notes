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
To start a pod (i.e., start an instance of a container), run the following command.

```bash
kubectl run <NAME> --image=<IMAGE_NAME>
```

The cluster will create a pod and will pull the `IMAGE_NAME` image from <span style = "color:lightblue">Docker Hub</span>. The `--port` option can be added to specify the port the container will expose (i.e., which port the container will run on). **This is not the same as services.** To view running pods, run the following command.

```bash
kubectl gets pods
```

```bash
kubectl get pods -o wide
```

The status of each pod can be viewed.

## YAML Configuration
A pod can also be configured with a YAML file. All pod files must have four required fields.
- `apiVersion`: Kubernetes API version (e.g., `v1` or `apps/v1`)
- `kind`: the type of the object (e.g., `Pod`, `Service`, `ReplicaSet`, or `Deployment`)
- `metadata`: user-defined information about the pod
- `spec`: pod specifications

> [!INFO]
> The `metadata` field does **not** specify the containers to be run on the pod. Pod specifications are specified in the `specs` field.

A sample configuration file for a single-container pod named `myapp-pod` that runs an `nginx` application is shown below.

```yaml
# FILE: pod-definition.yml
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

Alternatively, the `run` command can be used to generate a configuration file.

```bash
kubectl run <NAME> --image=<IMAGE_NAME> --dry-run=client -o yaml > <FILENAME>.yml
```

> [!INFO]
> The `>` symbol directs the terminal output to a location (e.g., a file).

The command `kubectl create -f <FILENAME>.yml` is used to create a pod in the Kubernetes cluster. The command `kubectl describe pod <POD_NAME>` will show details about a pod (*add the `--all` option to delete all*).

The command `kubectl delete pod <POD_NAME>` is used to delete a pod. The `delete` command can be applied to other Kubernetes components.

The pod can be updated with the command `kubectl edit pod <POD_NAME>`. Alternatively, given that the configuration file has been changed, a pod can be updated with the command `kubectl replace -f <FILENAME>.yml`. The command `kubectl apply -f <FILENAME>.yml` will only work if the pod was previously created with `apply` as well (*a last applied configuration exists*).

Below are some other useful options.
- `--force`: force the operation
- `--watch`: watch for any changes
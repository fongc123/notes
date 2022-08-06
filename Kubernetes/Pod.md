# Pod
A pod is a single instance of a Docker container (*application*) and is the smallest object that can be created in Kubernetes.
$$
App \rightarrow Container \rightarrow Pod
$$
As workload increases, more pods will be created to share the workload between multiple Docker-containerized applications.

Additional nodes with pods can be added to the cluster to balance the workload as well.

<span style = "color:lightblue">Scaling up</span> creates more pods, while <span style = "color:lightblue">scaling down</span> deletes existing pods.

<span style = "color:lightblue">Multi-container pods</span> are pods that have multiple containers in them. Typically, only one container is in a pod; however, it may be beneficial for <span style = "color:lightblue">helper containers</span> to exist alongside with the main container. Since they exist in the same pod, these containers refer to each other using `localhost`.

## Creation
### Command
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

### YAML Configuration
A pod can also be configured with a YAML file. All pod files must have four required fields.
- `apiVersion`: Kubernetes API version (e.g., `v1` or `apps/v1`)
- `kind`: the type of the object (e.g., `Pod`, `Service`, `ReplicaSet`, or `Deployment`)
- `metadata`: user-defined information about the pod (`name` and `labels` help identify the pod)
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

The pod can be updated with the command `kubectl edit pod <POD_NAME>`. Alternatively, given that the configuration file has been changed, a pod can be updated with the command `kubectl replace -f <FILENAME>.yml`. The command `kubectl apply -f <FILENAME>.yml` will only work if the pod was previously created with `apply` as well (i.e., a last applied configuration exists).

When a pod is running, the `edit` command cannot modify specifications except the following.
- `spec.containers[*].image`
- `spec.initContainers[*].image`
- `spec.activeDeadlineSeconds`
- `spec.tolerations`

The current configuration file can be generated with the following command.

```bash
kubectl get pod <POD_NAME> -o yaml > <FILENAME>.yml
```

If changes are made to the file and the `replace` command is used, the previous pod will be deleted.

The `exec` command can execute a specified command inside the container of a pod.

```bash
kubectl exec -it <POD_NAME> -- <COMMAND>
```

Below are some other useful options.
- `--force`: force the operation (*often used with `replace`*)
- `--watch`: watch for any changes
- `--selector`: specify labels in a key-value format (e.g., `--selector="env=dev"`)
- `wc`: word count (*add `-l` option*)
- `--no-headers`: no headers

## Static Pods
A <span style = "color:lightblue">static pod</span> is a pod that is run **manually** on a node. Typically, in a cluster, the kubelet will listen for requests from the API server for new pod assignments.

However, the kubelet will also check the following path in a node for pod definitions even without a master node or scheduling components.

```bash
/etc/kubernetes/manifests
```

Definition files placed in this path will be automatically created and managed by the kubelet.

The `--pod-manifest-path` changes the default path.

```bash
--pod-manifest-path="/path/to/files"
```

The `--config` option with a YAML file containing a `staticPodPath` key and a path value also changes the default path.

```bash
--config=kubeconfig.yml
```

```yaml
# FILE: kubeconfig.yml
staticPodPath: "/path/to/files"
```

Replica sets or deployments cannot be created with this method. Run the following command and look for the config path specified in the `--config` option to view the config file and the static pod path.

```bash
ps -aux | grep kubelet
```

The static pod path can also be found under `staticPodPath` with the following command.

```bash
cat /var/lib/kubelet/config.yml
```

Static pods can be identified by the `ownerReferences` field in the YAML configuration output. The `kind` of the owner should be a `Node` instead of a `ReplicaSet` or a `Deployment`.

When there is no Kubernetes cluster, the `kubectl` command will not work. Instead, the `docker ps` command is used to view the running static pods.

In a Kubernetes cluster, static pods are shown on the Kubernetes API as **read-only** mirror images. Modification of static pods is not possible. For example, when deleting a static pod, Kubernetes would automatically create it again. The original YAML definition file would have to be deleted on the specific node.

Control plane components are deployed as static pods on the master node (*shown as `--<NODE_NAME>` in their names*). Their pod definition files are found in the static pod path.

## Multi-container Pods
For multi-container pods, additional containers with image names can be specified under the `containers` field.

```yaml
# FILE: multi-container-pod-definition.yml
apiVersion: v1
kind: Pod
metadata:
	name: myapp-pod
	labels:
		app: myapp
		type: front-end
spec:
	containers:
	- name: nginx-container
	  image: nginx
	- name: log-agent
	  image: log-agent
```

Typical multi-container pods include **sidecar**, **adapter**, or **ambassador**.

## initContainer Pods
An <span style = "color:lightblue">initContainer pod</span> is a container that first runs **to completion** on pod creation and startup before the main container in the pod starts.

If there are multiple initContainers, each initContainer is run sequentially. The main container will only start once **all initContainers are complete**.

initContainers are specified under the `initContainers` field.

```yaml
# FILE: init-container-pod-definition.yml
apiVersion: v1
kind: Pod
metadata:
	name: myapp-pod
	labels:
	app: myapp
spec:
	containers:
	- name: myapp-container
	  image: busybox:1.28
	  command: [ 'sh', '-c', 'echo Hello && sleep 3600']
	initContainers:
	- name: init-myservice
	  image: busybox
	  command: [ 'sh', '-c', 'git clone <link>; done;']
```

When the `describe` command is used on a pod, initContainers can be identified under the `Init Containers` section.

**If any of the initContainers fail, Kubernetes restarts the pod repeatedly until the initContainer succeeds.**
# Namespace
A <span style = "color:lightblue">namespace</span> enables isolation of resources and objects in the Kubernetes cluster.

The <span style = "color:lightblue">default</span> namespace is automatically created when the cluster is first set up. The `kube-system` and `kube-public` namespaces are also created for internal operations (e.g., for running Kubernetes components).

Custom namespaces can be created to organize resources and components (e.g., develop and production namespaces).

Objects within the same namespace refer to each other by their names. Objects *outside* the namespace must refer to each other by their name **and** the corresponding namespace (e.g., `<SERVICE_NAME>.<NAMESPACE>.<SERVICE>.<DOMAIN>`)

## Specifying Namespaces

The `--namespace` option (or `-n`) is used to specify the namespace. For example, the command below lists pods in the `kube-system` namespace.

```bash
kubectl get pods --namespace=kube-system 
```

Configuration files can also contain the `namespace` field to ensure that an object is created in the specified namespace.

```yaml
# FILE: pod-definition.yml
apiVersion: v1
kind: Pod
metadata:
	name: myapp-pod
	namespace: dev
	labels:
		app: myapp
		type: front-end
spec:
	containers:
	- name: nginx-container
	  image: nginx
```

To permanently change the namespace, the context can be changed.

```bash
kubectl config set-context $(kubectl config current-context) --namespace=<NAMESPACE>
```

With this, the `--namespace` option is not needed anymore when running commands. The `--all-namespaces` option will display information in all namespaces.

## Namespace Creation
A namespace can be created using the `create` command.

```bash
kubectl create namespace dev
```

Alternatively, a namespace can be created with a configuration file.

```yaml
# FILE: namespace-dev.yml
apiVersion: v1
kind: Namespace
metadata:
	name: dev
```

## Resource Quota
A quota on each namespace can also be specified, limiting the resource usage of each namespace.

```yaml
# FILE: compute-quota.yml
apiVersion: v1
kind: ResourceQuota
metadata:
	name: compute-quota
	namespace: dev
spec:
	hard:
		pods: "10"
		requests.cpu: "4"
		requests.memory: 5Gi
		limits.cpu: "10"
		limits.memory: 10Gi
```


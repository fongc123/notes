# Application Management
Kubernetes has several functions to manage <span style = "color:lightblue">application life cycles</span>.

## Rolling Updates & Rollbacks
Deployment versions are updated to a new version with <span style = "color:lightblue">rollouts</span> and reverted to a previous version with <span style = "color:lightblue">rollbacks</span>. The commands below will show the **rollout status** and the **rollout history** respectively.

```bash
kubectl rollout status <DEPLOYMENT_NAME>
```

```bash
kubectl rollout history <DEPLOYMENT_NAME>
```

All three commands below will update the deployment; however, only the first one will edit the configuration file.

```bash
kubectl apply -f <FILENAME>.yml
```

```bash
kubectl set image <DEPLOYMENT> <CONTAINER>:<IMAGE>
```

```bash
kubectl edit deployment <DEPLOYMENT_NAME>
```

The `describe` command is used to view the rollout strategy, as shown under the `StrategyType` field.

```bash
kubectl describe <DEPLOYMENT_NAME>
```

It is noted that the changes to the number of replicas are different in different rollout strategies. To rollback a deployment, the `undo` command is used.

```bash
kubectl rollout undo <DEPLOYMENT_NAME>
```

### Strategy: Recreate
In the <span style = "color:lightblue">recreate</span> deployment strategy, pods that must be updated with a newer version will be deleted all at once. Then, new pods with a newer version will be created.

**In between pod deletion and creation, there will be downtime. This is not the default Kubernetes deployment strategy.**

### Strategy: Rolling Update
In the <span style = "color:lightblue">rolling update</span> deployment strategy, pods that must be updated will be deleted and recreated sequentially.

**This will ensure minimal downtime.**

### Additional Notes

When a new deployment is triggered, pods are created in a new replica set to accomdate the changes, while the pods in the old replica set are simultaneously deleted.

The `RollingUpdateStrategy` field will show how many pods can be down at any given time. For example, if there are **four pods** and **25% unavailable**, there can be only one pod down at any given time.

The `edit` command can be used to change the deployment update strategy. It is noted that the old strategy properties (e.g., `strategy.rollingUpdate`) must also be removed.

## Configuration
### Commands
In a pod definition file, arguments can be passed under the `containers.args` field to specify additional settings when running the container. The `containers.command` field changes the command on container startup.

```yaml
# FILE: pod-definition.yml
apiVersion: v1
kind: Pod
metadata:
	name: myapp-pod
spec:
	containers:
	- name: mycontainer
	  image: myimage
	  command:
	  - "command"
	  args:
	  - "10"
```



The Docker `ENTRYPOINT` keyword corresponds to the Kubernetes `command` field, while the Docker `CMD` keyword corresponds to the Kubernetes `args` field.

The container will always be run from `ENTRYPOINT`; however, if the Kubernetes `command` field is specified, **the original command and any arguments in `CMD` will be overwritten**.

The `args` field will only overwrite arguments specified from `CMD`. It will not overwrite the `ENTRYPOINT` command.

> [!INFO]
> The Docker `CMD` keyword will append arguments to the command denoted in the Docker `ENTRYPOINT` keyword.
> 
> The following Dockerfile configuration is considered.
> ```Docker
> # FILE: Dockerfile
> ENTRYPOINT [ "command" ]
> CMD [ "10" ]
> ```
> A Docker container with the above configuration will run the command `command 10` when started.

#### Syntax Variations
The following syntaxes are valid.

```yaml
command: [ "command" ]
args: [ "10" ]
```

```yaml
command:
- "command"
- "10"
```

```yaml
command: [ "command", "10" ]
```

It is noted that commands and arguments are *never* placed within the same quotation marks.

### Environment Variables
<span style = "color:lightblue">Environment variables</span> are specified in a plain key-value format, where `name` is the key and `value` is the value.

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
	  env:
	  - name: APP_COLOR
	    value: pink
```

Alternatively, environment variables can be specified using <span style = "color:lightblue">config maps</span> or <span style = "color:lightblue">secrets</span>. The source of the value (config map or secret) is specified instead of the value itself.

### Config Maps
<span style = "color:lightblue">Config maps</span> are central storage locations for configuration values, making configuration management easier.

#### Creation
To create a config map, an imperative command can be run. The `--from-literal` option can be specified as many times as needed and will read in key-value pairs.

```bash
kubectl create configmap <NAME> --from-literal=<KEY>=<VALUE>
```

The `--from-file` option can be used to read in values from a file.

```yaml
kubectl create configmap <NAME> --from-file=<PATH>
```

The file must have a file type of `.properties`. Alternatively, a declarative definition file can be created.

```yaml
# FILE: config-map.yml
apiVersion: v1
kind: ConfigMap
metadata:
	name: app-config
data:
	APP_COLOR: blue
	APP_MODE: prod
```

```bash
kubectl create -f config-map.yml
```

Key-value pairs are stored under the `data` field. The `get` and `describe` commands will list all config maps and get details of a specific config map respectively.

#### Pod Injection
To apply config maps to a pod, they must be injected into a pod definition file. The `envFrom.configMapRef` will reference a config map object to read configuration values from.

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
	  envFrom:
	  - configMapRef:
		    name: app-config
```

In the above pod definition with the previous config map definition, the pod's environment should have variable `APP_COLOR` equal to `blue` and variable `APP_MODE` equal to `prod`.

> [!INFO]
> Multiple config maps can be specified under `envFrom`.


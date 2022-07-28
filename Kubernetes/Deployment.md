# Deployment
The Kubernetes <span style = "color:lightblue">deployment</span> manages <span style = "color:lightblue">version control</span> in deployed applications.

A <span style = "color:lightblue">rolling update</span> is performed when a **new version** of an application is available, where running instances are replaced with new instances **sequentially** (i.e., not all at once).

If the update contained a bug, a <span style = "color:lightblue">rollback</span> will revert the instance versions sequentially as well.

Other changes made to the pods in the deployment will also take effect in a manner that will not affect the user's experience.

## YAML Configuration
Other than the `kind`, the deployment configuration has the same required fields as that of a replica set.

```deployment-definition.yml
apiVersion: apps/v1
kind: Deployment
metadata:
	name: myapp-deployment
	labels:
		app: myapp
		type: front-end
spec:
	template:
		metadata:
			name: myapp
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

The `create` command can be used to create the deployment. The `get` command will show details about deployments, replica sets, and pods which should all be running according to the configuration file.

A deployment can also be created without a configuration file. An example is shown below.

```bash
kubectl create deployment <NAME> --image=<IMAGE_NAME> --replicas=<NUM>
```

```bash
kubectl create deployment <NAME> --image=<IMAGE_NAME> --replicas=<NUM> --dry-run=client -o yaml > <FILENAME>.yaml
```

The former will create a deployment, while the latter will generate a YAML configuration file.
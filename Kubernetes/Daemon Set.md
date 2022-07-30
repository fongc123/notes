# Daemon Set
A <span style = "color:lightblue">daemon set</span>, similar to a replica set, ensures that at least one instance of a pod is running on each node. A daemon set is a great solution for **monitoring** or **logging** pods.

After verison 1.12, a daemon set uses <span style = "color:lightblue">node affinity</span> and the default scheduler to schedule one pod for each node.

## YAML Configuration
Similar to replica sets, a daemon set can be configured in a YAML file.

```yaml
# FILE: daemon-set-definition.yml
apiVersion: apps/v1
kind: DaemonSet
metadata:
	name: monitoring-daemon
spec:
	selector:
		matchLabels:
			app: monitoring-agent # match `labels`
	template:
		metadata:
			labels:
				app: monitoring-agent # match `matchLabels`
		spec:
			containers:
			- name: monitoring-agent
			  image: monitoring-agent
```

The `create` and `get` commands can be used to create and view daemon sets respectively.

A quick way to create a daemon set is to generate the YAML file from a `deployment` configuration and change the `Kind` field to `DaemonSet`.
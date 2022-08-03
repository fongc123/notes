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

## Commands

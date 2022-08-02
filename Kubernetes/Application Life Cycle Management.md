# Application Life Cycle Management
Kubernetes has several functions to manage <span style = "color:lightblue">application life cycles</span>.

## Rolling Updates & Rollbacks
Deployment versions are updated to a new version with <span style = "color:lightblue">rollouts</span> and reverted to a previous version with <span style = "color:lightblue">rollbacks</span>.

```bash
kubectl rollout status <DEPLOYMENT_NAME>
```

```bash
kubectl rollout history <DEPLOYMENT_NAME>
```

The commands above will show the **rollout status** and the **rollout history** respectively.

### Strategy: Recreate
In the <span style = "color:lightblue">recreate</span> deployment strategy, pods that must be updated with a newer version will be deleted all at once. Then, new pods with a newer version will be created.

**In between pod deletion and creation, there will be downtime. This is not the default Kubernetes deployment strategy.**

### Strategy: Rolling Update
In the <span style = "color:lightblue">rolling update</span> deployment strategy, pods that must be updated will be deleted and recreated sequentially.

**This will ensure minimal downtime.**


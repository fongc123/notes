# Deployment
The Kubernetes <span style = "color:lightblue">deployment</span> manages <span style = "color:lightblue">version control</span> in deployed applications.

A <span style = "color:lightblue">rolling update</span> is performed when a **new version** of an application is available, where running instances are replaced with new instances **sequentially** (i.e., not all at once).

If the update contained a bug, a <span style = "color:lightblue">rollback</span> will revert the instance versions sequentially as well.

Other changes made to the pods in the deployment will also take effect in a manner that will not affect the user's experience.


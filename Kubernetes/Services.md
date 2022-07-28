# Services
A <span style = "color:lightblue">service</span> enable communication between pods and external users.

## External Access
Components inside a Kubernetes node share the same network which cannot be accessed from outside. Although `ssh` is possible, it is not a good method.

A <span style = "color:lightblue">NodePort service</span> maps the IP of the node through the internal pod network to the IP of a pod hosting an application.

$$
External \rightarrow NodePort \rightarrow Service \rightarrow Port \rightarrow TargetPort \space\rightarrow Pod
$$
The NodePort is in the range of 30000 to 32767.

Once set up, the pod can be accessed using the node's IP address at the forwarded NodePort.

## Internal Access
A <span style = "color:lightblue">ClusterIP</span> creates a virtual IP inside the cluster to enable communication between different services and applications.

## Load Balancer
A <span style = "color:lightblue">LoadBalancer</span>, in addition to handling external access, also manages requests to be forwarded to different pods based on the traffic load.

## YAML Configuration
Similar to pods, replica sets, and deployments, a service definition must have the same four required fields. There are three additional **children fields** of the `spec` field that must be added as well.
- `type`: type of service (*shown above*)
- `ports`: information regarding ports to forward traffic
	- `targetPort`: port of the pod
	- `port`: port on the service
	- `nodePort`: port on the node
- `selector`: labels to identify which pods to link to the service

The fields `port` and `targetPort` will be assumed to be the same if one is not given. The field `nodePort` will be automatically allocated to a free port in the valid range if it is not given.

```service-definition.yml
apiVersion: v1
kind: Service
metadata:
	name: myapp-service

spec:
	type: NodePort
	ports:
	- targetPort: 80
	  port: 80
	  nodePort: 30008
	selector:
		app: myapp
		type: front-end
```

The `create` and `get` command can be used to create the service and get details about services respectively.

> [!INFO]
> A service uses a **random** load-balancing algorithm with `SessionAffinity`.


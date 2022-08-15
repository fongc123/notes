# Design
Listed below are some design ideas to consider when designing a Kubernetes cluster.
- purpose
	- education (**Minikube** or single-node cluster with `kubeadm` or with cloud hosting)
	- development or testing (multi-node cluster with `kubeadm` or with cloud hosting)
	- production
		- high availability
		- multi-node cluster with `kubeadm` or cloud hosting
		- multiple master nodes
		- 5,000 nodes, 150,000 pods, 100 pods per node, and 300,000 total containers
- cloud or on-premise (`kubeadm` for an on-premise setup)
- storage
	- SSD backed storage (high performance)
	- network-based storage (multiple concurrent connections)
	- persistent shared volumes across pods
- nodes
	- virtual or physical
	- Linux x86_64 architecture
	- **recommended:** a cluster with four nodes
- workloads
	- amount
	- kind (e.g., web, big data, analytics, etc.)
	- resource requirements (e.g., CPU-intensive or RAM-intensive)
	- network traffic

> [!INFO]
> Master nodes *can* host workloads; however, it is recommended to have master nodes host only controlplane components.

> [!INFO]
> In high availability environments, the ETCD cluster server can be moved into its own node.

> [!INFO]
> Kubernetes cannot be installed on Windows. A Linux virtual machine would need to be installed.


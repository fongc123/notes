# Design
Listed below are some design ideas to consider when designing a Kubernetes cluster.
- purpose
	- education (**Minikube** or single-node cluster with `kubeadm` or with cloud hosting)
	- development or testing (multi-node cluster with `kubeadm` or with cloud hosting)
	- production
		- high availability (redundancy on all Kubernetes components)
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
> Kubernetes cannot be installed on Windows. A Linux virtual machine would need to be installed.

## Infrastructure
Minikube is primarily used for education or testing purposes, where it automatically deploys virtual machines for the user but can only create a single-node cluster. The `kubeadm` tool is used for development, testing, and production environments, where multi-node clusters are generally recommended, but requires virtual machines to be managed and set up before hand.

<span style = "color:lightblue">Turnkey solutions</span> require the administrator to provision, configure, and maintain the virtual machines as well as to manage Kubernetes. Some on-premise turnkey solution softwares include OpenShift, Cloud Foundry Container Runtime, VMware Cloud PKS, and Vagrant.

In <span style = "color:lightblue">hosted solutions</span>, the maintenaces of the virtual machines and the Kubernetes installation are done by the cloud provider beforehand.

In a high availability environment, multiple master nodes are run to prevent a single point failure. A <span style = "color:lightblue">load balancer</span>, such as Nginx or HA Proxy, distributes workloads across the API servers of the master nodes. For schedulers and controller managers, only one can be active at the same time. The `--leader-elect` option specifies which instance is set to active, while the other instances are on standby.

In a <span style = "color:lightblue">stacked topology</span>, the ETCD clusters are run in the same node with the controlplane components. It is easy to set up but has risks when the node fails. In a <span style = "color:lightblue">external ETCD topology</span>, the ETCD clusters are run on different nodes. It is less risky but is harder to set up and requires more servers. The API server must point to the correct address that the ETCD cluster is hosted at.

The ETCD cluster can be <span style = "color:lightblue">distributed</span> across multiple instances and should have the same state. Among all the ETCD servers, one instance is elected a leader by the <span style = "color:lightblue">RAFT protocol</span>, where write operations are processed and distributed to other instances. Read operations from any of the instance will return the same information.


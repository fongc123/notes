# Cluster Architecture
The purpose of <span style = "color:lightblue">Kubernetes</span> is to host your applications on containers in an automated fashion, such that it is easy to deploy as many instances as required and that it allows communication between different services.

## Nodes
The cluster consists of two types of nodes: <span style = "color:lightblue">worker</span> and <span style = "color:lightblue">master</span>. Nodes can be any machine (*on-premise or on cloud*) that is part of the cluster.

<span style = "color:lightblue">Worker nodes</span> host applications in containers.
- [[Kublet|kubelet]]: agent on each worker node that listens to the <span style = "color:lightblue">kube-apiserver</span> for instructions and sends reports
- [[Kube Proxy|kube-proxy]]: ensures communication between services

<span style = "color:lightblue">Master nodes</span> are responsible for managing the cluster and planning, scheduling, and monitoring the worker nodes.
- <span style = "color:lightblue">control plane components</span>: components that allow the master node to perform its functions
- [[ETCD Cluster|ETCD cluster]]: key-value database that keeps information about nodes
- [[Scheduler|kube-scheduler]]: schedules containers to correct nodes based on requirements and policies
- [[Controller Manager|controller-manager]]: management of containers
	- <span style = "color:lightblue">node-controller</span>: maintains nodes
	- <span style = "color:lightblue">replication-controller</span>: ensures that the desired number of containers are running at all times
- [[Kube API Server|kube-apiserver]]: communication to pods and external access

## Container
It is the <span style = "color:lightblue">container runtime engine</span> that is used by the cluster to containerize applications. Two examples include <span style = "color:lightblue">Docker</span> or <span style = "color:lightblue">containerd</span>.

## Analogy
A simple analogy of **cargo ships** is provided.
- nodes → ships
- controller-manager → operations offices
- kube-scheduler → loading crane
- kublet → ship captain

![[k8s-arch.png|center|650]]


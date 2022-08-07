# Security
As Kubernetes is a reliable, production-grade solution to hosting applications, security is an important issue.

As the API server is what communicates to internal components and external access, it is the first line of defense.

Security in Kubernetes controls **who can access the cluster** ([[#^8c9d4f]]) and **what can they do** ([[#^e8e0d8]]).

All communication between Kubernetes components are secured with <span style = "color:lightblue">TLS encryption</span>.

By default, communication between applications in a pod is not restricted; however, this can be changed with <span style = "color:lightblue">network policies</span>.

## Authentication
^8c9d4f

There are several options for authenticating a connection.
- files
	- usernames and passwords
	- usenames and tokens
- certificates
- external authentication providers (LDAP)
- service accounts (*for machines*)



### TLS Encryption


## Authorization
^e8e0d8

There are several options for authorizing a connection.
- RBAC authorization
- ABAC authorization
- node authorization
- webhook mode


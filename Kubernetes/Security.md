# Security
As Kubernetes is a reliable, production-grade solution to hosting applications, security is an important issue.

As the API server is what communicates to internal components and external access, it is the first line of defense.

Security in Kubernetes controls **who can access the cluster** ([[#^8c9d4f]]) and **what can they do** ([[#^e8e0d8]]).

All communication between Kubernetes components are secured with <span style = "color:lightblue">TLS encryption</span>.

By default, communication between applications in a pod is not restricted; however, this can be changed with <span style = "color:lightblue">network policies</span>.

## Authentication
^8c9d4f

There are several mechanisms for authenticating a connection.
- files
	- usernames and passwords
	- usenames and tokens
- certificates
- external authentication providers (e.g., LDAP)
- service accounts (*for bot integration*)

All cluster administrative access is handled by the API server.

It is noted that usage of static files for authentication **is not recommended** as it is **not secure**. In fact, they are deprecated since version `1.19`, and other authentication methods are used instead.

### Files
#### Static Password File
Credentials can be provided in a `.csv` file, where each entry contains a password, username, user ID, and, optionally, a user group.

```
password123,user1,u0001,group1
```

This path of the authentication file can be passed into the API server service with the `--basic-auth-file` option.

If the API server is run as a pod (*static pod*), the above option is added to the `command` field in the YAML configuration file.

When accessing a cluster configured this way, the username and password are specified with the `-u` option, where the username and password are separated by a `:`. An example is shown below.

```bash
curl -v -k https://ip:6443/api/v1/pods -u "user:password"
```

#### Static Token File
Tokens can be also provided in a `.csv` file. Each entry contains a token, username, user ID, and, optionally, a user group.

```
KpjCVbI7rCFAHYPkByTIzRb7gu1cUc4B,user1,u0001,group1
```

A token file is specified with the `--token-auth-file` option.

Access to a cluster configured this way requires the `--header` option followed by the token in the following format: `"Authorization: Bearer <TOKEN>"`. An example is shown below.

```bash
curl -v -k https://ip:6443/api/v1/pods --header "Authorization: Bearer KpjCVbI7rCFAHYPkByTIzRb7gu1cUc4B"
```

### TLS Encryption
#### Certificates
A <span style = "color:lightblue">certificate</span> is used to guarantee trust between two parties during a transaction. It ensures that the parties are genuine entities, and data transferred in between the parties is <span style = "color:lightblue">encrypted</span> using an <span style = "color:lightblue">encryption key</span>.

In <span style = "color:lightblue">symmetric encryption</span>, the same encryption key is used to encrypt and decrypt data and **must also be sent over the network** (*the other party needs to read it as well*). This encryption method compromises the system.

In <span style = "color:lightblue">asymmetric encryption</span>, there is a pair of encryption keys: a <span style = "color:lightblue">private key</span> and a <span style = "color:lightblue">public key</span>. A public key is shown to everyone but can only be decrypted by the private key.

> [!INFO]
> The command `ssh-keygen` generates a pair of encryption keys.



## Authorization
^e8e0d8

There are several options for authorizing a connection.
- RBAC authorization
- ABAC authorization
- node authorization
- webhook mode


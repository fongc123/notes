# Imperative & Declarative
An <span style = "color:lightblue">imperative command</span> specifies the goal of a task and *how* to perform a task, while a <span style = "color:lightblue">declarative command</span> only specifies the goal of a task.

In Kubernetes, the `run`, `create`, `replace`, `delete`, `expose`, `edit`, `scale`, etc. commands are **imperative**, as these are manual commands that Kubernetes *how* to perform operations.

On the other hand, the `apply` command with a configuration file will automatically apply changes and allocate resources. The `apply` command will create an object if it doesn't exist and update an object otherwise.

> [!INFO]
> A **path** can be specified in the `apply` command to perform operations on **multiple files**.

Imperative commands are useful for completing small, one-time tasks, while declarative commands should be used most of the time.
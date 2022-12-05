A <span style = "color:lightblue">network</span> consists of a set of nodes and edges, where some connection between two or more nodes is represented by an edge (*see [[Graphs|visualizing network graphs]]*).

A highly researched example is the graph of social ties and rivalries in <span style = "color:lightblue">Zachary's karate club</span>.

![[ml-networks-zachary-karate.png|600]]

There are several properties when analyzing networks.
- size: the number of nodes or the number of edges
- <span style = "color:lightblue">degree of node</span>: the number of edges connected to a node
- <span style = "color:lightblue">shortest path</span>: the shortest path between two nodes (*all shortest paths can be averaged*)
- <span style = "color:lightblue">diameter</span>: the longest shortest path between two nodes (i.e., the shortest distance between two most distant nodes)
- <span style = "color:lightblue">node centrality</span>: rankings to identify the most **important** nodes
	- <span style = "color:lightblue">betweenness centrality</span>: the number of shortest paths that pass through a node (*similar for edges*)
	- <span style = "color:lightblue">eigenvalue centrality</span>: measure of influence of a node (e.g., Google's PageRank)

> [!INFO]
> The betweenness centrality of a node $v$ is given by the following expression.
> $$g(v)=\sum_{s\neq v\neq t}{\dfrac{\sigma_{st}(v)}{\sigma_{st}}}$$
> Here, $\sigma_{st}(v)$ represents the number of shortest paths that pass through node $v$ and $\sigma_{st}$ represents the total number of shortest paths from node $s$ to node $t$. 
> 
> In general, <span style = "color:lightblue">betweenness</span> refers to the constraint that some entities need to be **in between** others.

# Graph Representations
An <span style = "color:lightblue">adjacency matrix</span> displays connections in a tabular format. The value evaluates to $1$ if the connection is in the set of edges $E$ and $0$ otherwise.

$$
A=[a_{ij}]\quad\text{where}\space a_{ij}=\begin{dcases}
1 & \text{if}\space(v_i,v_j)\in E \\
0 & \text{if}\space(v_i,v_j)\notin E
\end{dcases}
$$

![[ml-networks-adjacency-matrix.png|600]]

The adjacency matrix uses $O(V^2)$ storage, where $V$ is the number of vertices.

> [!INFO]
> For an undirected graph (i.e., no arrows), the adjacency matrix is always symmetric.

Alternatively, an <span style = "color:lightblue">adjacency list</span> stores connections in a dictionary, where each dictionary value $Adj[u]$ is a linked list of all vertices $v$ that have connections to the node $u$.

![[ml-networks-adjacency-list.png|600]]

The adjacency list uses $O(V+E)$ storage, where $V$ is the number of vertices and $E$ is the number of edges.



> [!INFO]
> The total number of combinations can be calculated with the following formula.
> $$_nC_r=\dfrac{n!}{r!(n-r)!}$$
> For example, the number of combinations from picking $2$ out of $4$ items is $_4C_2$.


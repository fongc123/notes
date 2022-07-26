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

# Breadth-first Search
The <span style = "color:lightblue">breadth-first search (BFS)</span> algorithm traverses all nodes in the graph to reveal properties of a network. While traversing the graph, it keeps track of which nodes to explore next with a [[Stack & Queue|queue]].
- `color[u]`: the algorithm's progress on the node $u$ (*usually represented by color*)
	- `WHITE`: undiscovered
	- `GRAY`: discovered but not finished processing (*neighbors of $u$ not found yet*)
	- `BLACK`: finished processing
- `prev[u]`: the predecessor to node $u$
- `d[u]`: the **shortest** distance from the source to node $u$

First, each node $u$ is initialized as `WHITE` (i.e., undiscovered), and `pred[u] = NULL` (i.e., no predecessor).

```text
// visit each node (handles disconnected nodes as well)
foreach u in V do
	// start a new tree
	if color[u] = WHITE then
		visit(u);
	end
end

function visit(s):
	color[s] = GRAY; pred[s] = NULL; d[s] = 0;
	Q = 0; Enqueue(Q, s); // enqueue this node to the queue
	while len(Q) != 0 do
		u = Dequeue(Q);
		foreach v in Adj[u] do // iterate through neighbors of node u
			if color[v] = WHITE then // only continue if neighbor v is unvisited
				color[v] = GRAY;
				d[v] = d[u] + 1;
				pred[v] = u;
				Enqueue(Q, v);
			end
		end
		color[u] = BLACK; // complete processing after all neighbors discovered
	end
```

> [!INFO]
> The **shortest distance** will always be stored, as the closest neighbors to a node will be discovered first.

An example is shown below.

![[ml-networks-bfs.png|600]]

> [!INFO]
> In steps (c) and (d), notice that the distance from node $s$ to node $y$ is not $4$, as the queue ensures that node $x$ instead of node $u$ will discover node $y$.

The algorithm outputs the shortest distance from a source node to any other node, which can be viewed as a hierarchical structure.

# Girvan-Newman
The <span style = "color:lightblue">Girvan-Newman algorithm</span> identifies communities (i.e., groups) in an **undirected and unweighted** network by calculating the betweenness of each edge (i.e., <span style = "color:lightblue">edge betweenness</span> $\rightarrow$ the number of shortest paths passing through the edge).
1. Calculate **betweenness** of each edge.
2. Remove the edge with the highest betweenness. If two or more edges have the same highest score, all edges are removed.
3. Repeat until no edges are left.

> [!INFO]
> The betweenness of each edge is recalculated after every removal step.

An example is shown below.

![[ml-networks-girvan-newman-original.png|600]]

![[ml-networks-girvan-newman-steps.png|600]]

A [[Clustering#Hierarchical Clustering|hierarchical cluster]] can be created by observing the communities that are formed from removing edges.

## Calculating Betweenness
The [[#Breadth-first Search|breadth-first search (BFS)]] algorithm is used to calculate the **betweenness of each edge**.
1. Start at a node.
2. Count the **number of shortest paths** from the node to all other nodes.
3. Compute betweenness by working up the tree (i.e., starting from the furthest node and ending with the root node).
	1. Each node is given a credit of $1$.
	2. The **flow through each node** is equal to $1+\sum{\text{child edges}}$, where $1$ is the node's original credit.
	3. The flow is distributed to the parent node(s) proportional to each parent's value.
		1. **Example 1:** Since nodes $F$ and $G$ are parent nodes of node $I$ and have values of $2$ and $1$ respectively, node $I$ will give $\frac{2}{3}$ of its flow to node $F$ and $\frac{1}{3}$ of its flow to node $G$.
		2. **Example 2:** Since nodes $D$ and $E$ are parent nodes of node $H$ and have equal values, node $H$ will equally distribute its flow to both nodes $D$ and $E$.
4. Repeat steps 1-3 for each node in the network, obtaining an edge betweenness graph after each iteration.
5. For each edge in the original graph, sum up the flow values for the edge in each iteration and divide by two (*undirected*) to obtain the **edge betweenness**.

For example, the final betweenness value for the edge between $A$ and $B$ is the sum of all edge values of $A$ and $B$ in the graph originating at $A, B, \ldots, K$ divided by two.

$$\text{betweenness}_{AB}=\dfrac{\text{edge}_{AB}^{A}+\text{edge}^B_{AB}+\ldots+\text{edge}^K_{AB}}{2}$$

![[ml-networks-calculating-betweenness.jpg|600]]
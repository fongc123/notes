A <span style = "color:lightblue">network</span> consists of a set of nodes and edges, where some connection between two or more nodes is represented by an edge (*see [[Graphs|visualizing network graphs]]*).

A highly researched example is the graph of social ties and rivalries in <span style = "color:lightblue">Zachary's karate club</span>.

![[ml-networks-zachary-karate.png|600]]

There are several properties when analyzing networks.
- size: the number of nodes or the number of edges
- <span style = "color:lightblue">degree of node</span>: the number of edges connected to a node
- <span style = "color:lightblue">shortest path</span>: the shortest path between two nodes (*all shortest paths can be averaged*)
- <span style = "color:lightblue">diameter</span>: the longest shortest path between two nodes (i.e., the shortest distance between two most distant nodes)
- <span style = "color:lightblue">node centrality</span>: rankings to identify the most **important** nodes
	- <span style = "color:lightblue">betweenness centrality</span>: 

> [!INFO]
> The total number of combinations can be calculated with the following formula.
> $$_nC_r=\dfrac{n!}{r!(n-r)!}$$
> For example, the number of combinations from picking $2$ out of $4$ items is $_4C_2$.


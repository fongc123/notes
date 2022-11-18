<span style = "color:lightblue">Graphs</span> have been traditionally used to understand and solve problems, especially those with internal relationships. Because of their properties, graphs also have many mathematical tools for further analysis.

Graphs aim to **model relations in data**.
- <span style = "color:lightblue">node</span>: an entity with pre-defined properties
- <span style = "color:lightblue">edges</span>: connections between nodes
	- <span style = "color:lightblue">directed</span> or <span style = "color:lightblue">undirected</span>: indicate direction of connection 
	- <span style = "color:lightblue">binary</span> or <span style = "color:lightblue">weighted</span>: indicate strength of connection

Trees are **graphs with hierarchical structure**. A tree with $N$ nodes will have $N-1$ edges, where nodes are categorized as parent or child nodes.

> [!INFO]
> **Why $N-1$ edges?** The tree starts with $1$ node and $0$ edges. A new edge ($+1$) is added for every new node ($+1$).

Typical tasks for a graph representation are listed below.
- Count the number of nodes and edges.
- Calculate the **degree** for a node and the graph density.
- Count a separate group of nodes and find strong clusters.
- Locate a specific node or edge.
- Find neighboring nodes of a specific node.
- Compute the length of the path (*shortest?*) between two nodes.
- Compute **centrality** (e.g., betweenness centrality, closeness, centrality measures).

The graph should be represented clearly and easily.

> [!INFO]
> The <span style = "color:lightblue">degree</span> of a node is the number of edges that are connected to the node. Loops (i.e., edges that connect back to the originating node) count as $2$.

Common challenges in graph visualization are listed below.
- **Data size:** large datasets are difficult both computationally (*NP-complete algorithms*) and visually (*display clutter*)
- **Complex structure:** graphs cannot effectively display multidimensional data (*use color to encode dimensions*)
- **Cognitive issues:** the efficiency and efficacy of the visualization should be considered
- **Spatial layout:** how to properly arrange the nodes and edges?

# Designs
Graphs are normally represented with these idioms: node-link layouts, enclosure (nested) layouts, division (layered) layouts, matrix layouts, and three-dimensional layouts.

## Node-Link
A generic <span style = "color:lightblue">node-link</span> graph consists of a set of nodes and edges, where node positions are calculated and connecting lines are drawn for the edges. These elements are laid out on a two-dimensional space, where edge lengths are kept uniform and nodes are distributed uniformly.

|                           **Data**                            | **Mark** |           **Channels**           |             **Task**             | **Scalability** |
|:-------------------------------------------------------------:|:--------:|:--------------------------------:|:--------------------------------:|:---------------:|
| Generic graph |   Points (nodes) & lines (edges)   | Color, size | Understand relationships | More nodes and edges               |


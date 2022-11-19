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
Graphs are normally represented with these idioms: **node-link layouts**, **enclosure (nested) layouts**, **division (layered) layouts**, **matrix layouts**, and **three-dimensional layouts**.

Matrix layouts and three-dimensional layouts are additional representations of node-link or tree diagrams.

## Generic Node-Link
A <span style = "color:lightblue">generic node-link</span> graph consists of a set of nodes and edges, where node positions are calculated and connecting lines are drawn for the edges. These elements are laid out on a two-dimensional space, where edge lengths are kept uniform and nodes are distributed uniformly.

|                           **Data**                            | **Mark** |           **Channels**           |             **Task**             | **Scalability** |
|:-------------------------------------------------------------:|:--------:|:--------------------------------:|:--------------------------------:|:---------------:|
| Generic graph |   Points (nodes) & lines (edges)   | Color, size | Understand relationships | More nodes and edges               |

Node positions can be adjusted based on other layouts.
- <span style = "color:lightblue">spring layout</span>: edges are elastic springs and adjust node positions accordingly
	- Optimization algorithms: <span style = "color:lightblue">Newton-Raphson method</span>, <span style = "color:lightblue">simulated annealing method</span>, <span style = "color:lightblue">GEM method</span>, etc.
- <span style = "color:lightblue">force-directed layout</span>: nodes are charged particles, edges are elastic springs

Alternatively, node-link graphs can be implemented to summarize common connections with an **arc diagram**, **radial graph**, or **chord diagram**.

![[data-vis-chord-diagram.png|600]]

## Bipartite & Directed Acyclic Graphs
A <span style = "color:lightblue">bipartite graph</span> displays connections between <u>two</u> sets of nodes.

|                           **Data**                            | **Mark** |           **Channels**           |             **Task**             | **Scalability** |
|:-------------------------------------------------------------:|:--------:|:--------------------------------:|:--------------------------------:|:---------------:|
| Bipartite graph |   Points (nodes) & lines (edges)   | Color, size | Illustration of two groups | More nodes and edges               |

A <span style = "color:lightblue">Sankey diagram</span> is a <span style = "color:lightblue">directed acyclic graph (DAG)</span> that consists of **a sequence of bipartite graphs**. It identifies composition and matches between attributes.

![[data-vis-sankey-diagram.png|600]]

## Tree
An <span style = "color:lightblue">indented tree layout</span> places items along rows, where indentation is used to show parent-child relationships. Alternatively, a [[Multivariate Data#Layout Density|dendrogram]] (*cluster dendrogram*) can be used to display hierarchical clustering relationships.

A <span style = "color:lightblue">radial tree layout</span> places items radially around an origin, where the radius of an item encodes depth. The example below displays a cluster dendrogram with a radial tree layout.

![[data-vis-radial-tree-cluster-dendrogram.png|600]]

A <span style = "color:lightblue">balloon tree</span> is a node-link diagram in polar coordinates, where each subtree (i.e., cluster) is enclosed in a circular area.

![[data-vis-balloon-tree.png|600]]

## Nested (Enclosure) Layout
A <span style = "color:lightblue">nested or enclosure layout</span> displays items in a spatial enclosure (i.e., nodes $\rightarrow$ rectangles), where child nodes are placed within their parent node.

| **Data** | **Mark** | **Channels** |        **Task**        |   **Scalability**    |
|:--------:|:--------:|:------------:|:----------------------:|:--------------------:|
|   Tree   |   Area   | Color, size  | Understand composition | More areas |

This visualization is also known as a <span style = "color:lightblue">tree map</span>.

![[data-vis-tree-map.png|600]]

Alternatively, a <span style = "color:lightblue">Voronoi treemap</span> displays items as arbitrary polygonal shapes and boundaries. Iterative and weighted Voronoi tessellations are used to achieve cell areas proportional to values.

A <span style = "color:lightblue">radial treemap</span> displays nodes as circles, where child nodes are nested inside larger parent nodes.

## Division (Layered) Layout
A <span style = "color:lightblue">division or layered layout</span> involves the recursive subdivision of space. Unlike [[#Nested (Enclosure) Layout|nested layouts]], where nodes are nested in each other, child nodes are **attached** to parent nodes.

| **Data** | **Mark** | **Channels** |        **Task**        |   **Scalability**    |
|:--------:|:--------:|:------------:|:----------------------:|:--------------------:|
|   Tree   |   Area   | Color, size  | Understand composition | Layering, adjacency, alignment |

A <span style = "color:lightblue">sunburst tree layout</span> displays items and compositions radially.

![[data-vis-sunburst.png|600]]

> [!WARNING]
> Both [[#Division (Layered) Layout|division layouts]] and [[#Nested (Enclosure) Layout|nested layouts]] suffer from an inefficient use of space.

# Visual Clutter Reduction
As the data size increases, visual clutter can become a major issue.
- <span style = "color:lightblue">edge-centric</span>: adjust representation of edges
	- <span style = "color:lightblue">confluent drawings</span>: group intersection points together
	- <span style = "color:lightblue">flow map</span>: group edges by a single-source flow as a free-style binary tree structure
	- <span style = "color:lightblue">edge bundling</span>: group edges together into thicker edges
- <span style = "color:lightblue">node-centric</span>: content-based clustering (e.g., divide structure into sub-graphs)
- <span style = "color:lightblue">appearance-centric</span>: sampling or filtering

> [!WARNING]
> Node-centric visual clutter reduction approaches cause a loss of detail.

Animations can also aid in reducing visual clutter.
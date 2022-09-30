# Decision Tree
A <span style = "color:lightblue">decision tree</span> (*decision tree learning*) is a supervised learning approach. It performs classification (*or regression*) by using a decision tree to create a predictive model, where each <span style = "color:lightblue">internal node</span> represents a test on an attribute, each <span style = "color:lightblue">branch</span> represents an attribute value (i.e., outcome of the test), and each <span style = "color:lightblue">leaf node</span> represents a class label.

The associated class of a new object can be predicted by **testing the attribute values against a decision tree.** A path starting from the root node is traced top-down to a leaf node (i.e., class label).

![[ml-decision-tree.png|600]]

## Creation
Decision tree induction algorithms are <span style = "color:lightblue">top-down</span> and <span style = "color:lightblue">recursive</span>. Some examples include <span style = "color:lightblue">ID3</span>, <span style = "color:lightblue">C4.5</span>, and <span style = "color:lightblue">CART</span>. The majority of the algorithms are <span style = "color:lightblue">greedy</span>.

The steps of the creation of a decision tree are outlined below.
1. Confirm inputs (e.g., nodes, training set, attribute list, attribute selection method) of the tree creation process.
2. If one of the <span style = "color:lightblue">terminating conditions</span> is satisfied, terminate the process.
3. At each node, use a <span style = "color:lightblue">splitting criterion</span> to best partition the original dataset into subsets $D_i$ such that each subset is as <span style = "color:lightblue">pure</span> as possible (*see [[#Purity Entropy|Purity]]*).
4. Create new branches $i$ and nodes $N_i$ for each outcome of the splitting criterion, where node $N_i$ is associated with subset $D_i$.
5. Remove the splitting attribute $A$ from the attribute list.
6. Recursively call the process for every newly created $(N_i,D_i)$ pair.



## Attribute Selection

### Purity & Entropy


### Information Gain

### Gain Ratio

### Gini Index

## Over-fitting
Some methods to prevent over-fitting in decision trees are listed below.

### Early-Stopping
Extra <span style = "color:lightblue">terminating conditions</span> can be added to the decision tree algorithm, where the induction process is stopped if the number of tuples is fewer than a user-specified threshold.

However, selection of an appropriate threshold may be challenging.

### Pruning
The subtree rooted at a node is removed.
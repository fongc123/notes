# Decision Tree
A <span style = "color:lightblue">decision tree</span> (*decision tree learning*) is a supervised learning approach. It performs classification (*or regression*) by using a decision tree to create a predictive model, where each <span style = "color:lightblue">internal node</span> represents a test on an attribute, each <span style = "color:lightblue">branch</span> represents an attribute value (i.e., outcome of the test), and each <span style = "color:lightblue">leaf node</span> represents a class label.

The associated class of a new object can be predicted by **testing the attribute values against a decision tree.** A path starting from the root node is traced top-down to a leaf node (i.e., class label).

![[ml-decision-tree.png|600]]

## Creation
Decision tree algorithms include <span style = "color:lightblue">ID3</span>, <span style = "color:lightblue">C4.5</span>, and <span style = "color:lightblue">CART</span>. The majority of the algorithms are <span style = "color:lightblue">greedy</span>. 

> [!INFO]
> A <span style = "color:lightblue">greedy algorithm</span> makes the locally optimal choice at each stage but does not consider a globally optimal solution. However, a greedy heuristic can yield locally optimal solutions that approximate a globally optimal solution in a reasonable amount of time.


## Attribute Selection

### Purity & Entropy


### Information Gain

### Gain Ratio


### Gini Index


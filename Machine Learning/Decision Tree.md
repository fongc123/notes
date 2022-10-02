# Decision Tree
A <span style = "color:lightblue">decision tree</span> (*decision tree learning*) is a supervised learning approach. It performs classification (*or regression*) by using a decision tree to create a predictive model, where each <span style = "color:lightblue">internal node</span> represents a test on an attribute, each <span style = "color:lightblue">branch</span> represents an attribute value (i.e., outcome of the test), and each <span style = "color:lightblue">leaf node</span> represents a class label.

The associated class of a new object can be predicted by **testing the attribute values against a decision tree.** A path starting from the root node is traced top-down to a leaf node (i.e., class label).

![[ml-decision-tree.png|600]]

## Creation
Decision tree induction algorithms are <span style = "color:lightblue">top-down</span>, <span style = "color:lightblue">recursive</span>, and mostly <span style = "color:lightblue">greedy</span>. Some examples include <span style = "color:lightblue">ID3</span>, <span style = "color:lightblue">C4.5</span>, and <span style = "color:lightblue">CART</span>.

The steps of the creation of a decision tree are outlined below.
1. Confirm inputs (e.g., nodes, training set, attribute list, attribute selection method) of the tree creation process.
2. If one of the <span style = "color:lightblue">terminating conditions</span> is satisfied, terminate the process (*see [[#Terminating Conditions]]*).
3. At each node, use a <span style = "color:lightblue">splitting criterion</span> to best partition the original dataset into subsets $D_i$ such that each subset is as <span style = "color:lightblue">pure</span> as possible (*see [[#Purity Entropy|Purity]]*).
4. Create new branches $i$ and nodes $N_i$ for each outcome of the splitting criterion, where node $N_i$ is associated with subset $D_i$.
5. Remove the splitting attribute $A$ from the attribute list.
6. Recursively call the process for every newly created $(N_i,D_i)$ pair.

> [!INFO]
> Each subset $D_i$ contains tuples that satisfy the splitting criterion outcome of branch $i$. Examples of attribute criterion are listed below.
> - discrete-valued (e.g., $A=a_1$ or $A=a_2$)
> - continuous-valued (e.g., $A\leq \text{threshold}$)
> - discrete-valued and binary (e.g., $A\in \{\text{red},\text{green}\}$)

## Terminating Conditions
The [[#Creation|creation process]] is terminated if any of the statements below are valid.
1. All the tuples in partition $D$ belong to the same attribute (e.g., all tuples belong to attribute $A$).
2. There are no remaining attributes in the attribute list to help partition the tuples of $D$ further.
3. The partition $D$ is empty.

In the first condition, the node becomes a leaf and is labeled with the associated class. However, the node in the second and third condition is labeled with the **majority class of the partition** and the **majority class of the parent partition** respectively.

## Attribute Selection
Ideally, an attribute selection criterion that creates partitions that consist only of tuples with a <u>single</u> class is desired (i.e., **pure** datasets).

However, it is not always possible. A **ranking algorithm** for each attribute is done instead, where the attribute with the **best score** is selected.

### Purity & Entropy
<span style = "color:lightblue">Purity</span> refers to the composition (or uncertainty) of attributes.

>[!INFO]
>For example, in a dataset of training samples $D$ with two discrete classes $A$ and $B$, <span style = "color:lightblue">optimal purity</span> is achieved when the proportion of each class is either $0$ or $1$. A sample where both classes have equal proportions at $0.5$ is <span style = "color:lightblue">least pure</span>.
> - $p_A=0\quad\text{and}\quad p_B=1$ (optimal)
> - $p_A=1\quad\text{and}\quad p_B=0$ (optimal)
> - $p_A=0.5\quad\text{and}\quad p_B=0.5$ (least pure)

This can be summarized with an <span style = "color:lightblue">entropy curve</span>, where its values range between $0$ (*no entropy*) and $\log_2{m}$ (*maximum entropy*).

$$
\begin{gather}
Entropy(D)=-p_A\log_b{p_A}-p_B\log_b{p_B}\quad\Tiny\text{(two values)} \newline \newline
Entropy(D)=\sum_{i=1}^{m}{-p_i\log_2{p_i}\quad\Tiny\text{(general)}}
\end{gather}
$$

The <span style = "color:lightblue">units</span> that entropy is measured in is controlled by the value of $b$.
- <span style = "color:lightblue">nats</span>: $b\rightarrow e$
- <span style = "color:lightblue">bits</span>: $b\rightarrow 2$ (*this is used in machine learning*)

<span style = "color:lightblue">Continuous-valued attributes</span> (e.g., temperature) are discretized, and a Boolean attribute is created, where it evaluates to true if the attribute value is greater than a threshold $c$ and false otherwise.

$$A_c<c$$

The set of candidate thresholds are the midway segregation point between attribute values. The value of $c$ is determined by the information gain.

### Information Gain
The <span style = "color:lightblue">information gain</span> of $D$ relative to attribute $A$ is the expected **reduction** in entropy caused by knowing the value of $A$. The set of examples in $D$ where attribute $A$ has value $v$ is represented by $D_v$. It is a selection measure used in the ID3 decision tree induction algorithm.

$$Gain(D,A)=Entropy(D)-\sum_{v}{\frac{|D_v|}{|D|}}Entropy(D_v)$$

**The attribute that generates the maximum information gain is desired.**

### Gain Ratio
Information gain is **biased** toward tests with many outcomes. These attributes (e.g., student ID) create perfect entropy and should be penalized.

$$SplitInfo_A(D)=-\sum_{j=1}^{v}{\frac{|D_j|}{|D|}\log_2{\frac{|D_j|}{|D|}}}$$

### Gini Index
The <span style = "color:lightblue">Gini index</span> is another attribute selection method.

## Over-fitting
Some methods to prevent over-fitting in decision trees are listed below.

### Early-Stopping
Extra <span style = "color:lightblue">terminating conditions</span> can be added to the decision tree algorithm, where the induction process is stopped if the number of tuples is fewer than a user-specified threshold.

However, selection of an appropriate threshold may be challenging.

### Pruning
The subtree rooted at a node is removed.
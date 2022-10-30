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

In the first condition, nodes become leaves and are labeled with the associated class. However, nodes with the second and third condition are labeled with the **majority class of the partition** and the **majority class of the parent partition** respectively.

## Attribute Selection
Ideally, an attribute selection criterion that creates partitions that consist only of data entries with only a <u>single</u> class is desired (i.e., **pure** datasets).

However, it is not always possible. A **ranking algorithm** for each attribute is done instead, where the attribute with the **best score** is selected.

### Purity & Entropy
<span style = "color:lightblue">Purity</span> refers to the composition (or uncertainty) of attributes.

>[!INFO]
>For example, in a dataset of training samples $D$ with two discrete class labels $A$ and $B$, <span style = "color:lightblue">optimal purity</span> is achieved when the proportion of each class is either $0$ or $1$. A sample where both classes have equal proportions at $0.5$ is <span style = "color:lightblue">least pure</span>.
> - $p_A=0\quad\text{and}\quad p_B=1$ (optimal)
> - $p_A=1\quad\text{and}\quad p_B=0$ (optimal)
> - $p_A=0.5\quad\text{and}\quad p_B=0.5$ (least pure)

This can be represented by an <span style = "color:lightblue">entropy curve</span>, where its values range between $0$ (*no entropy*) and $\log_2{m}$ (*maximum entropy*) for $m$ different class labels.

$$
\begin{gather}
Entropy(D)=-p_A\log_b{p_A}-p_B\log_b{p_B}\quad\small\text{(two values)} \newline \newline
Entropy(D)=\sum_{i=1}^{m}{-p_i\log_b{p_i}\quad\small\text{(general)}}
\end{gather}
$$

The <span style = "color:lightblue">units</span> that entropy is measured in is controlled by the value of $b$.
- <span style = "color:lightblue">nats</span>: $b\rightarrow e$
- <span style = "color:lightblue">bits</span>: $b\rightarrow 2$ (*this is used in machine learning*)

### Information Gain
The <span style = "color:lightblue">information gain</span> of a subset $D$ relative to attribute $A$ is the expected **reduction** in entropy caused by knowing the value of $A$. The set of examples in $D$ where attribute $A$ has value $v$ is represented by $D_v$. It is a selection measure used in the ID3 decision tree induction algorithm.

$$Gain(D,A)=Entropy(D)-\sum_{v}{\frac{|D_v|}{|D|}}Entropy(D_v)$$

**The attribute that generates the maximum information gain is selected.**

#### Continuous-valued Attributes
<span style = "color:lightblue">Continuous-valued attributes</span> (e.g., temperature) are discretized, and a Boolean criterion is created. It evaluates to true if the attribute value is greater than a threshold $c$ and false otherwise.

$$A_c<c$$

The set of candidate thresholds are the **midway segregation point** (criterion) between attribute values, where there are a total of $m-1$ thresholds. The value of $c$ is determined by the information gain.

#### Example Calculation
A sample calculation for determining the attribute with the highest information gain is demonstrated. The training dataset table is shown below. Here, there exists only two class labels: `yes` and `no`.

| **RID** |   **Age**   | **Income** | **Student** | **Credit Rating** | <span style = "color:lightcoral"><b>Class: Buys computer?</b></span> |
|:-------:|:-----------:|:----------:|:-----------:|:-----------------:|:--------------------------------------------------------------------:|
|    1    |    youth    |    high    |     no      |       fair        |                                  no                                  |
|    2    |    youth    |    high    |     no      |     excellent     |                                  no                                  |
|    3    | middle_aged |    high    |     no      |       fair        |                                 yes                                  |
|    4    |   senior    |   medium   |     no      |       fair        |                                 yes                                  |
|    5    |   senior    |    low     |     yes     |       fair        |                                 yes                                  |
|    6    |   senior    |    low     |     yes     |     excellent     |                                 no                                  |
|    7    | middle_aged |    low     |     yes     |     excellent     |                                 yes                                  |
|    8    |    youth    |   medium   |     no      |       fair        |                                  no                                  |
|    9    |    youth    |    low     |     yes     |       fair        |                                 yes                                  |
|   10    |   senior    |   medium   |     yes     |       fair        |                                 yes                                  |
|   11    |    youth    |   medium   |     yes     |     excellent     |                                 yes                                  |
|   12    | middle_aged |   medium   |     no      |     excellent     |                                 yes                                  |
|   13    | middle_aged |    high    |     yes     |       fair        |                                 yes                                  |
|   14    |   senior    |   medium   |     no      |     excellent     | no                                                                     |

The entropy of the entire dataset $D$ is given as $0.940$ (?). The information gain for the `age` attribute $Gain(D, A=\text{age})$ is first calculated.

$$Gain(D,A=\text{age})=Entropy(D)-\sum_{v}{\frac{|D_v|}{|D|}Entropy(D_v)}$$

The `age` attribute can take **three** different values: `youth`, `middle_aged`, and `senior`. 
First, the entropy of the subset where age is equal to `youth` is calculated.

| **RID** | **Age** | **Income** | **Student** | **Credit Rating** | <span style = "color:lightcoral"><b>Class: Buys computer?</b></span> |
|:-------:|:-------:|:----------:|:-----------:|:-----------------:|:--------------------------------------------------------------------:|
|    1    |  youth  |    high    |     no      |       fair        |                                  no                                  |
|    2    |  youth  |    high    |     no      |     excellent     |                                  no                                  |
|    8    |  youth  |   medium   |     no      |       fair        |                                  no                                  |
|    9    |  youth  |    low     |     yes     |       fair        |                                 yes                                  |
|   11    |  youth  |   medium   |     yes     |     excellent     |                                 yes                                  |

In the `youth` subset, there are three data entries with the `no` class label and two entries with the `yes` class label. Thus, $p_{\text{no}}=0.6$ and $p_{\text{yes}}=0.4$.

$$
\begin{align}
	Entropy(D_{\text{youth}}) & =-\frac{2}{5}\log_2\left(\frac{2}{5}\right)-\frac{3}{5}\log_2\left(\frac{3}{5}\right) \newline
	Entropy(D_{\text{youth}}) & =0.971
\end{align}
$$

As expected, this subset has high entropy (i.e., high uncertainty). Next, the entropy of the subset where age is equal to `middle_aged` is calculated.

| **RID** |   **Age**   | **Income** | **Student** | **Credit Rating** | <span style = "color:lightcoral"><b>Class: Buys computer?</b></span> |
|:-------:|:-----------:|:----------:|:-----------:|:-----------------:|:--------------------------------------------------------------------:|
|    3    | middle_aged |    high    |     no      |       fair        |                                 yes                                  |
|    7    | middle_aged |    low     |     yes     |     excellent     |                                  yes                                  |
|   12    | middle_aged |   medium   |     no      |     excellent     |                                 yes                                  |
|   13    | middle_aged |    high    |     yes     |       fair        | yes                                                                     |

In the `middle_aged` subset, all four data entries have the `yes` class label. Thus, $p_{\text{no}}=0$ and $p_{\text{yes}}=1$.

$$
\begin{align}
	Entropy(D_{\text{middle\_aged}})&=-\frac{4}{4}\log_2\left(\frac{4}{4}\right) \newline
	Entropy(D_{\text{middle\_aged}})&=0
\end{align}
$$

This subset has low entropy (i.e., low uncertainty). Lastly, the entropy of the subset where age is equal to `senior` is calculated.

| **RID** | **Age** | **Income** | **Student** | **Credit Rating** | <span style = "color:lightcoral"><b>Class: Buys computer?</b></span> |
|:-------:|:-------:|:----------:|:-----------:|:-----------------:|:--------------------------------------------------------------------:|
|    4    | senior  |   medium   |     no      |       fair        |                                 yes                                  |
|    5    | senior  |    low     |     yes     |       fair        |                                 yes                                  |
|    6    | senior  |    low     |     yes     |     excellent     |                                  no                                  |
|   10    | senior  |   medium   |     yes     |       fair        |                                 yes                                  |
|   14    | senior  |   medium   |     no      |     excellent     | no                                                                     |

In the `senior` subset, there are two entries with the `no` class label and three entries with the `yes` class label. Thus,  $p_{\text{no}}=0.4$ and $p_{\text{yes}}=0.6$.

$$
\begin{align}
	Entropy(D_{\text{senior}}) & =-\frac{3}{5}\log_2\left(\frac{3}{5}\right)-\frac{2}{5}\log_2\left(\frac{2}{5}\right) \newline
	Entropy(D_{\text{senior}}) & =0.971
\end{align}
$$
A **weighted average** of the entropy values of each subset ($D_{\text{youth}}$, $D_{\text{middle\_aged}}$, and $D_{\text{senior}}$) and their subset sizes is calculated.

$$
\begin{align}
	Gain(D,A=\text{age})&=Entropy(D)-\sum_{v}{\frac{|D_v|}{|D|}Entropy(D_v)} \newline
	&=0.94-\left[\frac{5}{14}(0.971)+\frac{4}{14}(0)+\frac{5}{14}(0.971)\right] \newline
	Gain(D,A=\text{age})&=0.694
\end{align}
$$

The process is repeated for the other attributes, namely `income`, `student`, and `credit_rating`.

$$
\begin{gather}
	Gain(D,A=\text{income})=0.029 \newline
	Gain(D,A=\text{student})=0.151 \newline
	Gain(D,A=\text{credit\_rating})=0.048
\end{gather}
$$

Since the information gain for the `age` attribute has the highest value of $0.694$ among all the attributes, **the `age` attribute is selected**.

> [!WARNING]
> The information gain is **biased** towards tests with many outcomes. For example, if the data was partitioned based on a unique identifier (e.g., `product_id`), there would be many partitions, where each partition would have <u>one</u> entry. **The entropy after splitting would evaluate to $0$**. *See [[#Gain Ratio|gain ratio]] for countermeasures*.

### Gain Ratio
The <span style = "color:lightblue">gain ratio</span> is an extension of information gain, where an attribute that creates many partitions is penalized. The penalty should be (1) large when data is evenly spread and (2) small when all data belong to one branch.

The expression for the split info is shown below, where $v$ represents distinct values of an attribute $A$.
$$
\begin{gather}
	SplitInfo_A(D) =-\sum_{j=1}^{v}{\frac{|D_j|}{|D|}\times\log_2{\frac{|D_j|}{|D|}}} \newline
	GainRatio(A)=\frac{Gain(A)}{SplitInfo_A(D)} 
\end{gather}
$$

**The attribute that generates the maximum gain ratio is selected.**

#### Example Calculation
A sample calculation for the gain ratio of the `credit_rating` attribute is demonstrated. Again, the training dataset table is shown below.

| **RID** |   **Age**   | **Income** | **Student** | **Credit Rating** | <span style = "color:lightcoral"><b>Class: Buys computer?</b></span> |
|:-------:|:-----------:|:----------:|:-----------:|:-----------------:|:--------------------------------------------------------------------:|
|    1    |    youth    |    high    |     no      |       fair        |                                  no                                  |
|    2    |    youth    |    high    |     no      |     excellent     |                                  no                                  |
|    3    | middle_aged |    high    |     no      |       fair        |                                 yes                                  |
|    4    |   senior    |   medium   |     no      |       fair        |                                 yes                                  |
|    5    |   senior    |    low     |     yes     |       fair        |                                 yes                                  |
|    6    |   senior    |    low     |     yes     |     excellent     |                                 no                                  |
|    7    | middle_aged |    low     |     yes     |     excellent     |                                 yes                                  |
|    8    |    youth    |   medium   |     no      |       fair        |                                  no                                  |
|    9    |    youth    |    low     |     yes     |       fair        |                                 yes                                  |
|   10    |   senior    |   medium   |     yes     |       fair        |                                 yes                                  |
|   11    |    youth    |   medium   |     yes     |     excellent     |                                 yes                                  |
|   12    | middle_aged |   medium   |     no      |     excellent     |                                 yes                                  |
|   13    | middle_aged |    high    |     yes     |       fair        |                                 yes                                  |
|   14    |   senior    |   medium   |     no      |     excellent     | no                                                                     |

The `credit_rating` attribute can take **two** different values: `fair` and `excellent`, where the size of $D_{\text{fair}}$ is $8$ and the size of $D_{\text{excellent}}$ is $6$. Thus, the split info is calculated.

$$
\begin{align}
	SplitInfo_A(D)&=-\sum_{j=1}^{v}{\frac{|D_j|}{|D|}\times\log_2{\frac{|D_j|}{|D|}}} \newline
	&=-\frac{8}{14}\log_2\left(\frac{8}{14}\right)-\frac{6}{14}\log_2\left(\frac{6}{14}\right) \newline
	SplitInfo_A(D)&=0.985
\end{align}
$$
The information gain of the `credit_rating` attribute is $0.048$ (*see [[#Information Gain#Example Calculation|how to calculate information gain]]*). Thus, the gain ratio is calculated.

$$
\begin{align}
GainRatio(A)&=\frac{0.048}{0.985}\newline
GainRatio(A)&=0.048
\end{align}
$$
Since the attribute only creates two partitions, the gain ratio is similar to the information gain.

### Gini Index
The <span style = "color:lightblue">Gini index</span> is another attribute selection method. Its expression is shown below, where $p_i$ is the probability that an entry of a dataset $D$ belongs to a class label $C_i$. 

$$
\begin{gather}
	Gini(D)=1-\sum_{i=1}^{m}p_i^2\newline\newline
	\text{where }p_i=\frac{|C_i|}{|D|}
\end{gather}	
$$

> [!INFO]
> The Gini index $Gini(D)$ is small if most of the entries belong to a few classes.

The Gini index of the splitting of the dataset by an attribute $A$ into $n$ subsets is defined as the following.

$$Gini_A(D)=\sum_{i=1}^{n}{\frac{|D_i|}{|D|}Gini(D_i)}$$

The reduction in impurity is the difference between the Gini index of the parent dataset and that of the attribute dataset.

$$\Delta Gini(A)=Gini(D)-Gini_A(D)$$

**The attribute that generates the greatest difference is selected.**

## Over-fitting
Some methods to prevent over-fitting in decision trees are listed below.

### Early-Stopping
Extra <span style = "color:lightblue">terminating conditions</span> can be added to the decision tree algorithm, where the induction process is stopped if the number of tuples is fewer than a user-specified threshold.

However, selection of an appropriate threshold may be challenging.

### Pruning
The subtree rooted at a node is removed, turning the node into a leaf node.

In each iteration, the node that improves the validation set accuracy **the most** is removed (*see [[ML Basics|greedy algorithms]]*).

The pruning process continues until the pruned tree performs worse than the unpruned tree **on the validation set**.

> [!INFO]
> A pruned decision tree misclassifies more training examples than an unpruned tree.


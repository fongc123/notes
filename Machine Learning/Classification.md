# Classification

A classification model (a <span style = "color:lightblue">classifier</span>) takes as input <span style = "color:lightblue">non-class attribute values</span> and returns a <span style = "color:lightblue">class value</span>. lassification algorithms include **decision tree**, **rule-based**, **Bayesian**, **neural networks**, **support vector machines (SVM)**, and ***k*-nearest neighbors (KNN)**.

## Binary Classification

<span style = "color:lightblue">Binary classification</span> can be expressed as a linear combination of inputs $x$ and weights $w$ with a bias $b$.

$$
a = w_1x_1+w_2x_2+b
$$

A value of $a$ greater than $0$ corresponds to one class, while that of less than $0$ corresponds to the other. It can be visualized as a <span style = "color:lightblue">step function</span> $u(a)$ or <span style = "color:lightblue">sigmoid function</span> $\sigma(a)$, which is designed to output either $0$ or $1$. Normally, it is expressed as a probability of whether the object belongs to the class (i.e., true or false).

$$
p(y=1|x) = \sigma(w^Tx+b)=\sigma(\sum_{d-1}^{D}w_dx_d+b)
$$

> [!INFO]
> This model is referred to as <span style = "color:lightblue">logistic regression</span>, as a sigmoid function is also referred to as a logistic function.

## Cross-entropy Loss

In **binary** classification, a <span style = "color:lightblue">binary cross-entropy loss</span> is used instead.

## Decision Tree
A <span style = "color:lightblue">decision tree</span> represents the classification of an object, where each <span style = "color:lightblue">internal node</span> represents an attribute, each <span style = "color:lightblue">branch</span> represents an outcome, and each <span style = "color:lightblue">leaf node</span> holds a class label.

### Purity & Entropy
Attributes that split examples into sets that are relatively **pure** in one label are desired. <span style = "color:lightblue">Purity</span> refers to the composition (or uncertainty) of labels. For example, in a dataset $D$ with two discrete classes $A$ and $B$, <span style = "color:lightblue">optimal purity</span> is achieved when the proportion of each class is either $0$ or $1$. A sample where both classes have equal proportions at $0.5$ is <span style = "color:lightblue">least pure</span>.
- $D$: a sample of training samples
- $p_A=0\quad\text{and}\quad p_B=1$ (optimal)
- $p_A=1\quad\text{and}\quad p_B=0$ (optimal)
- $p_A=0.5\quad\text{and}\quad p_B=0.5$ (least pure)

This can be summarized with an <span style = "color:lightblue">entropy curve</span>, where its values range between $0$ (*no entropy*) and $\log_2{m}$ (*maximum entropy*).

$$
\begin{gather}
Entropy(D)=-p_A\log_b{p_A}-p_B\log_b{p_B}\quad\Tiny\text{(two values)} \newline \newline
Entropy(D)=\sum_{i=1}^{m}{-p_i\log_2{p_i}\quad\Tiny\text{(general)}}
\end{gather}
$$

The <span style = "color:lightblue">units</span> that entropy is measured in is controlled by the value of $b$.
- <span style = "color:lightblue">nats</span>: $b\rightarrow e$
- <span style = "color:lightblue">bits</span>: $b\rightarrow 2$ (*this is used in classification*)

The <span style = "color:lightblue">information gain</span> of $D$ relative to attribute $A$ is the expected **reduction** in entropy caused by knowing the value of $A$. The set of examples in $D$ where attribute $A$ has value $v$ is represented by $D_v$.

$$Gain(D,A)=Entropy(D)-\sum_{v}{\frac{|D_v|}{|D|}}Entropy(D_v)$$

**The attribute that generates the maximum information gain is desired.**

For <span style = "color:lightblue">continuous-valued attributes</span> (e.g., temperature), they are discretized, and a Boolean attribute is created, where it evaluates to true if the attribute value is greater than a threshold $c$ and false otherwise.

$$A_c<c$$

The set of candidate thresholds are the midway segregation point between attribute values. The value of $c$ is determined by the information gain.

### Gain Ratio
Information gain is **biased** toward tests with many outcomes. These attributes (e.g., student ID) create perfect entropy and should be penalized.

$$SplitInfo_A(D)=-\sum_{j=1}^{v}{\frac{|D_j|}{|D|}\log_2{\frac{|D_j|}{|D|}}}$$
### Gini Index
The <span style = "color:lightblue">Gini index</span> is another attribute selection method.

## Model Performance

A <span style = "color:lightblue">confusion matrix</span> is a tool to analyze how well a classifier can recognize tuples of different classes.

![[ml-confusion-matrix.png|600]]

Alternatively, other accuracy measures include sensitivity and specificity. <span style = "color:lightblue">Precision</span> is the fraction of correctly predicted classes (true positives; retrieved and relevant documents) out of all data points (true positives and false positives; all documents).

$$\text{precision}=\frac{\text{TP}}{\text{TP}+\text{FP}}$$

<span style = "color:lightblue">Recall</span> is the fraction of correctly predicted classes (true positives) out of all <u>class</u> data points (true positives and false negatives; all <u>relevant</u> documents).

$$\text{recall}=\frac{\text{TP}}{\text{TP}+\text{FN}}$$

An ideal system maximizes both precision and recall values; however, there is a trade-off between precision and recall. To increase precision, a small number of data points is predicted to increase the chance of a correct classification. To increase recall, a large number of data points is predicted to increase the number of class-specific data points evaluated.

The <span style = "color:lightblue">F-measure</span> is the harmonic mean which can be calculated with precision and recall values.

$$\text{F-measure}=\frac{2\times \text{recall}\times\text{precision}}{\text{recall}+\text{precision}}$$

For a general accuracy indicator, the <span style = "color:lightblue">accuracy</span> can be calculated as shown below.

$$\text{accuracy}=\frac{\text{TP}+\text{TN}}{\text{TP}+\text{TN}+\text{FP}+\text{FN}}$$
### $k$-Fold Cross-validation
In the <span style = "color:lightblue">holdout method</span>, a dataset $D$ is partitioned into two disjoint datasets $D_1$ and $D_2$. The larger dataset is used for the training set, and the smaller for the validation set.

> [!INFO]
> Typically, the size of $D_1$ is two thirds of the original, while the size of $D_2$ is one third of the original.

A <span style = "color:lightblue">k-fold cross-validation</span> partitions the original dataset into $k$ disjoint datasets and repeats the holdout method $k$ times. A new classifier is created for each iteration, and **the average of the classifier accuracies is the overall accuracy estimate**.

![[ml-cross-validation.png|400]]

> [!INFO]
> In each iteration $i$, the dataset $D_i$ size of $\frac{1}{k}|D|$ is selected as the test set, while the remaining datasets with size of$(1-\frac{1}{k})|D|$ is selected as the training set. Typically, a value of $k$ equal to $10$ is considered reasonable.

The <span style = "color:lightblue">leave-one-out cross-validation</span> is useful for small datasets, where $k$ is equal to the size of the original dataset. Here, training is done on $|D|-1$ examples, and validation is done on $1$ example.

To ensure that each class has approximately equal proportions in both the training and validation sets, <span style = "color:lightblue">k-fold stratified cross-validation</span> is done instead. Here, the original dataset is partitioned into $k$ folds such that **each class is uniformly distributed among all the folds**.

> [!INFO]
> In $k$-fold stratified cross-validation, the class distribution in each fold should be similar to that in the original dataset.

## Over-fitting
An <span style = "color:lightblue">over-fitted</span> model is **more complex** than an original model, where the over-fitted model will fit noisy data better than an original model.

Special anomalies may have been incorporated into the model. This affects the accuracy of the model on the test set.

### Early-Stopping
<span style = "color:lightblue">Extra terminating conditions</span> can be added to the decision tree algorithm, where the induction process is stopped if the number of tuples is fewer than a user-specified threshold.

> [!INFO]
> Selection of an appropriate threshold may be challenging.

### Pruning
The subtree rooted at a node is removed.

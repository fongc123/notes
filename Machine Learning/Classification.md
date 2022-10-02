# Classification

A classification model (a <span style = "color:lightblue">classifier</span>) takes as input <span style = "color:lightblue">non-class attribute values</span> and returns a <span style = "color:lightblue">class value</span>. Classification algorithms include [[Decision Tree|decision trees]], **rule-based**, **Bayesian**, **neural networks**, **support vector machines (SVM)**, and ***k*-nearest neighbors (KNN)**.

## Binary Classification

<span style = "color:lightblue">Binary classification</span> can be expressed as a linear combination of inputs $x$ and weights $w$ with a bias $b$.

$$
a = w_1x_1+w_2x_2+b
$$

A value of $a$ greater than $0$ corresponds to one class, while that of less than $0$ corresponds to the other. It can be visualized as a <span style = "color:lightblue">step function</span> $u(a)$ or <span style = "color:lightblue">sigmoid function</span> $\sigma(a)$ which outputs either $0$ or $1$. Normally, it is expressed as a probability of whether the object belongs to the class (i.e., true or false).

$$
p(y=1|x) = \sigma(w^Tx+b)=\sigma(\sum_{d-1}^{D}w_dx_d+b)
$$
> [!INFO]
> This model is referred to as <span style = "color:lightblue">logistic regression</span>, as a sigmoid function is also referred to as a logistic function.

## Cross-entropy Loss

In **binary** classification, a <span style = "color:lightblue">binary cross-entropy loss</span> is used instead.

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

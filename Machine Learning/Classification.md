A classification model (i.e., a <span style = "color:lightblue">classifier</span>) takes as input <span style = "color:lightblue">non-class attribute values</span> and returns a <span style = "color:lightblue">class value</span>. Classification algorithms include [[Decision Tree|decision trees]], **rule-based**, **Bayesian**, **neural networks**, **support vector machines (SVM)**, and ***k*-nearest neighbors (KNN)**.

Classification is a <span style = "color:lightblue">supervised</span> learning model.

## Binary Classification
<span style = "color:lightblue">Binary classification</span> can be expressed as a linear combination of inputs $x$ and weights $w$ with a bias $b$. Inputs with higher weighting correlated to greater importance and affect the output more drastically (*similar to neurons*).

$$
a = w_1x_1+w_2x_2+b
$$

A value of $a$ greater than $0$ corresponds to one class, while that of less than $0$ corresponds to the other. It can be visualized as a <span style = "color:lightblue">sigmoid function</span> $\sigma(a)$ (*see [[Feedforward Neural Networks#Activation Functions|activation functions]]*) which outputs values between $0$ and $1$. Normally, it is expressed as a probability of whether the object belongs to the class (i.e., true or false).

$$
p(y=1|x) = \sigma(w^Tx+b)=\sigma(\sum_{d-1}^{D}w_dx_d+b)
$$
> [!INFO]
> This model is referred to as <span style = "color:lightblue">logistic regression</span>, as a sigmoid function is also referred to as a logistic function.

### Cross-entropy Loss
In **binary** classification, a <span style = "color:lightblue">binary cross-entropy (BCE) loss</span> is used instead.

## Bayesian Classification
Based on the **Bayes rule**, <span style = "color:lightblue">Bayesian classification</span> classifies an object based on the [[Data Preprocessing#Probability Independence|probability]] of observing events (i.e., attribute values) in the dataset.

This classification is **easy to implement** and **obtains good results for most cases**. However, it relies on the [[#Conditional Independence|conditional independence assumption]] which may cause a loss of accuracy.

### Bayes Rule
The <span style = "color:lightblue">Bayes rule</span> is shown below.

$$P(A|B)=\frac{P(A\cap B)}{P(B)}=\frac{P(B|A)P(A)}{P(B)}$$
The Bayes rule can be applied to classification and hypothesis testing, where:
- $P(h)$: <span style = "color:lightblue">prior probability</span> of hypothesis $h$ (i.e., initial probability of $h$ before observing the training data)
- $P(h|D)$: <span style = "color:lightblue">posterior probability</span> of $h$ after observing the data $D$ (i.e., probability of $h$ given $D$)
- $P(D|h)$: <span style = "color:lightblue">likelihood</span> of observing the data $D$ given the hypothesis $h$
- $P(D)$: probability that the data $D$ will be observed

$$P(h|D)=\frac{P(D|h)P(h)}{P(D)}=\frac{P(D|h)P(h)}{\sum_h{P(D|h)P(h)}}$$


#### Example
The probabilities of the events of developing COVID-19 ($A$) and experiencing cough symptoms ($B$) are shown below.
- $P(B|A)=0.8$ (i.e., probability of coughing after developing COVID-19)
- $P(A)=0.005$ (i.e., probability of COVID-19)
- $P(B)=0.05$ (i.e., probability of coughing)

With the Bayes rule, the probability of developing COVID-19 after cough symptoms is obtained.

$$
\begin{align}
	P(A|B)&=\frac{P(B|A)P(A)}{P(B)} \newline
	&=\frac{0.8\times 0.005}{0.05} \newline
	&=0.08
\end{align}
$$

### Naive Bayes Classifier
The <span style = "color:lightblue">naive Bayes classifier</span> assumes [[#Conditional Independence|conditional independence]]. Without the assumption, the calculated probabilities will be very small, which is undesired.

#### Conditional Independence
Absolute independence is a strong requirement and is **seldom met**. Random variables $X$ and $Y$ are **conditionally independent** given $Z$ when the following statement is true.

$$P(X|Y,Z)=P(X|Z)$$

Given $Z$, knowledge about $X$ contains <u>no information</u> about $Y$.

In classification, the **attributes are assumed to be conditionally independent given the class label**.

### Prediction
To predict the class of a particular tuple $x$, the following is done.
- Compute probability $P(C_i|x)$ for <u>every</u> possible class $C_i$.
- Assign the tuple to the class $C_i$ that has the <span style = "color:lightblue">maximum posterior probability (MAP)</span>.

In other words, the class $C_i$ that maximizes the probability $P(x|C_i)P(C_i)$ is selected.

$$\text{prediction}=\arg \max_{C_i}{P(C_i)}\prod_{k}{P(x_k|C_i)}$$

With the conditional independence assumption, the probability $P(x|C_i)$ is calculated easily, reducing the computational cost.

$$P(x|C_i)=\prod_{k=1}^{n}P(x_k|C_i)$$

> [!INFO]
> If the attribute is **continuous-valued**, the attribute values can be discretized or the probability can be estimated based on some distribution (e.g., Gaussian distribution).

> [!INFO]
> The <span style = "color:lightblue">Laplace correction</span> fixes the case where there are no tuples of $C_i$ having $A_k=x_k$. If any of the probabilities is zero, the entire probability will be zero as well.
> $$
> P(x_k|C_i)=\frac{N_{k,C_i}+1}{N_{C_i}+c}
> $$
> The expression for the Laplace correction is shown above, where $c$ is the number of distinct values for attribute $A_k$.

### Example
A dataset is shown below. A prediction of the following sample tuple is made.

$$(\text{age}=\text{senior},\text{income}=\text{low},\text{student}=\text{yes},\text{credit\_rating}=\text{excellent})$$

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

First, the **prior probability** of each class is calculated, where $C_1$ represents `yes` and $C_2$ represents `no`.

$$
\begin{gather}
	P(C_1)=\frac{9}{14}=0.643 \\
	P(C_2)=\frac{5}{14}=0.357
\end{gather}
$$

The individual probabilities of each attribute of the sample tuple given the class $C_1$ are calculated.

$$
\begin{gather}
P(\text{age}=\text{senior}|C_1)=\frac{3}{9}=0.33 \\
P(\text{income}=\text{low}|C_1)=\frac{3}{9}=0.33 \\
P(\text{student}=\text{yes}|C_1)=\frac{6}{9}=0.66 \\
P(\text{credit\_rating}=\text{excellent}|C_1)=\frac{3}{9}=0.33
\end{gather}
$$

Similarly, the individual probabilities of each attribute of the sample tuple given the class $C_2$ are calculated.

$$
\begin{gather}
P(\text{age}=\text{senior}|C_2)=\frac{2}{9}=0.22 \\
P(\text{income}=\text{low}|C_2)=\frac{1}{9}=0.11 \\
P(\text{student}=\text{yes}|C_2)=\frac{1}{9}=0.11 \\
P(\text{credit\_rating}=\text{excellent}|C_2)=\frac{3}{9}=0.33
\end{gather}
$$

Because of the **conditional independence assumption**, $P(x|C_1)$ and $P(x|C_2)$ can be calculated by multiplying their respective attribute probabilities together.

$$
\begin{align}
P(x|C_1) & = P(\text{senior}|C_1)\times P(\text{low}|C_1)\times P(\text{yes}|C_1) \times P(\text{excellent}|C_1) \\
& =0.33 \times 0.33 \times 0.66 \times 0.33 \\
& = 0.0237 \\
P(x|C_2) & = P(\text{senior}|C_2)\times P(\text{low}|C_2)\times P(\text{yes}|C_2) \times P(\text{excellent}|C_2) \\
& = 0.22 \times 0.11 \times 0.11 \times 0.33 \\
& = 0.000878
\end{align}
$$

Lastly, $P(x|C_1)P(C_1)$ and $P(x|C_2)P(C_2)$ are calculated.

$$
\begin{align}
P(x|C_1)P(C_1) & = 0.0237 \times 0.643 = 0.0152 \\
P(x|C_2)P(C_2) & = 0.000878 \times 0.357 = 0.000313
\end{align}
$$

Thus, the sample tuple should be assigned $C_1$ (i.e., `yes`) as the class probability of $C_1$ is greater.

### Code
The `sklearn` library provides the `BernoulliNB` object for naive Bayes classification.

```python
from sklearn.naive_bayes import BernoulliNB

bnb = BernoulliNB(alpha = 0)
bnb.fit(X_train, Y_train)
bnb.predict(X_test)
```

The `alpha` parameter determines whether [[#Prediction|Laplace correction]] should be used.

> [!INFO]
> In text data, it is required to vectorize the input text data.
> ```python
> from sklearn.feature_extraction.text import CountVectorizer
> 
> vect = CountVectorizer(stop_words = "english", binary = True)
> X_train = vect.fit_transform(X_train)
> X_test = vect.fit_transform(X_test)
> ```

## Nearest Neighbor Classification
A <span style = "color:lightblue">nearest neighbor classifier</span> assigns class labels to an object based on its **similarity** to objects in the training data.

Similarity measures include the [[Clustering#Similarity|Manhattan distance]] and [[Clustering#Similarity|Euclidean distance]].

### $k$-Nearest Neighbor (KNN)
Given a new entry, the <span style = "color:lightblue">k-nearest neighbors</span> algorithm searches for the $k$ nearest training data entries based on a pre-defined distance metric and assigns the new entry the **majority class label in the nearest neighbor set**.

> [!INFO]
> [[Data Preprocessing#Normalization|Data normalization]] must be performed as the distance metric is affected by the ranges of the attribute values.

The number of neighbors $k$ is a user-defined parameter which affects the accuracy of the classifier.
- A low value of $k$ (e.g., $k=1$) makes the classifier oversensitive to noise.
- A high value of $k$ (e.g., $k=N$) makes the classifier include irrelevant classes into the prediction.

**The value of $k$ can be tuned by [[#k -Fold Cross-validation|cross-validation]]**.

> [!INFO]
> Instead of assigning the majority class label, the algorithm can also take into account the distance between a point and its neighbors.
> $$
> w=\frac{1}{dist(x_q,x_k)^2}
> $$
> Here, the weighting decreases as the distance increases.

KNN is a <span style = "color:lightblue">lazy learning</span> algorithm. It simply stores all training examples and only compares the similarity between a new object and the dataset during testing.

> [!INFO]
> For lazy learning algorithms, computation on training is a lot, while that of on testing is little. Thus, for applications that require real-time computational speed, KNN is not suitable.

### Dimensionality
As stated in [[Data Preprocessing#Reduction|dimensionality reduction]], when dimensionality increases (i.e., more attributes are added), data becomes increasingly **sparse**. Thus, density and distance between points becomes less meaningful.

The number of dimensions can be reduced. Alternatively, weights can be added to the distance metric to give more importance to certain attributes.

$$dist(x_1,x_2)=\sqrt{\sum_{i=1}^{n}{\beta_i(x_{1i}-x_{2i})^2}}$$

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

A <span style = "color:lightblue">macro-averaged</span> score simply averages the metric values across all classes, while a <span style = "color:lightblue">micro-averaged</span> score uses the 

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

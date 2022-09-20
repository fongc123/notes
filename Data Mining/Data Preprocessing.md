# Data Preprocessing

Real world data is dirty, often containing **incomplete** (*missing fields or inapplicable*), **noisy** (*errors or outliers*), **inconsistent** (*mismatch fields*), and **redundant** (*duplicate fields*) records. The quality of the raw data affects the quality of the mining results. Additionally, the size and complexity of the data affects the cost and performance of data mining tasks.

<span style = "color:lightblue">Data preprocessing</span> is the preparation stage before the data is processed, where (1) dirty data is removed and (2) the size and complexity of the data is reduced. It involves **data cleaning**, **data integration**, **data transformation**, and **data reduction**.

## Data Objects
A <span style = "color:lightblue">dataset</span> is a collection of <span style = "color:lightblue">objects</span>, where each object corresponds to each *item* in the data. Alternative names for **object** include *record*, *tuple*, *point*, *case*, *sample*, etc.

An object is characterized by a set of <span style = "color:lightblue">attributes</span> (e.g., `name`, `eye_color`, `temperature`). Alternative names for **attribute** include *variable*, *field*, *characteristic*, and *feature*.

Additionally, each attribute has a corresponding <span style = "color:lightblue">attribute value</span>, where a mapping between an attribute and its value creates a key-value pair.

```json
{
	"name" : "Bob"
}
```

All machine learning algorithms have a <span style = "color:lightblue">training set</span> and a <span style = "color:lightblue">test set</span> (and occasionally a <span style = "color:lightblue">validation set</span>). A model is fit based on the training set, where each object of the consists of a <span style = "color:lightblue">class attribute</span> (i.e., the correct answer) and a set of labels (i.e., data).

> [!WARNING]
> The test set and the training set must be disjoint.

## Statistical Descriptions
Statistical descriptions give an overall picture of the data. Typically, they involve the <span style = "color:lightblue">central tendency</span> (e.g., mean, median, mode, midrange), the <span style = "color:lightblue">dispersion</span>, and some <span style = "color:lightblue">visualization</span> (e.g., boxplots, histogram, scatter plots) of the descriptions.

> [!INFO]
> The standard arithmetic mean is susceptible to outliers. The **trimmed mean** will ignore the smallest and largest data points when calculating the mean to try to solve this issue.

> [!INFO]
> The **midrange** is the average of the smallest and largest values in the data.

A review of several dispersion statistics is shown below.
- range: difference between smallest and largest value
- *k*th percentile: value $x_i$ with the property that $k$ percent of the data is smaller than $x_i$
- quartiles: $25^{th}$ percentile ($Q_1$), $50^{th}$ percentile, $75^{th}$ percentile ($Q_3$)
- interquartile range (IQR): $IQR=Q_3 - Q_1$
- five-number summary: minimum, $Q_1$, median, $Q_3$, and maximum
- variance: measure of dispersion 
- standard deviation: another measure of dispersion

> [!INFO]
> Outliers are usually defined as values greater than or lower than $1.5 \times IQR$.

## Cleaning
<span style = "color:lightblue">Data cleaning</span> attempts to fill in missing values, smooth out noise, and correct inconsistencies in the data.

**Missing values** can be solved by either ignoring them or replacing them with placeholder values (e.g., global constant, attribute mean, or the most probable value). They can also be replaced manually, but this may be infeasible.

**Noise** can be solved by removing outliers, binning, regression, or clustering. <span style = "color:lightblue">Binning</span> sorts values into equally-sized bins, and each value is replaced by the bin average.

Lastly, **inconsistencies** can be solved by referring to the metadata or consulting an external source of information to verify values. For example, a person's height should not be a negative value.

## Integration
<span style = "color:lightblue">Data integration</span> combines data from multiple data sources into a coherent data store. Problems that should be considered during integration are listed below.
- entity identification: multiple fields refer to the same entity
- data value conflicts: for the same entity, values from different sources are conflicting
- data redundancy: identical fields or values for an entity

Statistical evaluations can be performed to determine if it is necessary to keep *all* the attributes.

### Correlation Coefficient
The <span style = "color:lightblue">correlation coefficient</span> $r$ can be used to determine if **numerical attributes** are correlated with each other.

The expression for the correlation coefficient between attributes $A$ and $B$ is shown below, where $a_i$ and $b_i$ are the respective values, $\bar{A}$ and $\bar{B}$ are the respective means, and $\sigma_A$ and $\sigma_B$ are the respective standard deviations.

$$r_{A,B}=\frac{\frac{1}{N}\sum_{i=1}^{N}(a_i-\bar{A})(b_i-\bar{B})}{\sigma_A\sigma_B}=\frac{\sum_{i=1}^{N}a_ib_i-N\bar{A}\bar{B}}{N\sigma_A\sigma_B}$$

## Probability & Independence
Given events $A$ and $B$, the probability expression of a disjunction (either $A$ or $B$) is shown below.

$$P(A\vee B)=P(A)+P(B)-P(A\wedge B)$$
Conditional probability is the probability of an event $A$ *given* that another event $B$ has occurred.

$$P(B|A)=\frac{P(A\cap B)}{P(A)}$$
It is the probability that both events occur given that the first event has already occurred. Two random variables are **independent** if the following statements are true.

$$
\begin{align}
	P(X|Y)=P(X) \space or \space P(Y|X)=P(Y)
\end{align}
$$
Equivalently, the probability of $X$ and $Y$ is shown below.

$$P(X,Y)=P(X)P(Y)$$

Knowledge about $X$ contains <u>no information</u> about $Y$.


> [!INFO]
> Independence implies no correlation, but no correlation does not always imply independence.

### Chi-squared Test
The <span style = "color:lightblue">Chi-squared test</span> $\chi^2$ can be used to determine if **categorical attributes** are independent of each other.

The expression for the $\chi^2$ test is shown below, where $r$ and $c$ represent the number of rows and columns respectively.

$$
\chi^2=\sum \frac{(observed-expected)^2}{expected}
= \sum_{i=1}^{c}\sum_{j=1}^r\frac{(o_{ij}-e_{ij})^2}{e_{ij}}
$$

 There are $N$ occurrences of the event where attribute $A$ has value $a_i$ and attribute $B$ has value $b_j$. Assuming that the attributes are independent, the expression for the <span style = "color:lightblue">expected value</span> $e_{ij}$ is shown below.

$$
\begin{align}
	e_{ij} & = N\times P(A=a_i \wedge B=b_j)\newline
	& = \frac{1}{N}[count(A=a_i)\times count(B=b_j)]
\end{align}	
$$

After the $\chi^2$ value is calculated, a look-up value is obtained from a table at a desired <span style = "color:lightblue">significance level</span> (e.g., 0.05) with a calculated <span style = "color:lightblue">degree of freedom</span>.

$$df=(r-1)\times(c-1)$$

The <span style = "color:lightblue">null hypothesis</span> is rejected if the calculated value exceeds the look-up value.

#### Example
We would like to determine if attribute $A$ and $B$ are independent of each other or not. The distinct values for $A$ are male ($a_1$) and female ($a_2$), while that of for $B$ are fiction ($b_1$) and non-fiction ($b2$). A two-by-two contingency table containing the <span style = "color:lightblue">observed frequencies</span> of each attribute is shown below.

|                                              |                    male                    |                   female                    | <span style = "color:lightblue">total</span> |
|:--------------------------------------------:|:------------------------------------------:|:-------------------------------------------:|:--------------------------------------------:|
|                   fiction                    |                    250                     |                     200                     |                      <span style = "color:lightblue">450</span>                      |
|                 non-fiction                  |                     50                     |                    1000                     |                      <span style = "color:lightblue">1050</span>                     |
| <span style = "color:lightblue">total</span> | <span style = "color:lightblue">300</span> | <span style = "color:lightblue">1200</span> |                      <span style = "color:lightblue">1500</span>                     |

The expected frequencies are found.

|             | male | female | total |
|:-----------:|:----:|:------:|:-----:|
|   fiction   |  90  |  360   |  450  |
| non-fiction | 210  |  840   | 1050  |
|    total    | 300  |  1200  | 1500      |

A sample calculation for the cell that represents males and fiction is shown below.

$$
\begin{align}
	e_{11} & =N\times P(A=a_1 \wedge B=b_1) \newline
	& = N\times P(A=a_1)\times P(B=b_1) \newline
	& = 1500 \times \frac{300}{1500} \times\frac{450}{1500} \newline
	e_{11} & = 90
\end{align}
$$
We calculate the probability that the events fiction and male occur out of all occurrences. If they are independent, the probability of an event occuring should not affect the probability of the other event occurring.

The $\chi^2$ value of this contingency table is $507.93$ with a degree of freedom of $1$. Referring to a table, the corresponding value at a significance level of $0.001$ with degree of freedom of $1$ is $10.83$.

$$\chi^2=507.93>10.83$$
Thus, since the calculated value exceeds the table value, the null hypothesis is rejected, and the attributes $A$ and $B$ are considered to be **not independent**.


## Transformation
<span style = "color:lightblue">Data transformation</span> modifies the data to improve the results gained from data mining (i.e., improve mining performance.
- <span style = "color:lightblue">attribute or feature construction</span>: create new attributes that capture important information more effectively than the original ones (e.g., Fourier transform)
- <span style = "color:lightblue">normalization</span>: scale attribute values to smaller, specified range
- <span style = "color:lightblue">discretization</span>: divide continuous attribute into intervals to reduce data size (e.g., histogram, cluster analysis, decision-tree analysis)

### Normalization
In min-max normalization, original values a mapped to a new range within a new minimum ($nmin$) and maximum ($nmax$). The expression of a new value $v'$ is shown below.

$$v'=\frac{v-min_A}{max_A-min_A}(nmax_A-nmin_A)+nmin_A$$

For example, an income range of \$12,000 to \$98,000 can be normalized to a range of 0 to 1. Typically, ranges of $[0.0, 1.0]$ or $[-1.0, 1.0]$ are used. However, this normalization method requires estimation of the absolute minimum and maximum values of the original dataset which may not be known. 

In ***z*-score normalization**, new values are mapped based on the attribute mean $\bar{A}$ and standard deviation $\sigma_A$ of the original values.

$$v'=\frac{v-\bar{A}}{\sigma_A}$$
> [!QUESTION]
> How many standard deviations from the average does the data point lie?

## Reduction

<span style = "color:lightblue">Data reduction</span> obtains a reduced representation of the dataset, while allowing similar, if not the same, analytical results to be produced.

> [!INFO]
> To capture a fraction $r$ of a dataset with $d$ dimensions, the range of each output that must be covered is $r^{\frac{1}{d}}$. As dimensionality increases, data becomes increasingly sparse, and the number of required points increases **exponentially** to maintain the same sampling density.

### Principal Component Analysis (PCA)

<span style = "color:lightblue">Principal component analysis (PCA)</span> projects original data onto a **lower-dimensional** space to perform dimensionality reduction. The dimension projection with the **largest amount of variation in the data is chosen** (i.e., find projection $w$ such that $var(w^tx)$ is maximized).

#### Variation

A review of calculating variation is shown below.
- one-dimensional: variance
- two-dimensional: variance and <span style = "color:lightblue">covariance</span>
- three-dimensional: covariance with $3$ attributes ($x$, $y$, $z$)
- $n$-dimensional: covariance with $n$ attributes

> [!INFO]
> <span style = "color:lightblue">Variance</span> describes the spread between a data set from its mean value.
> $$Var(x)=\frac{\sum(x_i-\bar{x})^2}{n-1}$$
> <span style = "color:lightblue">Covariance</span> describes how two random variables will change when compared with each other.
> $$Cov(x,y)=\frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{N-1}$$
> The variance of a single random variable $x$ can also be expressed as the covariance of itself $cov_{x,x}$.
> 
> The <span style = "color:lightblue">covariance matrix</span> $C$ is a square matrix with the below form and with size $d$ which represents the number of dimensions. It represents the variances and covariances of the dimensions.
> $$
> \begin{align}
> 	C & = \sum_{k=1}^{n}(\textbf{X}_k-\bar{\textbf{X}})(\textbf{X}_k-\bar{\textbf{X}})^T \newline \newline
> 	\sum & =
> 	\begin{bmatrix}
> 		Var(X_1) & \cdots & Cov(X_d,X_1) \newline
> 		\vdots & \ddots & \vdots \newline
> 		Cov(X_1, X_d) & \cdots & Var(X_d)
> 	\end{bmatrix}
> \end{align}
> $$
> It should be noted that $Cov(X_1, X_d)$ and $Cov(X_d, X_1)$ are identical.

The <span style = "color:lightblue">eigenvectors</span> of the covariance matrix $C$ are found.

$$C\textbf{v}=\lambda \textbf{v}$$

In the context of PCA, the eigenvector(s) $\textbf{v}$ are the <span style = "color:lightblue">principal components (PC)</span>. The eigenvalue $\lambda$ measures the variance magnitude in the direction of the eigenvector, where decreasing eigenvalue corresponds to decreasing significance or strength of a particular dimension.

Principal components with the smallest eigenvalues are discarded to perform dimensionality reduction.

#### Choosing PCs

The <span style = "color:lightblue">proportion of variance</span> shows the proportion of principal components kept. Its expression is shown below, where $k$ corresponds to the number of dimensions kept and $d$ corresponds to the number of dimensions before PCA was performed.

$$proportion=\frac{\lambda_1+\lambda_2+\cdots+\lambda_k}{\lambda_1+\lambda_2+\cdots+\lambda_d}$$

The proportion of variance increases logarithmically as the number of eigenvectors increases. At a high number of eigenvectors, additional eigenvectors will not significantly increase the variance.

![[data-mining-eigenvectors-variance.png|500x400]]

> [!WARNING]
> Some machine learning problems, such as classification, and datasets will cause problems when performing dimensionality reduction, as the dimensions are needed in these problems. Additionally, PCA does not consider nonlinear cases (*only unidirectional*).

### Attribute Subset Selection

In <span style = "color:lightblue">attribute or feature subset selection</span>, the <u>minimum</u> possible **subset** of attributes is chosen such that the quality of the data mining task is not compromised.

It is difficult to test *all* possible combinations of attributes, as there are $2^d$ possible combinations of $d$.

<span style = "color:lightblue">Greedy forward selection</span> selects the best $n$ single attributes. On the other hand, <span style = "color:lightblue">greedy backward elimination</span> removes the worst $n$ attributes. The final reduced attribute set is obtained.

> [!INFO]
> **Greedy**, in computer science, means...

### Numerosity Reduction

The data volume is reduced by choosing smaller forms of data representation. Storing each point of the dataset may use unnecessary storage space.

<span style = "color:lightblue">Parametric methods</span> assume the data is fit to a model, where only the **estimated model parameters** are stored instead of the actual data. For example, if a dataset follows a linear regression, only the parameters $a$ and $b$ are needed.

$$y=\underbracket{a}_{slope}x+\underbracket{b}_{y-intercept}$$
<span style = "color:lightblue">Nonparametric methods</span> do not assume that the data is fitted to a model. Instead, they are stored in smaller forms, such as histograms, clustering, sampling, or <span style = "color:lightblue">data cube aggregation</span>.

> [!INFO]
> In <span style = "color:lightblue">random sampling</span>, there is an equal probability of selecting any particular item. On the other hand, in <span style = "color:lightblue">stratified sampling</span>, the dataset is partitioned (e.g., by age group), and samples are drawn from each partition. Random sampling is applicable to normally distributed data, while stratified sampling is applicable to skewed data.


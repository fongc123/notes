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

After the $\chi^2$ value is calculated, a look-up value is obtained from a table at a desired <span style = "color:lightblue">significance level</span> (e.g., 0.05) with a <span style = "color:lightblue">degree of freedom</span>.

$$df=(r-1)\times(c-1)$$

The <span style = "color:lightblue">null hypothesis</span> is rejected if the calculated value exceeds the look-up value.

## Transformation
kk

## Reduction
kk


Normalization maps a value of $v$ of $A$ to a new range.

$$
v'=\frac{v-min_A}{max_A-min_A}(new\_max_A-new\_min_A)+new\_min_A
$$


For example, an income range of \$12,000 to \$98,000 can be normalized to a range of 0 to 1. Typically, ranges of $[0.0, 1.0]$ or $[-1.0, 1.0]$ are used.

The above normalization method requires prior knowledge of the absolute minimum and maximum values of the original dataset which may not be known. Alternatively, ***z*-score normalization** can be done instead.

> [!QUESTION]
> How many standard deviations from the average does the data point lie?

The new value $v'$ is calculated as follows, where $\bar{A}$ corresponds to the average of the dataset.

$$v'=\frac{v-\bar{A}}{\sigma_A}$$
Discretization divides the range of a continuous attribute (e.g., age) into <u>intervals</u>. It also reduces the data size. Some methods include the following.
- histogram
- cluster analysis (*when original data is clearly separated into clusters*)
- decision-tree analysis

Data reduction obtains a reduced representation of the dataset, while allowing (*at least as close as possible*) the same analytical results to be pro
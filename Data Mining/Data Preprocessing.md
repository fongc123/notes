# Data Preprocessing

Real world data is dirty, often containing **incomplete** (*missing fields or inapplicable*), **noisy** (*errors or outliers*), **inconsistent** (*mismatch fields*), and **redundant** (*duplicate fields*) records. The quality of the raw data affects the quality of the mining results. Additionally, the size and complexity of the data affects the cost and performance of data mining tasks.

<span style = "color:lightblue">Data preprocessing</span> is the preparation stage before the data is processed, where (1) dirty data is removed and (2) the size and complexity of the data is reduced. It involves **data cleaning**, **data integration**, **data transformation**, and **data reduction**.


## Basics
### Data Objects
A <span style = "color:lightblue">dataset</span> is a collection of <span style = "color:lightblue">objects</span>, where each object corresponds to each *item* in the data. Alternative names for **object** include *record*, *tuple*, *point*, *case*, *sample*, etc.

An object is characterized by a set of <span style = "color:lightblue">attributes</span> (e.g., `name`, `eye_color`, `temperature`). Alternative names for **attribute** include *variable*, *field*, *characteristic*, and *feature*.

Additionally, each attribute has a corresponding <span style = "color:lightblue">attribute value</span>, where a mapping between an attribute and its value creates a key-value pair.

```json
{
	"name" : "Bob"
}
```


### Statistical Descriptions
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

## Cleaning
<span style = "color:lightblue">Data cleaning</span> attempts to fill in missing values, smooth out noise, and correct inconsistencies in the data.

**Missing values** can be solved by either ignoring them or replacing them with placeholder values (e.g., global constant, attribute mean, or the most probable value). They can also be replaced manually, but this may be infeasible.

**Noise** can be solved by removing outliers, binning, regression, or clustering. 

## Integration
kk

## Transformation
kk

## Reduction
kk

> [!INFO]
> Outliers are usually defined as values greater than or lower than $1.5 \times IQR$.

$$
\chi^2=\sum \frac{(observed-expected)^2}{expected}
= \sum_{i=1}^{c}\sum_{j=1}^r\frac{(o_{ij}-e_{ij})^2}{e_{ij}}
$$
In the above equation for calculating the Chi-squared value $\chi^2$, $r$ and $c$ correspond to the number of rows and number of columns respectively.

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
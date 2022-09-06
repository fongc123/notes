# Data Preprocessing

Real world data is dirty, often containing **incomplete** (*missing fields or inapplicable*), **noisy** (*errors or outliers*), **inconsistent** (*mismatch fields*), and **redundant** (*duplicate fields*) records. The quality of the raw data affects the quality of the mining results. Additionally, the size and complexity of the data affects the cost and performance of data mining tasks.

<span style = "color:lightblue">Data preprocessing</span> is the preparation stage before the data is processed, where (1) dirty data is removed and (2) the size and complexity of the data is reduced. It involves **data cleaning**, **data integration**, **data transformation**, and **data reduction**.

## Data Objects
A <span style = "color:lightblue">dataset</span> is a collection of <span style = "color:lightblue">objects</span>, where each object corresponds to each *item* in the data. Alternative names for **object** include *record*, *tuple*, *point*, *case*, *sample*, etc.

An object is characterized by a set of <span style = "color:lightblue">attributes</span> (e.g., `name`, `eye_color`, `temperature`). Alternative names for **attribute** include *variable*, *field*, *characteristic*, and *feature*. Additionally, each attribute has a corresponding <span style = "color:lightblue">attribute value</span>.

```json
{
	"name" : "Bob"
}
```

A mapping between an attribute and an attribute value creates a key-value pair.

## Statistical Descriptions
Statistical descriptions give an overall picture of the data. Typically, they involve the <span style = "color:lightblue">central tendency</span> (e.g., mean, median, mode, midrange), the <span style = "color:lightblue">dispersion</span>, and some <span style = "color:lightblue">visualization</span> (e.g., boxplots, histogram, scatter plots) of the descriptions.

> [!INFO]
> The standard arithmetic mean is susceptible to outliers. The **trimmed mean** will ignore the smallest and largest data points when calculating the mean to try to solve this issue.

> [!INFO]
> The **midrange** is the average of the smallest and largest values in the data.

A review on dispersion statistics is shown below.
- range: difference between smallest and largest value
- *k*th percentile: value $x_i$ with the property that $k$ percent of the data is smaller than $x_i$
- quartiles: $25^{th}$ percentile ($Q_1$), $50^{th}$ percentile, $75^{th}$ percentile ($Q_3$)
- interquartile range (IQR): $IQR=Q_3 - Q_1$
- five-number summary: minimum, $Q_1$, median, $Q_3$, and maximum
- variance: measure of dispersion 
- standard deviation: another measure of dispersion

> [!INFO]
> Outliers are usually values greater or lower than $1.5 \times IQR$.


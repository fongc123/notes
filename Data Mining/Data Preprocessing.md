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


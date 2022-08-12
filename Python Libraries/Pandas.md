# Pandas
The `pandas` library is a powerful data frame library for the <span style = "color:lightblue">exploration and manipulation</span> of data. It is a Python library and, thus, is imported before usage.

```python
import pandas as pd
```

## Creating a Data Frame
<span style = "color:lightblue">Data frames</span> store data in tables.

### Manual Creation
The `DataFrame` object is called with a dictionary, where each key-value pair maps a column name to a list of row values. Information in the cells **are not limited** to integers.

```python
pd.DataFrame({ "Yes" : [50, 25], "No" : [131, 2] })
```

|     | **Yes** | **No** |
| :---: | :-------: | :------: |
| 0   | 50      | 131    |
| 1   | 21      | 2      |

An empty list (i.e., `[]`) will create an empty data frame with no row values.

```python
pd.DataFrame({ "Yes" : [], "No" : [] })
```

|     | **Yes** | **No** |
| --- | ------- | ------ |
|     |         |        |

The `index` parameter can be specified to customize the row names. By default, the indices will be positive integers starting from `0`.

```python
pd.DataFrame(
	{ "Yes" : [1, 2, 3], "No" : [4, 5, 6] },
	index = [ "Apple", "Banana", "Orange" ]
)
```

|        | **Yes** | **No** |
|:------:|:-------:|:------:|
| Apple  |    1    |   4    |
| Banana |    2    |   5    |
| Orange |    3    |   6    |
|        |         |        |

> [!INFO]
> The number index elements in the array **must match** the number of rows.

### Importing & Exporting
Data frames can also be imported from and exported to several file inputs and outputs respectively. The code blocks below demonstrate how to read in a CSV file and a JSON file respectively.

```python
df = pd.read_csv("<FILENAME>.csv")
```

```python
df = pd.read_json("<FILENAME>.csv")
```

The code block below demonstrates how to export a data frame to a CSV file.

```python
df.to_csv("<FILENAME>.csv")
```

## Exploration
`pandas` has functionality to easily view the data, especially when it is large.

### Viewing

In Jupyter Notebook, executing a cell that contains the data frame variable (e.g., `df`) will print the dataframe in its entirety. The `head` method is used to get the first *n* rows of a data frame, and the `shape` method is used to get the dimensions (number of columns and number of rows) of a data frame.

```python
df.head()
```

```python
df.shape
```

If no argument is passed into `head`, only the **first five** rows are shown by default.

### Description
The `mean` method will calculate the mean of a column. Alternatively, the `describe` method 
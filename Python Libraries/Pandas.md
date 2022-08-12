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

If no argument is passed into `head`, only the **first five** rows are shown by default. Alternatively, the `tail` method is used to get the *last* rows of all columns.

```python
df.tail()
```

### Description
The `mean` method will calculate the mean of a column. Alternatively, the `describe` method wil show a summary containing the **mean**, **standard deviation**, **minimum value**, **maximum value**, **first quartile (25%)**, **second quartile (50%)**, and **third quartile (75%)** of each column.

```python
df.<COLUMN_NAME>.mean()
```

```python
df.describe()
```

The `unique` method returns a list of unique values of a column, while the `value_counts` method returns a list of unique values and the frequency of their occurrences.

```
df.<COLUMN_NAME>.unique()
```

```python
df.<COLUMN_NAME>.value_counts()
```

### Mapping
The two examples below demonstrate the use of <span style = "color:lightblue">mapping</span> to extract information from a data set. The data set contains a list of wines and their reviews. In the first example, the number of times that the words <u>fruity</u> and <u>tropical</u> appear in the `description` field (i.e., column name) are individually summed.

```python
num_tropical = df.description.map(lambda desc: "tropical" in desc).sum()
num_fruity = df.description.map(lambda desc: "fruity" in desc).sum()
```

The occurrences of each word are stored in a series.

```python
desc_count = pd.Series([ num_tropical, num_fruity ], index = [ "Tropical", "Fruity" ])
```

Some knowledge of the `lambda` function would be useful here. It is noted that the `desc` variable is a temporary variable that checks if each description contains the specified word. The `sum` method will only count expressions that evaluate to true.

In the second example, the number of stars a wine product should receive is determined based on the `country` field and the `points` field. A custom function is created to specify the conditions and is applied to the data frame.

```python
def get_stars(row):
	if row.country == "Canada":
		return 3
	elif row.points >= 95:
		return 3
	elif row.points >= 85:
		return 2
	else:
		return 1

stars = df.apply(get_stars, axis = "columns")
```

The `stars` variable contains a series that has the same length as the `df` data frame. Each value corresponds to the wine product at the same index.

### Selection
The code blocks below demonstrate several syntaxes of retrieving columns. 

```python
df.columns # get column labels
```

```python
df["COLUMN1"] # one column
```

```python
df["COLUMN1", "COLUMN2", "COLUMN3"] # multiple columns
```

```python
df["COLUMN1"][i] # ith-row of column
```

The `iloc` method is used to extract specific rows and columns using indices. The first element in the list denotes the row(s), while the second element denotes the column(s).

```python
df.iloc[:, 0] # all rows, first column
```

```python
df.iloc[1:3, 1] # range of rows, second column
```

Additionally, column names (i.e., labels) can be handled as well.

```python
df.loc[:, [ "LABEL1", "LABEL2", "LABEL3" ]]
```

### Conditions

<span style = "color:lightblue">Data mining</span> is the process of extracting **interesting** (non-trivial, implicit, previously unknown, and potentially useful) patterns or knowledge from an **abundance** of data. Ideally, this extraction and analysis process is done automatically or semi-automatically.

> [!INFO]
> Data mining is not the same as database querying.

Data mining consists of several disciplines: statistics, database technology, algorithms (complexity), machine learning, visualization, and pattern recognition.

> [!NOTE]
> In 2003, there were **five exabytes ($10^{18}$ bytes)** of digital data. Now, the same amount of data is created in two days. In 2012, the world data was expanded to **2.72 zettabytes**.

# Data Types & Sources

The **major sources of abundant data** are mainly **social** (e.g., news and social networking), **business** (e.g., web, e-commerce, transactions, and stocks), and **science** (e.g., sensors, bioinformatics, and scientific simulations). New and efficient ways to analyze vast quantities of raw data must be developed.

![[data-mining-system.png|500]]

Additionally, there are several **data repositories**.
- relational data: a set of data where each entry contains the same attributes
- transactional data: a special type of relational data where each entry is a <span style = "color:lightblue">transaction</span> and involves a set of items
- graph data: data that consists of <span style = "color:lightblue">nodes</span> and <span style = "color:lightblue">edges</span> to capture relationships between objects (e.g., social networking or fraud data)
- sequence data: ordered sequence of entries (e.g., DNA sequence)
- time series data: sequence data with measurements of time
- spatial data: data with **geographical attributes** (e.g., spatial coordinates)
- text & multimedia data: databases that contain text and multimedia data (e.g., images and videos) respectively

# Functionalities
The <span style = "color:lightblue">training set</span> is the dataset that was used to create and the model.

$$
train \rightarrow \space model \rightarrow \space predict 
$$
A [[Classification|classification]] problem categorizes records into categorical attributes. On the other hand, a [[Regression|regression]] problem predicts numerical attributes. For example, a model that predicts the age given facial features is related to regression.

A <span style = "color:lightblue">clustering</span> problem puts common objects into <span style = "color:lightblue">clusters</span> based on a <span style = "color:lightblue">similarity measure</span>. Objects in the same cluster are more similar, while objects in separate clusters are more dissimilar. An image segmentation problem is a clustering problem, as the pixels that belong to the same objects are determined. Outliers can also be found using clustering methods.
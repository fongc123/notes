Data visualization is the computer-supported and interactive representation of data to amplify cognition. Data is changed into a visual form to provide insights to users.

> [!INFO]
> Data visualization should involve <span style = "color:lightblue">human computer interaction (HCI)</span> to convey further insight and understanding of the data.

<span style = "color:lightblue">Ansombe's Quartet</span> is an example of the benefits of using data visualization. Four graphs of different datasets are shown below.

![[data-vis-anscombe-quartet.png|500]]

**All datasets have the same arithmetic mean, standard deviation, $r$ coefficient, and linear regression.** But, the distribution of the individual points are significantly different.

The type of visualization is also important, as incorrect chart choices will create little to no insight. The figure below demonstrates the differences between a <span style = "color:lightblue">boxplot</span> and a <span style = "color:lightblue">violin plot</span>.

![[data-vis-violin-plots.png|400]]

A violin plot will show deeper distribution of data points in addition to the standard statistical descriptions, such as the interquartile range and the median.

Visualization must also be efficient and effective. For example, a bar chart for a dataset with one million data points would be too cluttered to display anything useful.

A list of visualization and dataset references can be found [[References|here]]. Refer to [[Color#Color Selection Rules|this section]] for help in selecting colors.

# User-centric Visualization
A <span style = "color:lightblue">user-centric visualization</span> that involves HCI is suitable when there is a need to **augment human capabilities** rather than replace people with computational decision-making methods.

![[data-vis-user.png|650]]

The creation of a data visualization platform begins with the user's needs.

# Common Charts

Some commonly used chart types are described below.
- <span style = "color:lightblue">deviation</span>: emphasize variations from a fixed reference point (e.g., trade surplus or defecit)
- <span style = "color:lightblue">correlation</span>: show the relationship between two or more variables (e.g., life expectancy)
- <span style = "color:lightblue">ranking</span>: show comparisons between items in an ordered list (e.g., election results)
- <span style = "color:lightblue">distribution</span>: show frequency and position of values in a dataset
- <span style = "color:lightblue">evolution</span>: emphasize changing trends over a period of time (e.g., stock price)
- <span style = "color:lightblue">magnitude</span>: show size comparisons (e.g., market capitalization)
- <span style = "color:lightblue">part-to-whole</span>: show how an entity can be broken down into its component elements
- <span style = "color:lightblue">spatial</span>: show locations or geographical patterns in data (e.g., population density)
- <span style = "color:lightblue">flow</span>: show volumes or intensity of movement (e.g., relationship graphs)

> [!INFO]
> Ranking and magnitude seem to be similar, but ranking emphasizes the largest item (e.g., winner in a competition).

> [!INFO]
> If the objective is to simply show the size of components, a magnitude-type chart would be better instead of a part-to-whole chart.

![[data-vis-ft-vocab.png]]

# Data Types
The <span style = "color:lightblue">data type</span> is useful in determining the chart type that best fits the dataset.

|   Type   |                     Description                     |           Example           |
|:--------:|:---------------------------------------------------:|:---------------------------:|
| Nominal  |                  Categorized only                   |           Gender            |
| Ordinal  |               Categorized and ranked                | Competition ranking |
| Interval |       Categorized, ranked, and evenly spaced        |         Test scores         |
|  Ratio   | Categorized, ranked, evenly spaced, and "true zero" |              Height              |

**Ranked** data implies that certain values are superior to other values; however, the difference between each consecutive value may not be the same (i.e., not **evenly spaced**). In ratio data, a zero value implies that there is <u>absolute absence of the variable of interest</u>.

> [!INFO]
> Unlike the Celsius or Fahrenheit temperature scale, the Kelvin scale is a ratio data type, as a temperature reading of 0 corresponds to an absolute absence of thermal energy.

![[data-vis-xai.png|650]]


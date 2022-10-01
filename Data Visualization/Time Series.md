# Time Series Data
A <span style = "color:lightblue">time series</span> is a series of data points indexed, listed, or graphed in chronological order. It is a sequence of discrete time data. 
- <span style = "color:lightblue">timestamp</span>: quantitative values or categorical points in time
- <span style = "color:lightblue">granularity</span>: time interval (e.g., day or hour)
- <span style = "color:lightblue">temporal pattern</span>: repetitive nature (e.g., cyclic or seasonal)

Time series data mainly analyzes the following tasks.
- <span style = "color:lightblue">trend or outlier</span>: general pattern or detect anomalies
- <span style = "color:lightblue">correlation</span>: co-occurrence between two variables
- <span style = "color:lightblue">sequential order</span>: dependency


## Line Graph
A <span style = "color:lightblue">line graph</span> or <span style = "color:lightblue">dot plot</span> directly displays the values of a quantitative variable with respect to time.

|          **Data**           |    **Mark**    |          **Channels**          |       **Task**        | **Scalability** |
|:---------------------------:|:--------------:|:------------------------------:|:---------------------:|:---------------:|
| Two quantitative attributes (one for timestamp) | Points & lines | Horizontal (time) & vertical (value) position | Find trend & extremes | Multiple lines  |

To display additional quantitative variables, multiple lines can be superimposed on a shared chart, where each line is encoded by a different color.

![[data-vis-line-graph-multiple.png|300]]

On the other hand, a <span style = "color:lightblue">slope graph</span> displays the magnitude of change of quantitative attributes.

|                   **Data**                   |       **Mark**        | **Channels** |     **Task**      | **Scalability** |
|:--------------------------------------------:|:---------------------:|:------------:|:-----------------:|:---------------:|
| Two quantitative attributes (one for derived change) | Line connecting marks |   Position   | Emphasize changes | Multiple value levels                |

The example below shows the **change** in amount of sleep in hours in Americans between 2003 and 2017.

![[data-vis-slope-graph.png|400]]

In line graphs, the <span style = "color:lightblue">aspect ratio</span> can drastically alter the perception of change. Additionally, <span style = "color:lightblue">dual axis</span> graphs can create misleading inform

## Area Graph
Similar to a line graph, the x-axis represents time, while y-axis represents attribute values.

To improve space efficiency, juxtaposition techniques are used to combine and shrink charts. Example charts include the <span style = "color:lightblue">horizon chart</span> and the <span style = "color:lightblue">ridgeline plot</span>.

## Bar Graph
A <span style = "color:lightblue">bar graph</span> can display the change of a quantitative variable over time. For multiple variables, a multi-bar chart or multiple single-bar charts can be used.

## Heatmap


## Metaphorical Idioms
In these special charts, the use of metaphors and symbolism in the chart's design, such as **radial timelines**, **calendars**, or **rivers**, complements the context of the data. For example, the use of a calendar view as the base design of a chart is applicable to data about daily and monthly car accidents.

River or road metaphors also create a sense of flowing time.

Other metaphors:
- tree trunk: old data at the center, new data at the edge
- pearl or seashell: flow of time through spiral
- 
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

In line graphs, the <span style = "color:lightblue">aspect ratio</span> can drastically alter the perception of change. Additionally, <span style = "color:lightblue">dual axis</span> graphs can create misleading conclusions.
- <span style = "color:lightblue">indexed line graph</span>: plots normalized data instead of original value (*useful for vastly different data*)
- <span style = "color:lightblue">connected scatterplot</span>: scatter plot with line connection marks to show relationship

> [!WARNING]
> As the indexed line graph shows the normalized values instead of the original values, it shows a **change over time** rather than absolute values.

## Area Graph
Similar to a line graph, an <span style = "color:lightblue">area graph</span> or a <span style = "color:lightblue">stacked graph</span> emphasizes horizontal continuity over vertical items. 

|                     **Data**                      |    **Mark**     |                   **Channel**                   |        **Task**        | **Scalability** |
|:-------------------------------------------------:|:---------------:|:-----------------------------------------------:|:----------------------:|:---------------:|
| Categorical, ordered, quantitative (derived data) | Layers or areas | Vertical position (values), color (categorical) | Find trends & extremes, emphasize change | Multiple time and category keys                |

A <span style = "color:lightblue">stacked graph</span> is a classic method for visualizing change in a set of items, where the sum of the values is as important as the individual items.

However, as it uses areas to convey numbers, they **do not work for negative values** (*better for a line graph*). Additionally, **comparisons between trends are difficult** in a stacked graph.


> [!INFO]
> The lowest layer is aligned at the bottom, and the first category should be carefully considered.

To improve space efficiency, juxtaposition techniques are used to combine and shrink charts. Example charts include the <span style = "color:lightblue">horizon chart</span> and the <span style = "color:lightblue">ridgeline plot</span>.

![[data-vis-ridgeline.png|600]]

## Bar Graph
A <span style = "color:lightblue">bar graph</span> can display the values of a quantitative variable over time. For multiple variables, a multi-bar chart in a single view can be used or multiple single-bar charts in multiple views can be used.

|                     **Data**                      |    **Mark**     |                   **Channel**                   |        **Task**        | **Scalability** |
|:-------------------------------------------------:|:---------------:|:-----------------------------------------------:|:----------------------:|:---------------:|
| Quantitative, categorical | Bars (line) | Horizontal (time), vertical (values), color (categorical) | Compare individual (separate bars) or total (stacked bar) values | Multiple bars              |

![[data-vis-multiple-bars.png|600]]

Alternatively, to summarize duration, compare events, and identify intersections or dependencies, a <span style = "color:lightblue">Gantt chart</span> can be used. This chart is commonly used in the tracking of the timeline of tasks, where length represents task duration and color represents the status of the task.

## Heatmap
A <span style = "color:lightblue">heatmap</span> can display an estimated value of a quantitative variable over time, where the value counts are represented by their color (opacity).

|                     **Data**                      |    **Mark**     |                   **Channel**                   |        **Task**        | **Scalability** |
|:-------------------------------------------------:|:---------------:|:-----------------------------------------------:|:----------------------:|:---------------:|
| Categorical, quantitative (values), ordered (time) | Area (grid layout) | Horizontal (time), vertical (category), color (value) | Find trends & extremes | -             |

The example below shows the PM2.5 density pattern at five different stations in Hong Kong between March 23 to March 31 in 2020.

![[data-vis-heatmap.png|600]]

## Metaphorical Idioms
In these unconventional charts, the use of metaphors and symbolism in the chart's design, such as **radial timelines**, **calendars**, or **rivers**, complements the context of the data.

For example, the use of a calendar view as the base design of a chart is applicable to data about daily and monthly car accidents. River or road metaphors also create a sense of flowing time.

Other unconventional visualization forms are listed below.
- <span style = "color:lightblue">tree trunk</span>: old data at the center, new data at the edge
- <span style = "color:lightblue">pearl</span> or <span style = "color:lightblue">seashell</span>: flow of time through spiral


# Design Tasks

Task design pertains to the purpose of the visualization (i.e., overall message). <span style = "color:lightblue">Bertin's three stages for reading a graphic</span> outline how a visualization is comprehended.
- <span style = "color:lightblue">external</span>: overall context (e.g., graph title, axis labels)
- <span style = "color:lightblue">internal</span>: visual variables used to represent components, such as **marks** and **visual channels** (*see [[Visual Channels#Visual Encoding]]*)
- <span style = "color:lightblue">relationships</span>: connections between components to create meaning and knowledge

These stages are also similar with <span style = "color:lightblue">reading level</span>: **elementary** (*values and variables*), **intermediate** (*comparisons*), **overall** (*meaning*).

> [!QUESTION]
> Why is the user looking at the visualization?

## Task Abstraction

Each visualization task is domain-dependent, as the data is different. However, the tasks can be abstracted. Similar <span style = "color:lightblue">task abstractions</span> have similar solutions.

$$\text{task}\rightarrow\text{verb (action)}+\text{noun (target)}$$

A task consists of an **action** and a **target** to perform the action on.

### Actions



The <span style = "color:lightblue">analyze</span> category aims to create insights at a high level. The <span style = "color:lightblue">consume</span> subcategory simply redistributes information (e.g., )

### Verb: Analyze
Consume: discover, present, enjoy (for fun). The `consume` category simply redistributes information.
Produce: annotate, record, derive. The `produce` category performs additional modification to the display to show more insights.

### Verb: Search

Finding for one or a group of points (locate, browse, locate, explore)

### Verb: Query

Directly find the value of a particular point, a group of points, or all the points (identify, compare, summarize).

### Target
A target refers to the subject of a visualization <u>task</u>. All data possess trends, outliers, and features, where one attribute (variable) or multiple attributes can be analyzed. Specific to network and spatial data are topologies and shapes respectively.


## Interaction Design

<span style = "color:lightblue">Interactions</span> can be implemented to handle the increasing complexity of a dataset.
- <span style = "color:lightblue">manipulate</span>: change view
- <span style = "color:lightblue">facet</span>: facet across multiple views
- <span style = "color:lightblue">reduce</span>: reduce items or attributes in a single view

Additionally, new data can be derived to show insights within the same view.

### Manipulate

Automatic? manual?

Manual $\rightarrow$ change encoding, parameters, arrangement or ordering, 

Manipulation can also be used for selection. Components in the foreground can be highlighted by changing the color or other channels. Selection: hover (light), click (heavy).

Lastly, manipulation can be used for navigation to change the viewpoint $\rightarrow$ item reduction.

### Facet

Juxtapose shows views side-by-side, while partition has no strict dividing line. Superimpose consists of one or more dataset layers overlapping each other. Each layer should be visually distinguishable.

Superimpose is useful for reducing space; however, when there are too many layers, juxtapose may be better for clarity.


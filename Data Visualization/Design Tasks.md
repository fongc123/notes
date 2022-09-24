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

The <span style = "color:lightblue">analyze</span> category aims to create insights at a high level.

| **Sub-category** |          **Examples**           |
|:----------------:|:-------------------------------:|
|     Consume      | Discover, present, <u>enjoy</u> |
|     Produce      |    Annotate, record, derive     |

The <span style = "color:lightblue">consume</span> sub-category simply redistributes information, while the <span style = "color:lightblue">produce</span> sub-category displays additional operations and analysis (e.g., aggregation, simplification, dimensionality reduction).

The <span style = "color:lightblue">search</span> category aims to look into a group of points.

![[data-vis-actions-search.png|600]]

The <span style = "color:lightblue">query</span> category directly finds the value of a particular point or a group of points.
- <span style = "color:lightblue">identify</span>: query a specific point
- <span style = "color:lightblue">compare</span>: compare a trend with another
- <span style = "color:lightblue">summarize</span>: give an overview of all points

### Target

A <span style = "color:lightblue">target</span> refers to the subject of a task abstraction. **Trends**, **outliers**, and **features** can be found in all data.

In single-attribute data, the distribution or extreme values can be outlined. In data with multiple attributes, the similarity or correlation between datasets can be identified.

Specific to network and spatial data are topologies and shapes respectively.


## Interaction Design

<span style = "color:lightblue">Interactions</span> can be implemented to handle the increasing complexity of a dataset.
- <span style = "color:lightblue">manipulate</span>: change view over time
- <span style = "color:lightblue">facet</span>: facet across multiple views
- <span style = "color:lightblue">reduce</span>: reduce items or attributes in a single view

### Manipulate

A <span style = "color:lightblue">change over time</span> can be implemented by changing the **encoding**, the **parameters**, or the **arrangement** of a visualization. Here, the data and the attributes are identical, but the form has changed.

<span style = "color:lightblue">Selection</span> can also be implemented to highlight specific components of interest. It is a basic interaction for most visualizations. Selection channels include **color** and **motion**, where components can be selected by interval (1D brush or 2D brush), by hovering (lightweight), or by clicking (heavyweight).

> [!INFO]
> Multiple selection is typically done by shift-clicking or by automatically selecting similar components.

Lastly, <span style = "color:lightblue">navigation</span> changes the viewpoint and controls item visibility. Common navigation actions include **zooming**, **panning**, and **rotating**.
- <span style = "color:lightblue">slice</span>: show only items matching a specific value or are within a specific range of values
- <span style = "color:lightblue">cut</span>: show only items in a cut region
- <span style = "color:lightblue">project</span>: change mathematics of image creation (e.g., orthographic, perspective)

Interaction within a **single chart view** can be <span style = "color:lightblue">manipulated</span> manually or automatically.

### Facet

A visualization can be <span style = "color:lightblue">faceted</span> into multiple views.

<span style = "color:lightblue">Juxtaposed</span> views are shown side-by-side, where each view could convey different representations of the same dataset.

![[data-vis-facet-juxtapose.png|600]]

<span style = "color:lightblue">Partitioned</span> views are shown in the same chart, where there is no strict dividing line. Data can be split by **attributes**, **spatial proximity**, or **patterns**.

<span style = "color:lightblue">Superimposed</span> views consists of one or more dataset **layers** overlapping on the same chart. Each layer should be visually distinguishable.

> [!WARNING]
> Superimposed views are useful for space reduction; however, when there are too many layers, juxtaposed views may be better for clarity.

### Reduce

The items and attributes displayed can be reduced to highlight only the necessary components.

<span style = "color:lightblue">Filters</span> can specifically remove or include items or attributes. It is straightforward and intuitive; however, removed items may be forgotten.

<span style = "color:lightblue">Aggregation</span> can be performed to group or summarize items, but it is often difficult to avoid loss of data. In the two-dimensional density plot below, the raw data is aggregated into circles or squares.

![[data-vis-reduce-aggregate.png|600]]

>[!INFO]
>Aggregation should be logical, and important information (e.g., averages, standard deviations, uncertainties) should still be included.

<span style = "color:lightblue">Embedding</span> incorporates additional user interactions to combine information in a single view. Focus and context information are included in a single view, but length comparisons and object tracking may be impaired.

![[data-vis-reduce-embed.png|450]]

Distortion is used in the above chart.

### Benefits & Limitations

Some benefits of using interactions are listed below.
- flexible, powerful, and intuitive
- ease of exploration of data
- fluid task switching
- good support of animated transitions

However, there are some limitations of interactions.
- time cost
- cognitive load on previous state
- interaction controls require space
- interaction not as intended by designer

> [!WARNING]
> When switching views or data displays, it is difficult for users to compare the current visible item with an item from memory.

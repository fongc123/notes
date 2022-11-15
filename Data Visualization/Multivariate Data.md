<span style = "color:lightblue">Multivariate data</span> consists of data with **high dimensionality**, where the correlations between the attributes in the data are investigated.

| **Terminology**  |                **Definition**                |
|:----------------:|:--------------------------------------------:|
|    Dimensions    |         Key attributes (independent)         |
|    Variables     |         Value attributes (dependent)         |
| Multidimensional | Dimensionality of the independent dimensions |
|   Multivariate   |  Dimensionality of the dependent variables   |

The following approaches can be used to generate visualizations of multivariate data: **geometric projection**, **pixel-oriented** (i.e., layout density), **hierarchical display**, and **iconography**.

[[Data Preprocessing#Reduction|Dimensionality reduction]] techniques can be used to reduce the complexity of the data.

# Geometric Projection
In <span style = "color:lightblue">geometric projection</span>, multidimensional datasets are mapped to a dimensional or arbitrary space.

It can handle **large datasets** and can **detect outliers and correlation**; however, data attributes may not be **perceived equally** and **visual cluttering** may occur.

A <span style = "color:lightblue">scatter plot</span> (i.e., rectilinear) displays two attributes along the vertical and horizontal axes.

|          **Data**           |    **Mark**    |          **Channels**          |       **Task**        | **Scalability** |
|:---------------------------:|:--------------:|:------------------------------:|:---------------------:|:---------------:|
| Two quantitative attributes | Points | Position, color | Identify trends, outliers, distribution, correlation, and clusters | More points  |

Additionally, a <span style = "color:lightblue">scatter plot matrix (SPLOM)</span> displays a collection of scatter plots, where more attributes and items can be displayed. However, patterns in data with higher dimensions are harder to visualize.

![[data-vis-splom.png|600]]

For **cyclic** patterns, <span style = "color:lightblue">a polar plot</span> or <span style = "color:lightblue">star coordinates</span> (i.e., radial) can be used, where attributes emanate radically from the center of the circle.

![[data-vis-polar-plot.png|600]]

<span style = "color:lightblue">Parallel coordinates</span> perform cluster and correlation analysis using parallel lines.

|        **Data**         | **Mark** |  **Channels**   |             **Task**              | **Scalability** |
|:-----------------------:|:--------:|:---------------:|:---------------------------------:|:---------------:|
| Quantitative attributes |   Line   | Position, color | Identify correlation and clusters |   More lines   |

![[data-vis-parallel-coordinates.png|600]]

Here, attributes are laid out across the horizontal axis, where their values are scaled to a specified range (e.g., $-3$ to $4$ in the above example). Data items are represented by **polygonal lines**, where each intersection represents the attribute value of the item.
- Good for identifying correlations among attributes.
- Effective for revealing distributions and dependencies.
- Visual clutter for many data points.
- Axes become packed when dimensionality is high.

Alternatively, <span style = "color:lightblue">hierarchical parallel coordinates</span> transform distinct lines into a color band, where opacity can convey cluster population and color can convey proximity. <span style = "color:lightblue">Circular parallel coordinates</span> can also be considered.

# Layout Density
<span style = "color:lightblue">Pixel-oriented</span> or <span style = "color:lightblue">layout density</span> charts fill the entire chart space to achieve high information density; however, there may be an inefficient use of space.

Unlike [[Time Series#Heatmap|heatmaps in time series data]], heatmaps in multivariate data do not have a time axis.

|             **Data**              | **Mark** |     **Channels**     |           **Task**           |        **Scalability**        |
|:---------------------------------:|:--------:|:--------------------:|:----------------------------:|:-----------------------------:|
| Two categorical, one quantitative |   Area   | Color (quantitative) | Identify clusters & outliers | Discretize categorical values |

When encoding a quantitative variable by color, only a limited number of color shades can be distinguishable.

Additionally, a <span style = "color:lightblue">cluster heatmap</span> can be implemented, which combines the basic heatmap with matrix reordering based on a <span style = "color:lightblue">dendrogram</span>.

![[data-vis-cluster-heatmap.png|600]]

> [!INFO]
> A **dendrogram** shows the cluster hierarchy in a dataset. Data points that are most similar are paired together.
> 
> ![[data-vis-dendrogram.png|600]]

A <span style = "color:lightblue">table lens</span> uses the familiar concept of a tabular view to represent data items in rows and columns.

# Hierarchical Display
A <span style = "color:lightblue">hierarchical display</span> divides the data space and presents sub-spaces in a hierarchical fashion. It can effectively visualize hierarchical data, especially when certain attributes have higher importance than others. However, it implicitly views attributes differently.

A <span style = "color:lightblue">hierarchical axis</span> lays out axes horizontally, allowing multiple attributes to be displayed.

Similar to a [[#Geometric Projection|scatter plot matrix]], <span style = "color:lightblue">dimensional stacking</span> partitions the data space into two-dimensional sub-spaces, where dimensions are embedded within other dimensions. It is suitable for categorical or binned ordinal values.

![[data-vis-dimensional-stacking.png|600]]

In the above example, the dimensions are represented by $g$.

# Iconography
<span style = "color:lightblue">Iconography</span> maps each multidimensional data item to an icon or a glyph that contains several parameters.

![[data-vis-iconography.png|600]]

Several glyph designs are listed below.
- <span style = "color:lightblue">Star glyph</span>: items represented by a star glyph, where dimensions are represented as angular axes of the star (*similar to radar plots*)
- <span style = "color:lightblue">Chernoff faces</span>: attributes mapped to the properties of a face (e.g., face, nose, mouth, eyes)
- <span style = "color:lightblue">Text glyph</span>: uses textual characters as symbols
- <span style = "color:lightblue">Metaphor</span>: uses familiar objects (e.g., animals) as symbols
- <span style = "color:lightblue">Color icon</span>: combines pixel-based spiral axes and icon-based shape encoding, where color properties and orientation are used to map the data

> [!INFO]
> Texture can also be used as a glyph or symbol to encode data.

A **star glyph** example is shown below, where each item is represented by a glyph that contains seven attributes.

![[data-vis-star-glyph.png|600]]


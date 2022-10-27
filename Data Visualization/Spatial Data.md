<span style = "color:lightblue">Spatial data</span> is derived from geometry data that conveys shape from the position of its elements. All attributes have individual positions at adjustable levels of granularity (e.g., district, city, country).

<span style = "color:lightblue">Cartography</span> refers to the process of creating a map from geometry data. Due to the spherical property of the Earth, there are several ways to project geographic information on a two-dimensional chart.
- <span style = "color:lightblue">azimuthal</span>: preserve direction and distance from center
- <span style = "color:lightblue">equal-area</span>: preserve area
- <span style = "color:lightblue">conformal</span>: preserve local angles (i.e., shape)

> [!INFO]
> <span style = "color:lightblue">Tissot's indicatrix</span> is a tool to characterize **distortions due to projecting a spherical representation of the Earth onto a flat surface**. Each ellipse is an **indicatrix** and represents the distortion at the point where it is centered.

Additionally, the scale of the chart should also be adjusted according to the scope of the data.

Additional non-conventional chart types include **transit maps**, which are used for transportation maps, and **prism maps**, which create a [[Design Rules#3D|justified three-dimensional]] view of a map.

# Choropleth
A <span style = "color:lightblue">choropleth map</span> categorically encodes different regions on a map by color.

|                           **Data**                            | **Mark** |           **Channels**           |             **Task**             | **Scalability** |
|:-------------------------------------------------------------:|:--------:|:--------------------------------:|:--------------------------------:|:---------------:|
| Geographic geometry & quantitative attribute |   Area   | Map (area) & color for attribute | Understand spatial relationships | Multiple colors                |

This map is scalable to diverging colors (e.g., bivariate or multidimensional) or smaller map partitions (i.e., regions). A single-variate choropleth map is shown below.

![[data-vis-choropleth.png|600]]

# Symbol
A <span style = "color:lightblue">symbol map</span> encodes the quality or quantity (i.e., density) of spatial regions with marks and symbols. Examples include **dot map** (*dots*), **bubble map** (*bubbles*), **spatial heatmap** (*area*), and **isoline map** (*an alternative heatmap*).

|                       **Data**                       |    **Mark**    |             **Channels**              |             **Task**             | **Scalability** |
|:----------------------------------------------------:|:--------------:|:-------------------------------------:|:--------------------------------:|:---------------:|
| Geography & categorical or quantitative attribute(s) | Area & symbols | Map (area) & symbols for attribute(s) | Understand quantity & quality of regions | Multiple symbols |

A dot map is shown below.

![[data-vis-dot-map.png|600]]

In dense datasets, visual occlusion may occur, which may affect the representation of the data.

# Cartogram
A <span style = "color:lightblue">cartogram</span> is an alternative to [[#Choropleth|choropleth maps]] and distorts geographical regions to directly use area to encode attributes.

|                       **Data**                       |    **Mark**    |             **Channels**              |             **Task**             | **Scalability** |
|:----------------------------------------------------:|:--------------:|:-------------------------------------:|:--------------------------------:|:---------------:|
| Approximate geographic geometry & categorical attribute | Area | Position, size, color | Alternative to choropleth or symbol map | Multiple colors |

There are several types of cartograms. In <span style = "color:lightblue">graphical cartograms</span>, shapes and circles are used to depict shape and area. On the other hand, in <span style = "color:lightblue">non-contiguous cartograms</span>, features can have any shape and do not have to stay connected.

Lastly, in <span style = "color:lightblue">contiguous (density-equalizing) cartograms</span>, map feature polygons are resized based on a variable, where each feature is connected. A cartogram of the electoral college results is shown below.

![[data-vis-cartogram.png|600]]

> [!WARNING]
> Major distortions should still be recognizable.

# Flow
In a <span style = "color:lightblue">flow map</span>, lines are used to show movement between spatial regions rather than symbols or color.

|                       **Data**                       |    **Mark**    |             **Channels**              |             **Task**             | **Scalability** |
|:----------------------------------------------------:|:--------------:|:-------------------------------------:|:--------------------------------:|:---------------:|
|  Geography & connections | Line | Position, length, color | Show spatial movement | Multiple lines |

Visual cluttering is especially prevalent in this chart type.

![[data-vis-flow.png|600]]

This example (https://hint.fm/wind/) is a wind map of the United States.


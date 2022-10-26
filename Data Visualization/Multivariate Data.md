<span style = "color:lightblue">Multivariate data</span> consists of data with **high dimensionality**, where the correlations between the attributes in the data are investigated.

| **Terminology**  |                **Definition**                |
|:----------------:|:--------------------------------------------:|
|    Dimensions    |         Key attributes (independent)         |
|    Variables     |         Value attributes (dependent)         |
| Multidimensional | Dimensionality of the independent dimensions |
|   Multivariate   |  Dimensionality of the dependent variables   |

The following approaches can be used to generate visualizations of multivariate data: **geometric projection**, **pixel-oriented** (i.e., layout density), **hierarchical display**, and **iconography**.

# Geometric Projection
In <span style = "color:lightblue">geometric projection</span>, multidimensional datasets are mapped to a dimensional or arbitrary space.

It can handle **large datasets** and can **detect outliers and correlation**; however, data attributes may not be **perceived equally** and **visual cluttering** may occur.

A <span style = "color:lightblue">scatter plot</span> displays two attributes along the vertical and horizontal axes.

|          **Data**           |    **Mark**    |          **Channels**          |       **Task**        | **Scalability** |
|:---------------------------:|:--------------:|:------------------------------:|:---------------------:|:---------------:|
| Two quantitative attributes | Points | Position, color | Identify trends, outliers, distribution, correlation, and clusters | More points  |

Additionally, a <span style = "color:lightblue">scatter plot matrix (SPLOM)</span> displays a collection of scatter plots, where more attributes and items can be displayed. However, patterns in data with higher dimensions are harder to visualize.

For cyclic patterns, <span style = "color:lightblue">a polar plot</span> or <span style = "color:lightblue">star coordinates</span> can be used, where attributes emanate radically from the center of the circle.

<span style = "color:lightblue">Parallel coordinates</span> perform cluster and correlation analysis using parallel lines.

Scatter plot, radical coordinates, star coordinates, parallel coordinates.
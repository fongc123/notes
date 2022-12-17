A <span style = "color:lightblue">feature</span> is a distinctive attribute or description of an object that can be **labeled** or **differentiated**. <span style = "color:lightblue">Feature detection</span> aims to find features in an image, while <span style = "color:lightblue">feature description</span> assigns quantitative attributes to the features.
- <span style = "color:lightblue">Boundary-based features</span>: pertaining to the outlining border
- <span style = "color:lightblue">Region-based features</span>: pertaining to the properties within a region

> [!INFO]
> A good feature descriptor should be invariant to scale, transition, rotation, illumination, viewpoint, etc. (*see [[Interpolation & Transformation|affine]] and [[Intensity Transformations|intensity]] transformations*).


# Boundary Features
There are several <u>basic</u> measures to describe the boundary of a feature.
- <span style = "color:lightblue">length</span>: the number of pixels along a boundary
- <span style = "color:lightblue">diameter</span>: the maximum distance between any two points on a boundary
- <span style = "color:lightblue">major axis</span>: the magnitude and the orientation (i.e., slope) of the diameter
	- **Points:** $(x_1,y_1)$ and $(x_2,y_2)$ (*extreme points*)
	- **Magnitude:** [[Clustering#Similarity|Euclidean distance]]
	- **Orientation:** $\theta=tan^{-1}\left[\frac{y_2-y_1}{x_2-x_1}\right]$
- <span style = "color:lightblue">minor axis</span>: the line **perpendicular** to the major axis with a **certain length** such that a box (i.e., a <span style = "color:lightblue">bounding box</span>) passing through all four points of the major and minor axes completely encloses the boundary
- <span style = "color:lightblue">curvature</span>: the overall rate of change of the slope
- <span style = "color:lightblue">tortuosity</span>: a measure of the twists and turns of a curve
	- $\tau=\sum_{i=1}^{n}|a_i|$
		- $n$: the number of elements
		- $a_i$: the values (i.e., slope changes) of the elements

The example below uses tortuosity to describe blood vessel morphology.

![[image-processing-tortuosity.png|600]]

A larger tortuosity ($\tau$) corresponds to a more crooked object.

The <span style = "color:lightblue">statistical moment</span> is a descriptor applicable to one-dimensional renderings of two-dimensional boundaries. For example, the **distances** from the boundary center to the boundary edge can be compared with the **angle** (i.e., <span style = "color:lightblue">distance-versus-angle signatures</span>).

![[image-processing-statistical-moment.png|600]]

The $n$th moment of $z

This may improve the characterization of boundaries.


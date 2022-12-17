A <span style = "color:lightblue">feature</span> is a distinctive attribute or description of an object that can be **labeled** or **differentiated**. <span style = "color:lightblue">Feature detection</span> aims to find features in an image, while <span style = "color:lightblue">feature description</span> assigns quantitative attributes to the features.
- <span style = "color:lightblue">Boundary-based features</span>: pertaining to the outlining border
- <span style = "color:lightblue">Region-based features</span>: pertaining to the properties within a region

> [!INFO]
> A good feature descriptor should be invariant to scale, transition, rotation, illumination, viewpoint, etc. (*see [[Interpolation & Transformation|affine]] and [[Intensity Transformations|intensity]] transformations*).


# Boundary Features
There are several <u>basic</u> measures to describe the boundary of a feature.
- <span style = "color:lightblue">length</span>: number of pixels along a boundary
- <span style = "color:lightblue">diameter</span>: maximum distance between any two points on a boundary
- 
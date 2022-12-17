A <span style = "color:lightblue">feature</span> is a distinctive attribute or description of an object that can be **labeled** or **differentiated**. <span style = "color:lightblue">Feature detection</span> aims to find features in an image, while <span style = "color:lightblue">feature description</span> assigns quantitative attributes to the features.
- <span style = "color:lightblue">Boundary-based features</span>: pertaining to the outlining border
- <span style = "color:lightblue">Region-based features</span>: pertaining to the properties within a region

> [!INFO]
> A good feature descriptor should be invariant to scale, transition, rotation, illumination, viewpoint, etc. (*see [[Interpolation & Transformation|affine]] and [[Intensity Transformations|intensity]] transformations*).


# Boundary Features
There are several <u>basic</u> measures to describe the boundary of a feature.
- <span style = "color:lightblue">length</span>: the number of pixels along a boundary (i.e., perimeter)
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

## Statistical Moments

The <span style = "color:lightblue">statistical moment</span> is a descriptor applicable to one-dimensional renderings of two-dimensional boundaries. For example, the **distances** from the boundary center to the boundary edge can be compared with the **angle** (i.e., <span style = "color:lightblue">distance-versus-angle signatures</span>).

![[image-processing-statistical-moment.png|600]]

The expression for the $n$th moment of $z$ (i.e., the **discrete random variable** of the amplitude of $g$) about its mean is shown below. In the diagram above, $z$ would represent the distance.

$$
\begin{gather}
\mu_n(z)=\sum_{i=0}^{A-1}(z_i-m)^np(z_i) \\
m=\sum_{i=0}^{A-1}z_ip(z_i)
\end{gather}
$$

Generally, only the first few moments ($n\in[0,3]$) are required to differentiate between signatures of clearly distinct shapes.

# Region Features
Similarly, there are several <u>basic</u> features to describe the region of a feature. Here, $\rho$ represents the perimeter (i.e., the length of the boundary), while $A$ represents the area (i.e., the number of pixels in the region).
- <span style = "color:lightblue">compactness</span>: the size of the region
$$\text{compactness}=\frac{\rho^2}{A}$$
- <span style = "color:lightblue">circularity</span>: the roundness of the region
$$\text{circularity}=\frac{4\pi A}{\rho^2}$$
- <span style = "color:lightblue">eccentricity</span>: the ratio of the distance between the foci and the length of the major axis

$$\text{eccentricity}=\frac{c}{a}=\frac{\sqrt{a^2-b^2}}{a}=\sqrt{1-\left(\frac{b}{a}\right)^2}\quad\text{where}\space a\geq b$$

An example of eccentricity is shown below.

![[image-processing-eccentricity.png|600]]

Instead of a bounding box, an ellipse is used to approximate the region to calculate eccentricity. A comparison between the three feature descriptors is shown below.

![[image-processing-region-feat-comparisons.png|600]]

Eccentricity describes the **centrality** of an object. Due to [[Acquisition & Representation#Digitization|digitization]], the eccentricity values for the circle and the star are non-zero.

> [!INFO]
> Objects can be mapped onto an $n$-dimensional space, where $n$ is the number of features, to compare the similarity between objects based on selected features.

<span style = "color:lightblue">Topological features</span> study the properties of an object that are unaffected by deformation given that there is no tearing or joining of the object (i.e., <span style = "color:lightblue">rubber-sheet distortions</span>).
$$\text{Euler number}=\text{no. of connecte}$$
Unlike previous [[Intensity Transformations|transformations]], [[Spatial Filtering|spatial filtering]], and [[Frequency Filtering|frequency filtering]], this section describes image processing with colored images instead of only grayscale images (*see [[Color|color]] and [[Acquisition & Representation#Human Visual System|human visual system]]*).

There are two types of color image processing.
- <span style = "color:lightblue">pseudocolor image</span>: assigning colors to gray values
- <span style = "color:lightblue">full color image</span>: manipulating colored images

# Pseudocolor Processing
Humans can distinguish different colors better than different shades of gray, as found in medical images. Additionally, pseudocolor processing can be used when giving color to originally grayscale images.

$$\text{if }f(x,y)\in I_k,\text{ let }f(x,y)=c_k$$

<span style = "color:lightblue">Intensity slicing</span> can be performed to assign pixels within above the threshold $I_k$ one color and pixels below the threshold $I_k$ another color. Alternatively, <span style = "color:lightblue">multi-level intensity slicing</span> maps multiple intensity ranges to multiple colors.

![[image-processing-pseudocolor.png|600]]

> [!INFO]
> Satellite imagery is originally in grayscale. Due to pseudocolor processing, however, color can be added to the image of the Earth.

# Full Color Image Processing
In <span style = "color:lightblue">full color image processing</span>, each color component is processed separately (i.e., per-color-component processing). For example, a colored image can be smoothened by smoothing each RGB component individually.

$$
\begin{gather}
	g(x,y)=T\left[f(x,y)\right] \\\\
	s_i=T_i(r_i)\quad \text{for }i=1,2,3
\end{gather}
$$
In the equations above, $f$ and $g$ represent the colored input and output images respectively, where the transformation $T$ is performed for each component $i$.

## Color Slicing Transformation
<span style = "color:lightblue">Color slicing transformations</span> slice specific colors from an image based on a range, where colors outside the range of interest are set to a neutral color.

$$
\begin{align}
	\text{cube-based region:}&\quad
	s_i=\begin{cases}
		0.5 & \text{if }r_j-a_j>W/2 \\
		r_i & \text{otherwise}
	\end{cases} \\\\
	\text{sphere-based region:}&\quad 
	s_i=\begin{cases}
		0.5 & \text{if }\sum_{j=1}^{n}\left(r_j-a_j\right)^2>R_0^2 \\
		r_i & \text{otherwise}
	\end{cases}
\end{align}
$$

Here, $a$ represents the prototypical centers of each color component (red, green, blue). An example of color slicing is shown below, where the red colors are sliced.

![[image-processing-color-slicing.png|600]]

## Full-color Histogram Equalization
Similar to [[Intensity Transformations#Histogram Equalization|grayscale histogram equalization]], the color intensities are equally distributed across all levels. **The HSI model must be used, as the colors should remain unchanged.** An example is shown below.

![[image-processing-color-hist-eq.png|600]]

In the above image, the saturation is also increased in the bottom right sub-image.
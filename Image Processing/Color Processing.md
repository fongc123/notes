Unlike previous [[Intensity Transformations|transformations]], [[Spatial Filtering|spatial filtering]], and [[Frequency Filtering|frequency filtering]], this section describes image processing with colored images instead of only grayscale images (*see [[Color|color]] and [[Acquisition & Representation#Human Visual System|human visual system]]*).

There are two types of color image processing.
- <span style = "color:lightblue">pseudocolor image</span>: assigning colors to gray values
- <span style = "color:lightblue">full color image</span>: manipulating colored images

> [!INFO]
> [[Image Restoration#Modeling Noise|Noise]] is less noticeable in colored images. This is because noise gets reduced when there are multiple images. Since there are three images (one for each channel), the result due to averaging is less noisy.

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
	s_i=\begin{dcases}
		0.5\vphantom{\frac{0}{0}} & \text{if }r_j-a_j>W/2 \\
		r_i\vphantom{\frac{0}{0}} & \text{otherwise}
	\end{dcases} \\\\
	\text{sphere-based region:}&\quad 
	s_i=\begin{dcases}
		0.5\vphantom{\frac{0}{0}} & \text{if }\sum_{j=1}^{n}\left(r_j-a_j\right)^2>R_0^2\\
		r_i\vphantom{\frac{0}{0}} & \text{otherwise}
	\end{dcases}
\end{align}
$$

Here, $a$ represents the prototypical centers of each color component (red, green, blue). An example of color slicing is shown below, where the red colors are sliced.

![[image-processing-color-slicing.png|600]]

## Full-color Histogram Equalization
Similar to [[Intensity Transformations#Histogram Equalization|grayscale histogram equalization]], the color intensities are equally distributed across all levels. **The HSI model must be used, as the colors should remain unchanged.** An example is shown below.

![[image-processing-color-hist-eq.png|600]]

In the above image, the saturation is also increased in the bottom right sub-image.

## Color Image Smoothing
Similar to spatial image smoothing by [[Spatial Filtering#Low-pass Filters|low-pass filters]] and [[Image Restoration|mean (and order-statistic) filters]], color image smoothing can be done by averaging pixel values in a specified filter region.
- <span style = "color:lightblue">per-color plane method</span>: for RGB and CMY models, smooth each color component and combine each component back
- <span style = "color:lightblue">intensity-only</span>: for HSI model, smooth only intensity component and leave hue and saturation unmodified

$$
\bar{\mathcal{c}}(x,y)=\begin{bmatrix}
	\frac{1}{K}\sum_{s,t\in S_{xy}}{R(s,t)} \\
	\frac{1}{K}\sum_{s,t\in S_{xy}}{G(s,t)} \\
	\frac{1}{K}\sum_{s,t\in S_{xy}}{B(s,t)}
\end{bmatrix}
$$

> [!INFO]
> The per-color plane and intensity-only methods are not equivalent. The results obtained from these methods are different.

In the example below, the result of smoothing all RGB components is shown on the left, while that of smoothing only the intensity component is shown in the middle. The difference between the two images is shown on the right.

![[image-processing-color-img-smoothing.png|600]]

## Color Image Sharpening
Similar to [[Spatial Filtering#High-pass Filters|high-pass filters]], color image sharpening can be achieved with the Laplacian filter. Again, all RGB components or only the intensity component can be sharpened.

$$
\nabla^2 \left[\bar{\mathcal{c}}(x,y)\right]=
\begin{bmatrix}
	\nabla^2{R(x,y)} \\
	\nabla^2{G(x,y)} \\
	\nabla^2{B(x,y)}
\end{bmatrix}
$$

![[image-processing-color-img-sharpening.png|600]]

## Color Segmentation
In <span style = "color:lightblue">color segmentation</span>, a threshold function based on **color information** in the hue and saturation components is implemented, where $\mathcal{c}_T$ represents the color to be segmented and $c(x,y)$ is the RGB vector at a pixel.

$$
g(x,y)=\begin{dcases}
	1 & \text{if }D(\mathcal{c}(x,y), \mathcal{c}_T)\leq T \vphantom{\frac{0}{0}}\\
	0 & \text{if }D(\mathcal{c}(x,y), \mathcal{c}_T)>T \vphantom{\frac{0}{0}}
\end{dcases}
$$

The distance between the pixel's color and the target color is calculated, and only the pixels within the distance threshold are set to $1$.

![[image-processing-color-segmentation.png|600]]

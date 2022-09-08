# Intensity Transformations

Specific parts of the image can be enhanced or diminished based on the use case (e.g., for clarity). Primarily, the focus of image transformations is on <u>grayscale images</u>.

<span style = "color:lightblue">Intensity transformations (gray-level mapping)</span> changes the intensity level of an image based on an intensity transformation or mapping function. An equation is shown below, where $r$ is the input intensity, $s$ is the output intensity, and $T$ is the mapping function.

$$
s = T(r)
$$

It is usually implemented in a <span style = "color:lightblue">look-up table (LUT)</span> (a query table) for maximum efficiency.

## Basic Transformations

Some basic transformations are listed below.

### Threshold
A <span style = "color:lightblue">threshold</span> function, where the original intenxity level will be retained or lossed before or after a certain point.
$$
s=
\begin{cases}
	0 & r < T
	\newline
	L-1 & r > T
\end{cases}
$$
The output is <span style = "color:lightblue">binary</span> and is used in <span style = "color:lightblue">pattern recognition</span> or <span style = "color:lightblue">object detection</span>.

![[image-processing-transform-threshold.png|400x200]]

### Negative
A <span style = "color:lightblue">negative</span> transformation inverts the intensity levels (i.e., black becomes white).

$$s = L - 1 - r$$
White or grey details embedded in black regions create more contrast after a negative transformation has been applied.

![[image-processing-transform-negative.png|400x200]]

### Log Transformation
An <span style = "color:lightblue">logarithmic</span> transformation maps a **narrow range of low intensity values** in the input to a wider range of output levels. <u>The low intensity values are stretched, while the high intensity values are compressed</u>.
$$s = c \log(1 + r)$$
![[image-processing-transform-log.png|400x200]]

The details in low intensity values are more expressed.

### Power-law Transformations

<span style = "color:lightblue">Power-law transformations</span> are similar to logarithmic transformations; however, the effect of the transformation changes based on the $\gamma$ parameter.

$$s = cr^{\gamma}$$
For transformations with $\gamma < 1$, the transformation will stretch low intensity levels and compress high intensity values. It **preserves details with low intensity values**. At low $\gamma$ values, the image becomes increasingly light (i.e., <span style = "color:lightblue">wash-out effect</span>).

![[Pasted image 20220908135403.png|600x200]]

For transformations with $\gamma > 1$, the transformation will stretch high intensity values and compress low intensity values. It **shows more details and greater contrast**.

![[Pasted image 20220908135509.png|600x200]]

#### Gamma Correction
With the power-law transformation, the <span style = "color:lightblue">power law effect</span> can be corrected using <span style = "color:lightblue">gamma correction</span> or <span style = "color:lightblue">gamma encoding</span>. Both low and high intensity values can be stretched or compressed based on the image.

For example, an image that is **corrected** to a gamma value of $\frac{1}{\gamma_0}$ will look **normal** on a monitor that naturally displays images with a gamma value of $\gamma_0$.



## Piece-wise Linear Transformations
- Contrast stretching: specifically expand the range of intensity values
- Intensity-level slicing: highlight a specific range of intensities

## Bit-plane Transformation
<span style = "color:lightblue">Bit-plane slicing</span> is the representation of each pixel in binary, where a binary image is constructed for each bit. For example, an image with 256 intensity levels is represented as an 8 bit-plane image.

<span style = "color:lightblue">High-order bit-planes</span> contain the most visually-significant data, while <span style = "color:lightblue">lower-order bit-planes</span> contribute to the subtle intensity details.

Applications:
- image compression $\rightarrow$ with only bit-planes 8 and 7, both modified and original images are similar
- digital watermarking $\rightarrow$ hide information digitally in low bit-planes

## Histogram Equalization
When performing <span style = "color:lightblue">histogram equalization</span>, the inverse is not considered. A single value can be mapped to multiple values and vice versa.

However, it may increase the contrast of background noise, while decreasing useful signal or it can remove small details.
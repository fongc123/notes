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


### Negative
The intensity levels are inverted (i.e., black becomes white).

### Log Transformation
A *log* transformation maps a narrow range of low intensity values in the input to a wider range of output levels. The low intensity values are stretched, while the high intensity values are compressed.

$$c \log(1 + r)$$
## Power-law Transformations
$$s = cr^{\gamma}$$
Similar to log transformations. For transformations with $\gamma < 1$, the transformation will stretch low intensity levels and compress high intensity values. It **preserves details with low intensity values**. At low $\gamma$ values, the image becomes increasingly light.

For transformations with $\gamma > 1$, the transformation will stretch high intensity values and compress low intensity values. It **shows more details and greater contrast**.

### $\gamma$ Correction
With the power-law transformation, the <span style = "color:lightblue">power law effect</span> can be corrected using <span style = "color:lightblue">gamma correction</span> or <span style = "color:lightblue">gamma encoding</span>. Both low and high intensity values can be stretched or compressed based on the image.

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
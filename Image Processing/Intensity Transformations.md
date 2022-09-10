# Intensity Transformations

Specific parts of the image can be enhanced or diminished based on the use case (e.g., for clarity). Primarily, the focus of image transformations is on <u>grayscale images</u>.

<span style = "color:lightblue">Intensity transformations (gray-level mapping)</span> changes the intensity level of an image based on a mapping function. An equation is shown below, where $r$ is the input intensity, $s$ is the output intensity, and $T$ is the mapping function.

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

![[image-processing-transform-gamma-1.png|600x200]]

For transformations with $\gamma > 1$, the transformation will stretch high intensity values and compress low intensity values. It **shows more details and greater contrast**.

![[image-processing-transform-gamma-2.png|600x175]]

#### Gamma Correction
With the power-law transformation, the <span style = "color:lightblue">power law effect</span> can be corrected using <span style = "color:lightblue">gamma correction</span> or <span style = "color:lightblue">gamma encoding</span>. Both low and high intensity values can be stretched or compressed based on the image.

For example, an image that is **corrected** to a gamma value of $\frac{1}{\gamma_0}$ will look **normal** on a monitor that naturally displays images with a gamma value of $\gamma_0$.

![[image-processing-transform-gamma-3.png|600x250]]

### Piece-wise Linear Transformations

A <span style = "color:lightblue">piece-wise linear transformation</span> is an upgraded version of the threshold function, allowing greater customizability. Specific intensity levels can be selected or discarded.
- <span style = "color:lightblue">contrast stretching</span>: specifically expand the range of intensity values
- <span style = "color:lightblue">intensity-level slicing</span>: highlight a specific range of intensities

![[image-processing-transform-piece.png|600x250]]

The above image shows intensity-level slicing, where only the light-grey portions of the image are highlighted.

### Bit-plane Transformation
<span style = "color:lightblue">Bit-plane slicing</span> is the representation of each pixel in binary, where a binary image is constructed for each bit. For example, an image with 256 intensity levels is represented as an 8 bit-plane image.

![[image-processing-transform-bitplane.png|600x300]]

> [!INFO]
> In the above example, only bit-planes 7 and 8 make visual sense, while bit-planes 1 to 6 are simply noise.

<span style = "color:lightblue">High-order bit-planes</span> contain the most visually-significant data, while <span style = "color:lightblue">lower-order bit-planes</span> contribute to the subtle intensity details.

Some applications of bit-plane transformations are described below.
- <span style = "color:lightblue">image compression</span>: other bit-planes that do not significantly contribute to the image can be removed
- <span style = "color:lightblue">digital watermarking</span>: information can be digitally hidden in low bit-plane levels

## Histogram Processing

A <span style = "color:lightblue">histogram</span> displays the **pixel intensity distribution** of all pixels in an image . Intensity values with values ranging from $0$ to $L-1$ must first be normalized.

$$p(r_k)=\frac{h(r_k)}{MN}$$
In the above equation, $p$ is the normalized intensity values, $h$ is the unnormalized intensity values, $M$ is the number of rows, and $N$ is the number of columns.

![[image-processing-histogram-process.png|600x300]]

The histogram of a high-contrast image has a wide and uniform range of intensity values.

### Histogram Equalization

<span style = "color:lightblue">Histogram equalization</span> is a contrast adjustment using the image's original histogram, where the modified image will have an equal number of pixels at each grey level. The transformation function $s$ should satisfy the following criteria.
- $T(r)$ is monotonically increasing
- $0 \leq T(r) \leq L - 1$ between $0$ and $L-1$ inclusive

![[image-processing-histogram-eq-1.png|600x300]]

>[!INFO]
>When performing histogram equalization, the inverse is not considered. A single value can be mapped to multiple values and vice versa.

#### Derivation
The intensity of an image is viewed as a <span style = "color:lightblue">random variable</span> between $0$ and $L-1$.

$$
\begin{gather}
	s=T(r) \\
	p_s(s)=p_r(r) |\frac{dr}{ds}|
\end{gather}
$$
- $p_s(s)$: <span style = "color:lightblue">probability density function (PDF)</span> of output intensity value $s$
- $p_r(r)$: PDF of input intensity value $r$
- the differentiation attempts to maps low and high intensity values equally

> [!INFO]
> A random variable can be an arbitrary set of numbers.

A <span style = "color:lightblue">cumulative distribution function (CDF)</span> is assumed (i.e., the output is assumed to be uniformly distributed).
$$s = T(r)=(L-1)\int_{0}^{r}{p_r(\omega)d\omega}$$
The transformation function is differentiated.
$$
\begin{align}
	\frac{ds}{dr} & = \frac{dT(r)}{dr} \\
	& = (L - 1)\frac{d}{dr}\int_{0}^{r}{p_r(\omega)d\omega} \\
	& = (L - 1)p_r(r)
\end{align}
$$
The expression for the differentiation of $s$ with respect to $r$ is substituted into the original equation.
$$
\begin{align}
	p_s(s) & = p_r(r) | \frac{dr}{ds}| \\
	& = p_r(r) \frac{1}{p_r(r)(L - 1)} \\
	& = \frac{1}{L - 1}
\end{align}
$$
The result is a **uniform distribution**. In a discrete image, probabilities and summations are used instead of probability density functions and integrals.

$$
s_k=T(r_k)=(L-1)\sum_{j=0}^{k}{\frac{n_j}{MN}},\space k=0,1,...,L-1
$$

#### Result
The output is a relatively uniform histogram. Equalization may not create a perfectly uniform histogram, but it helps span the histogram to a **wider range of intensity scales**.

![[image-processing-histogram-eq-2.png|600x200]]

However, it may increase the contrast of background noise, while decreasing useful signal or it can remove small details.
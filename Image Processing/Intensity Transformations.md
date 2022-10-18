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

A <span style = "color:lightblue">histogram</span> displays the **pixel intensity distribution** of all pixels in an image. Intensity values with values ranging from $0$ to $L-1$ must first be normalized.

$$p(r_k)=\frac{h(r_k)}{MN}$$
In the above equation, $p$ is the normalized intensity values, $h$ is the unnormalized intensity values, $M$ is the number of rows, and $N$ is the number of columns.

![[image-processing-histogram-process.png|600x300]]

The histogram of a high-contrast image has a wide and uniform range of intensity values.

### Histogram Equalization

<span style = "color:lightblue">Histogram equalization</span> is a contrast adjustment using the image's original histogram, where the modified image will have an equal number of pixels at each gray level. The transformation function $s$ should satisfy the following criteria.
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
The output is a uniform histogram. In a discrete image, equalization does not create a perfectly uniform histogram. Overall, the equalization distributes the values over **a wider range of intensities**.

![[image-processing-histogram-eq-2.png|600x200]]


> [!WARNING]
> Histogram equalization may increase the contrast of background noise, while decreasing useful signals or removing small details.

### Histogram Matching

<span style = "color:lightblue">Histogram matching</span> is the transformation of an image such that the its histogram matches a specified histogram. It may help in showing more picture details.

![[image-processing-histogram-matching.png|600x175]]

The histogram equalizations of both the **input image** and the **target image** are found and are equated together.

In the case when a direct matching is impossible, the **closest** $z_q$ value will be mapped instead.

#### Derivation
The continuous probability function of the image intensity values $r$ is represented as $p_r(r)$.

$$
s = (L-1)\int_0^r{p_r(r)dw}
$$

The specified probability function of the target histogram intensity values $z$ is represented as $p_z(z)$. The transformation function is represented as $G(z)$.

$$
G(z)=(L-1)\int_0^z{p_z(z)dt}
$$

To perform matching and mapping, the expressions of $s$ and $G(z)$ are equated together.

$$
\begin{align}
	G(z) & = s \newline
	\therefore z & =G^{-1}(s) \newline
	& = G^{-1}[T(r)]
\end{align}
$$

The output image with $z$ values is mapped to the values of the specified histogram. In the discrete case, the integrals are replaced with summations.

$$
\begin{align}
	s_k & = T(r_k)=(L-1)\sum_{j=0}^{k}{p_r(r_j)}=\frac{L-1}{MN}\sum_{j=0}^{k}{n_j} \newline
	G(z_q) & = (L-1)\sum_{i=0}^{q}{p_z(z_i)}=s_k \newline
	z_q&=G^{-1}(s_k)
\end{align}
$$

#### Example

The probability distribution function of the original image $p_r(r)$ and the target probability distribution function $p_z(z)$ are shown below.

$$
\begin{align}
	p_r(r) & =
	\begin{dcases}
		\frac{2r}{(L-1)^2} & \text{for}\space 0\leq r\leq L-1 \\\
		0\vphantom{\frac{0}{0}} & \text{otherwise}
	\end{dcases}
	\newline
	p_z(z) & =
	\begin{dcases}
		\frac{3z^2}{(L-1)^3} & \text{for} \space 0 \leq z \leq L-1 \\\
		0\vphantom{\frac{0}{0}} & \text{otherwise}
	\end{dcases}
\end{align}
\newline
$$

The transformation $z=f(r)$ to match the original image to the specified probability distribution is found. First, the histogram equalization of the input image $s$ is found.

$$
\begin{align}
	s & = T(r) \newline
	& = (L-1)\int_0^r{p_r(r)dw} \newline
	& = (L-1)\int_0^r{\frac{2w}{(L-1)^2}dw} \newline
	s & = \frac{r^2}{L-1}
\end{align}
$$

Next, the histogram equalization of the target histogram $G(z)$ is found.

$$
\begin{align}
	G(z) & = (L-1)\int_0^z{p_z(t)dt} \newline
	& = (L-1)\int_0^z{\frac{3t^2}{(L-1)^3}dt} \newline
	G(z) & = \frac{z^3}{(L-1)^2}
\end{align}
$$

Both histogram equalizations are equated with each other, and an expression for $z$ is found.

$$
\begin{align}
	s & = G(z) \newline
	\frac{r^2}{L-1} & = \frac{z^3}{(L-1)^2} \newline
	z^3 & = (L-1)r^2 \newline
	z & = (L-1)^{\frac{1}{3}}r^{\frac{2}{3}} \newline
\end{align}
$$

> [!TIP]
> If the function is simple (e.g., linear), the expression of the probability distribution function can be obtained from the graph.

#### Result

The resulting image should roughly have the same histogram distribution as the target image.

The figure below demonstrates the differences between histogram equalization and histogram matching. The image produced by histogram matching is more favorable; thus, histogram equalization may not always be the best processing method to use.

![[image-processing-histogram-matching-2.png|600x360]]

## Local Histogram Equalization

The histogram equalization performed in [[#Histogram Equalization]] is global which is suitable for **overall enhancement**. However, it cannot enhance **local details**, as small areas have negligible influence on global transformations.

In <span style = "color:lightblue">local histogram equalization</span>, the intensity distribution is defined in a local neighborhood around a center pixel instead of the entire image. The center pixel's values are modified to match its local neighborhood.

![[image-processing-local-histogram-eq.png|600x200]]

The effect of this method is similar to that of gamma correction.


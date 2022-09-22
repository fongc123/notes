# Spatial Filtering

<span style = "color:lightblue">Spatial filtering</span> modifies an image by replacing each pixel value with the output from a function that relies on the value of the pixel and the values of the neighboring pixels. A <span style = "color:lightblue">spatial filter</span> consists of a neighborhood (*the kernel*) and a predefined operation $T$.

## Linear Spatial Filtering

A <span style = "color:lightblue">linear spatial filter</span> performs a sum-of-products operation between an image $f$ and a filter kernel $w$. A filter is linear if the operation $T$ it performs is also linear. The expression for the <span style = "color:lightblue">correlation</span> of a filter $w$ with an image $f$ is shown below.

$$w(x,y)\bigstar f(x,y)=\sum_{s=-a}^a\sum_{t=-b}^b{w(s,t)f(x+s,y+t)}$$

The expression for the <span style = "color:lightblue">convolution</span> of a filter $w$ with an image $f$ is shown below. The filter $w$ is rotated by 180$^\circ$.

$$w(x,y)\star f(x,y)=\sum_{s=-a}^a\sum_{t=-b}^b{w(s,t)f(x-s,y-t)}$$

The <span style = "color:lightblue">impulse response</span> of correlation is a rotation of the filter by 180$^{\circ}$. In spatial convolution, since the filter is rotated beforehand, the impulse response is identical to the filter.

### Zero-padding

To perform a sum-of-products operation on pixels close to or at the image margins, additional zeros are padded. For example, in a one-dimensional signal, an image with original length of $M$ would create a correation result of length $M$ but a **full correlation result** of length $M + 2a$.

![[image-processing-1d-padding.png|275]]

In a two-dimensional signal, an image with size $(M,N)$ would create a **full correlation result** with size $(M+2a,N+2b)$.

![[image-processing-2d-padding.png|350]]

### Properties

The properties for convolution and correlation are shown in the table below.

![[image-processing-conv-corr-prop.png|600]]

### Separable Filter Kernels

A two-dimensional <span style = "color:lightblue">separable filter kernel</span> can be written as a product of two one-dimensional kernels.

$$w(x,y) = w(x)w(y)$$
An example of a separable filter is shown below.

$$
\begin{align}
	w & =
	\begin{bmatrix}
		1 & 1 & 1 \newline
		1 & 1 & 1
	\end{bmatrix}
	\rightarrow
	w_1=
	\begin{bmatrix}
		1 \newline 1
	\end{bmatrix}
	\quad\text{and}\quad
	w_2=
	\begin{bmatrix}
		1 & 1 & 1
	\end{bmatrix}
\end{align}
$$
The original kernel can be reconstructed from the constituent kernels with the matrix equation below.

$$w=w_1w_2^T=w_1\star w_2$$

## Highpass Filters

<span style = "color:lightblue">Highpass filters</span> create sharpening in an image, where intensity transitions and details are highlighted. This filter **allows high frequencies and restricts low frequencies.** 

A highpass filter is achieved using <span style = "color:lightblue">differentiation</span>.

### First Derivative

A first-derivative filter can be used for edge enhancement.

### Second Derivative

The <span style = "color:lightblue">Laplacian operator</span> is the simplest second-order isotropic derivative operator.

$$\nabla^2f=\frac{\partial^2f}{\partial x^2}+\frac{\partial^2f}{\partial y^2}$$

Some Laplacian kernels are shown below.


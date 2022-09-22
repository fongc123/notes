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

![[image-processing-1d-padding.png|250]]

In a two-dimensional signal, an image with size $(M,N)$ would create a **full correlation result** with size $(M+2a,N+2b)$.

![[image-processing-2d-padding.png|300]]

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
**Separable filter kernels are desired due to their computational advantage.** The ratio between the computational cost of an inseparable and a separable kernel with size $m\times n$ is shown below.

$$\text{computational advantage}=\frac{mn}{m+n}$$

## Lowpass Filters

<span style = "color:lightblue">Lowpass filters</span> can be used for **image smoothing** by reducing irrelevant high-frequency details that are found in noise. The filter **allows low frequencies and restricts high frequencies**, creating a blurred image.

> [!INFO]
> Noise is generally represented by high-frequency fluctuations.

A general equation is shown below, where $w$ represents the kernel and $f$ represents the image.
$$
g(x,y)=\frac{
	\sum_{s=-a}^{a}\sum_{t=-b}^{b}{w(s,t)f(x+s,y+t)}
}
{
	\sum_{s=-a}^{a}\sum_{t=-b}^{b}{w(s,t)}
}
$$

> [!INFO]
> The denominator is the <span style = "color:lightblue">normalization factor</span>. It is needed as the associations between pixels should not be disturbed.

### Box Filter

A <span style = "color:lightblue">box filter</span> accomplishes image smoothing spatial filtering by averaging.

$$R=\frac{1}{9}\sum_{i=1}^{9}{z_i}$$

![[image-processing-box-filter.png|600]]

The complete equation of the box filter is shown below, where pixel values are averaged over a larger region.

$$h[m,n]=\sum_{k,l}{g[k,l]f[m+k,n+l]}$$

### Gaussian Filter

Named after Carl Friedrich Gauss, the kernel values of the <span style = "color:lightblue">Gaussian filter</span> are sampled from the two-dimensional Gaussian function.

$$w(s,t)=\frac{1}{2\pi\sigma^2}\exp\left(-\frac{s^2+t^2}{2\sigma^2}\right)=K\exp\left(-\frac{s^2+t^2}{2\sigma^2}\right)$$

This filter is **separable**, where the weights fall off with distance from the center pixel.

> [!INFO]
> The Gaussian kernel values are theoretically infinite, but they are truncated typically at two to three standard deviations ($\sigma$).

![[image-processing-gaussian-filter.png|700]]

Lowpass filtering can be applied to thresholding for region extraction (e.g., astronomy) or for shading correction.

## Non-linear Spatial Filtering

<span style = "color:lightblue">Non-linear spatial filters</span> typically replace the center pixel value with a value determined by an ordering or ranking alogirthm of the neighborhood. Some examples of ordering filters include **median filter**, **max filter**, and **minimum filter**.

### Medium Filter

In a <span style = "color:lightblue">medium filter</span>, the center pixel value is replaced by the median of the sorted values in the pixel window. Three median filters of varying radii are shown below.

![[image-processing-median-filter.png]]

This filter removes impulse noise, avoids excessive smoothing, and preserves the image edges.

## Highpass Filters

<span style = "color:lightblue">Highpass filters</span> can be used for **image sharpening**, where intensity transitions and fine details are highlighted. The filter **allows high frequencies and restricts low frequencies.**

A highpass filter is achieved using <span style = "color:lightblue">differentiation</span>.

> [!WARNING]
> Differentiation is very sensitive to noise. It is important to blur the image first before performing differentiation.

First derivatives create thick edges, while second derivatives produce better edges.

### Image Gradient

<span style = "color:lightblue">Image gradients</span> can be achieved with the first derivative.

$$M(x,y)=\text{mag}(\nabla f)=\sqrt{g_x^2+g_y^2}\approx|g_x|+|g_y|$$
There are several gradient operators to use, such as the <span style = "color:lightblue">Roberts cross-gradient operator</span> or the <span style = "color:lightblue">Sobel operator</span>.

![[image-processing-roberts-sobel.png]]

A first-derivative filter can be used for edge enhancement, as **only the regions with <u><b>change</b></u> will be reflected in the output**. 

![[image-processing-gradient-ex.png|600]]

### Laplacian Operator

The <span style = "color:lightblue">Laplacian operator</span> is the simplest second-order isotropic derivative operator.

$$
\begin{gather}
	\nabla^2f =\frac{\partial^2f}{\partial x^2}+\frac{\partial^2f}{\partial y^2} \newline
	\frac{\partial^2f}{\partial x^2} = f(x+1,y)+f(x-1,y)-2f(x,y) \newline
	\frac{\partial^2f}{\partial y^2} = f(x,y+1)+f(x,y-1)-2f(x,y)
\end{gather}
$$
![[image-processing-laplacian.png|600]]


### Sharpening Images

Images can be sharpened by **adding edges to the images** to enhance details.

$$\underbracket{g(x,y)}_{\text{sharpened}}=\underbracket{f(x,y)}_{\text{original}}+c\cdot \underbracket{e(x,y)}_{\text{edge map}}$$
The amount of sharpening can be controlled by the sharpening factor $c$. A sharpening of an image of the moon with a Laplacian operator is shown below.

![[image-processing-laplacian-ex.png|600]]

### Unsharp Masking

Images can also be sharpened by adding **an unsharp mask** to the original image. The mask is obtained by **subtracting the blurred image from the original image**.

$$
\begin{gather}
	g_{mask}(x,y)=f(x,y)-\bar{f}(x,y) \newline \newline
	g(x,y) = f(x,y) + kg_{mask}(x,y)
\end{gather}
$$
The value of $k$ determines the contribution of the unsharp mask. For example, highboost filtering is performed when $k > 1$.

![[image-processing-unsharp-mask.png|250]]

An example of unsharp masking with a $31\times 31$ Gaussian filter is shown below, where unsharp masking ($k=1$) and highboost filtering ($k=4.5$) are compared.

![[image-processing-unsharp-mask-ex.png|700]]

> [!WARNING]
> Image sharpening should not be overdone, as the output would contain an unnecessary amount of noise.


# Arithmetic Operations

A review of <span style = "color:lightblue">elementwise</span> and <span style = "color:lightblue">matrix product</span> operations are shown.

$$
\begin{bmatrix}
	a_{11} & a_{12} \newline
	a_{21} & a_{22}
\end{bmatrix}
\odot
\begin{bmatrix}
	b_{11} & b_{12} \newline
	b_{21} & b_{22}
\end{bmatrix}
=
\begin{bmatrix}
	a_{11}b_{11} & a_{12}b_{12} \newline
	a_{21}b_{21} & a_{22}b_{22}
\end{bmatrix}
$$
$$
\begin{bmatrix}
	a_{11} & a_{12} \newline
	a_{21} & a_{22}
\end{bmatrix}
\begin{bmatrix}
	b_{11} & b_{12} \newline
	b_{21} & b_{22}
\end{bmatrix}
=
\begin{bmatrix}
	a_{11}b_{11} + a_{12}b_{21} & a_{11}b_{12} + a_{12}b_{22} \newline
	a_{21}b_{11} + a_{22}b_{21} & a_{21}b_{12} + a_{22}b_{22}
\end{bmatrix}
$$

Elementwise operations perform arithmetic operations on each indvidual element, while matrix product operations follow matrix multiplication rules. Additionally, the condition of a <span style = "color:lightblue">linear operation</span> is shown below.

$$H[af_1(x,y)+bf_2(x,y)]=aH[f_1(x,y)]+bH[f_2(x,y)]$$

If the operator $H$ satisfies the condition, the operator is considered to be linear.

These operations can be applied to images as well.

## Image Addition

<span style = "color:lightblue">Image addition</span> or averaging combines two images together.

$$s(x,y)=f(x,y)+g(x,y)$$

To perform noise reduction, a number of $K$ images can be summed together, where the image's details will be amplified. The noise-free clean image, noise, and noisy image are represented as $f$, $n_i$, and $f_i$ respectively.

$$
\begin{align}
	f_i(x,y) & = f(x,y)+n_i(x,y) \newline
	\bar{f}(x,y)&=\frac{1}{K}\sum_{i=1}^{K}{f_i(x,y)} \newline
	& = f(x,y) + \frac{1}{K}\sum_{i=1}^{K}n_i{x,y}
\end{align}
$$
Here, it is assumed that the additive noise is uncorrelated with zero mean.

$$E\{n(x,y)\}=0$$

This method is especially useful in astronomy as shown below.

![[image-processing-addition.png|600x450]]

## Image Subtraction

<span style = "color:lightblue">Image subtraction</span> can be used to enhance difference for comparison between two images.

$$d(x,y)=f(x,y)-g(x,y)$$

A common application of this method is <span style = "color:lightblue">mask mode radiography</span> as shown below.

![[image-processing-subtraction.png|700]]

## Image Multiplication & Division

<span style = "color:lightblue">Image multiplication & division</span> can be used for shading correction or masking.

$$g(x,y)=f(x,y)h(x,y)$$

Here, the corresponding pixel values for images $f$ and $h$ undergo **elementwise operations**. A masking on a dental X-ray image is shown below, where only the teeth with filings are displayed.

![[image-processing-multiplication.png|650]]
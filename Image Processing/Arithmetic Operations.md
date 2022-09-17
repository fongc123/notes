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

<span style = "color:lightblue">Image addition</span> or averaging combines two images together and can be used for noise reduction.

$$s(x,y)=f(x,y)+g(x,y)$$

$K$ number of images are averaged together to remove noise.

## Image Subtraction

<span style = "color:lightblue">Image subtraction</span> can be used to enhance difference for comparison.


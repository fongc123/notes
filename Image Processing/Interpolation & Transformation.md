# Image Interpolation

<span style = "color:lightblue">Image interpolation</span> is the process of using **known input image pixel values** to estimate new pixel values at unknown locations. Interpolation is commonly used in zooming, shrinking, rotating, and geometrically correcting digital images.

There are several **resampling methods** to perform interpolation.
- <span style = "color:lightblue">nearest neighbor</span>: assign the intensity value of the nearest neighbor to the new location (*easiest*)
- <span style = "color:lightblue">bilinear</span>: calculate the intensity value based on the distance difference of the four surrounding pixels to the new location (*standard*)
- <span style = "color:lightblue">bicubic</span>: considers 16 neighbors and high-order interpolation (*complex*)

![[image-processing-interpolation.png|450]]

> [!INFO]
> The expression for the intensity value of a new location $P$ with bilinear resampling is shown below, where $Q_{11}$, $Q_{12}$, $Q_{21}$, and $Q_{22}$ are the four points surrounding the new location. 
> $$
> \small
> f(x,y)=\frac{y_2-y}{y_2-y_1} \left(\frac{x_2-x}{x_2-x_1}f(Q_{11}) +\frac{x-x_1}{x_2-x_1}f(Q_{21})\right)+\frac{y-y_1}{y_2-y_1}\left(\frac{x_2-2}{x_2-x_1}f(Q_{12}+\frac{x-x_1}{x_2-x_1}f(Q_{22})\right)$$

A comparison between the resampling methods is shown below. The original image was reduced to 72 dpi and zoomed back to its original 930 dpi.

![[image-processing-resampling.png|650]]

# Geometric Transformation

<span style = "color:lightblue">Geometric transformations</span> utilize matrix product operations to modify images. *See [[Arithmetic Operations]].*

## Affine Transformations

<span style = "color:lightblue">Affine transformations</span> preserve lines and parallelism during geometric transformation. They include **scaling**, **translation**, **rotation**, and **shearing** (*non-rigid transformation*).

$$
\begin{bmatrix}
	x' \newline
	y' \newline
	1
\end{bmatrix}
=
\textbf{A}
\begin{bmatrix}
	x \newline
	y \newline
	1 \newline
\end{bmatrix}
=
\begin{bmatrix}
	a_{11} & a_{12} & a_{13} \newline
	a_{21} & a_{22} & a_{23} \newline
	0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
	x \newline
	y \newline
	1
\end{bmatrix}
$$

All affine transformations can be achieved by modifying the $a$ constants in the above matrix equation.

$$
\begin{align}
	\text{identity:} \quad \textbf{A} & =
	\begin{bmatrix}
		1 & 0 & 0 \newline
		0 & 1 & 0 \newline
		0 & 0 & 1
	\end{bmatrix} \newline \newline
	\text{scaling/reflection:} \quad \textbf{A} & =
	\begin{bmatrix}
		c_x & 0 & 0 \newline
		0 & c_y & 0 \newline
		0 & 0 & 1
	\end{bmatrix} \newline \newline
	\text{rotation (about the origin):} \quad \textbf{A} & =
	\begin{bmatrix}
		\cos{\theta} & -\sin{\theta} & 0 \newline
		\sin{\theta} & \cos{\theta} & 0 \newline
		0 & 0 & 1
	\end{bmatrix}
\end{align}
$$
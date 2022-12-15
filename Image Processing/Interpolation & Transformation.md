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
	\end{bmatrix} \quad\text{\small(original)} \newline \newline
	\text{scaling/reflection:} \quad \textbf{A} & =
	\begin{bmatrix}
		c_x & 0 & 0 \newline
		0 & c_y & 0 \newline
		0 & 0 & 1
	\end{bmatrix} \quad\text{\small (by respective factors $c$)} \newline \newline
	\text{rotation (about the origin, z-axis):} \quad \textbf{A} & =
	\begin{bmatrix}
		\cos{\theta} & -\sin{\theta} & 0 \newline
		\sin{\theta} & \cos{\theta} & 0 \newline
		0 & 0 & 1
	\end{bmatrix} \newline \newline
	\text{translation:} \quad \textbf{A} & =
	\begin{bmatrix}
		1 & 0 & t_x \newline
		0 & 1 & t_y \newline
		0 & 0 & 1
	\end{bmatrix} \quad\text{\small(by respective factors $t$)} \newline \newline
	\text{shear (vertical):} \quad \textbf{A} & =
	\begin{bmatrix}
		1 & s_v & 0 \newline
		0 & 1 & 0 \newline
		0 & 0 & 1 \newline
	\end{bmatrix} \quad\text{\small(by factor $s_v$)} \newline \newline
	\text{shear (horizontal):} \quad \textbf{A} & =
	\begin{bmatrix}
		1 & 0 & 0 \newline
		s_h & 1 & 0 \newline
		0 & 0 & 1
	\end{bmatrix} \quad\text{\small(by factor $s_h$)} \newline
\end{align}
$$
In rotation, image interpolation is needed to fill in missing pixel values. Three resampling methods and their effects on a rotated image are shown below.

![[image-processing-resampling-rotation.png|600]]

> [!INFO]
> The transformation matrix for rotation around the x-axis and the y-axis are shown below.
> $$
> \begin{gather}
> R_x=\begin{bmatrix}
> 1 & 0 & 0 \\
> 0 & \cos(\theta) & -\sin(\theta) \\
> 0 & \sin(\theta) & \cos(\theta)
> \end{bmatrix} \\\\
> R_y=\begin{bmatrix}
> \cos(\theta) & 0 & \sin(\theta) \\
> 0 & 1 & 0 \\
> -\sin(\theta) & 0 & \cos(\theta)
> \end{bmatrix}
> \end{gather} 
> $$
> In general, multiple rotation matrices can be multiplied together to perform rotation with respect to <u>any</u> axis.
> $$
> \begin{gather}
> T(\vec{x})=R\vec{x}\quad\text{where}\space R=R_{\theta_x}R_{\theta_y}R_{\theta_z}
> \end{gather}
> $$

For a three-dimensional object, the following general expression that accounts for all transformations is obtained.

$$
T\left(\begin{matrix}x\\y\\z\\1\end{matrix}\right)=\left(\begin{matrix}
a_{11} & a_{12} & a_{13} & a_{14} \\
a_{21} & a_{22} & a_{23} & a_{24} \\
a_{31} & a_{32} & a_{33} & a_{34} \\
0 & 0 & 0 & 1
\end{matrix}\right)\left(\begin{matrix}
x \\ y \\ z \\ 1
\end{matrix}\right)
$$

# Image Registration
<span style = "color:lightblue">Image registration</span> is the process of transforming different sets of data into one coordinate system. It finds the optimal spatial transformation mapping between images.

![[image-processing-image-registration.png|600]]

An **optimal value** of the [[#Objective Functions|objective function]] $F$ and the **optimal transformation** $\hat{T}$ between the <span style = "color:lightblue">reference image</span> and the <span style = "color:lightblue">floating image</span>.

$$
\underbracket{u(\vec{x})}_{\text{reference}}\Leftrightarrow \underbracket{v(T(\vec{x}))}_{\text{floating}}
$$

## Objective Functions
Markers are used as reference points to measure <span style = "color:lightblue">registration errors</span> in the transformation process. <span style = "color:lightblue">External markers</span> are externally attached to the object and appear in the image.

![[image-processing-external-markers.png|600]]

The above images show **fiducial markers** attached to a patient in CT and MR scans. On the other hand, <span style = "color:lightblue">internal markers</span> use surface-based registration to compare between the original and transformed image.

Common objective functions are shown below.

$$
\begin{align}
\text{sum of squared difference:} & \quad SSD=\frac{1}{N}\sum_{\vec{x}\in D}\left[u(\vec{x})-v(T(\vec{x}))\right]^2 \\\\
\text{sum of absolute difference:} & \quad SAD=\frac{1}{N}\sum_{\vec{x}\in D}{|u(\vec{x})-v(T(\vec{x}))|} \\\\
\text{correlation coefficient:} & \quad CC=\dfrac{\sum_{\vec{x}\in D}(u-\bar{u})(v-\bar{v})}{\left[\sum_{\vec{x}\in D}(u-\bar{u})^2(v-\bar{v})^2\right]^\frac{1}{2}} \\\\
\text{mutual information:} & \quad MI(u,v)=h(u) +h(v)-h(u,v) \\\\
& \quad h(x,y)=-\sum_{x\in X}\sum_{y\in Y}p(x,y)\log p(x,y)\small\leftarrow\text{entropy} \\\\
& \quad h(x)=-\sum_{x\in X}p(x)\log p(x)
\end{align}
$$

> [!INFO]
> The **sum of squared difference** is sensitive to voxels that have large intensity differences. The **sum of absolute difference** can reduce the effect of these outliers.

> [!INFO]
> Two images are matched when the **mutual information** is maximized.

[[Regression#Gradient Descent|Gradient descent]] is commonly used to **optimize** the objective function $F$.
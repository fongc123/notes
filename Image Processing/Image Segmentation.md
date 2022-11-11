The goal of <span style = "color:lightblue">image segmentation</span> is to identify groups of pixels that belong together or are similar with each other.

Image segmentation partitions a region $R$ into smaller sub-regions $R_1,R_2,\dots,R_n$ with the following conditions.
1. The union of all sub-regions $R_i$ must equal the original region $R$.
2. All sub-regions $R_i$ are connected sets.
3. Any two sub-regions must not intersect.
4. There is a **logical predicate** $Q$ for any sub-region (i.e., they must be distinguishable).

Generally, there are two methods: <span style = "color:lightblue">discontinuity</span> (*edge-based*) and <span style = "color:lightblue">similarity</span> (*region-based*).

For example, the two images below are segmented by edges (c) and by the standard deviation of intensities in a region (f).

![[image-processing-segmentation.png|600]]

# Detection of Sharp Intensity Changes
The following image characteristics produce sharp local changes.
- <span style = "color:lightblue">edge pixels</span>: abrupt change of intensity
- <span style = "color:lightblue">edges</span>: set of connected **edge pixels**
- <span style = "color:lightblue">lines</span>: an edge segment where both sides of the line segment have significantly different intensities
- <span style = "color:lightblue">point</span>: foreground pixel (*brighter*) <u>surrounded</u> by background pixels (*darker*)

Detection normally involves smoothing and [[#Thresholding|thresholding]] as well.

## Derivatives
To obtain a **finite difference** between pixels, the <span style = "color:lightblue">Taylor series estimation of a derivative</span> is used. The <span style = "color:lightblue">forward difference</span> considers the next and current pixels, while the <span style = "color:lightblue">backward difference</span> considers the previous and current pixels. Generally, however, <span style = "color:lightblue">central differences</span>, which consider the next and previous pixels, are used.

| **Derivative** | $f(x+2)$ | $f(x+1)$ | $f(x)$ | $f(x-1)$ | $f(x-2)$ |
|:--------------:|:--------:|:--------:|:------:|:--------:|:--------:|
|    $2f'(x)$    |    -     |    1     |   0    |    -1     |    -     |
|    $f''(x)$    |    -     |    1     |   -2   |    1     |    -     |
|   $2f'''(x)$   |    1     |    -2    |   0    |    2     |    -1    |
|   $f''''(x)$   |    1     |    -4    |   6    |    -4    |    1     |

> [!INFO]
> For example, the first difference at point $x$ is as follows.
> $$f'(x)=\dfrac{f(x+1) - f(x-1)}{2}$$
> For multivariable functions, the derivative is applied to each variable individually.

**First-order** and **second-order** derivatives are commonly used.
- First-order derivatives produce thicker edges.
- Second-order derivatives respond to fine details (e.g., thin lines, points, noise).
- Second-order derivatives produce a **double-edge response** (i.e., positive $\rightarrow$ negative).
- The **sign** of second-order derivatives can be used to determine the direction of the transition (e.g., light $\rightarrow$ dark).

As shown in [[Spatial Filtering#High-pass Filters|high-pass filtering]], convolution with a differentiation kernel (e.g., [[Spatial Filtering#Laplacian Operator|Laplacian filter]]) can be used to detect sharp intensity changes, such as isolated points or lines.

## Line Detection with Direction
Specific <span style = "color:lightblue">line detection kernels</span> can be used to detect lines in certain directions.

![[image-processing-line-detection-dir.png|600]]

The preferred direction is weighted with a larger coefficient (e.g., $2$).

## Edge Detection
As the [[Spatial Filtering#High-pass Filters|second-order derivative is highly sensitive to noise]], it is important to perform noise reduction before <span style = "color:lightblue">edge detection</span>.

$$
\begin{align}
\text{gradient:}&\quad\nabla f(x,y) =
\begin{bmatrix}
g_x(x,y) \\
g_y(x,y)
\end{bmatrix}
= \begin{bmatrix}
\dfrac{\partial f(x,y)}{\partial x} \\
\dfrac{\partial f(x,y)}{\partial y}
\end{bmatrix} \\\\
\text{magnitude:} & \quad M(x,y)=||\nabla f(x,y)||=\sqrt{g^2_x(x,y)+g_y^2(x,y)} \\\\
\text{direction:} & \quad \alpha(x,y)=\tan^{-1}\left[\dfrac{g_y(x,y)}{g_x(x,y)}\right]
\end{align}
$$

![[image-processing-edge-detection.png|600]]

The direction of the edge is orthogonal to the direction of the gradient vector (i.e., edge normal).

The expression for a **one-dimensional** kernel for implementing the **forward difference** is shown below.

$$
\begin{gather}
g_x(x,y)=\dfrac{\partial f(x,y)}{\partial x} = f(x+1,y)-f(x,y) \\\\
g_y(x,y)=\dfrac{\partial f(x,y)}{\partial y} = f(x,y+1)-f(x,y)
\end{gather}
$$

Other operators are listed below.
- <span style = "color:lightblue">Roberts cross operator</span>: $2\times2$ kernel for <u>diagonal</u> edge detection
- <span style = "color:lightblue">Prewitt operator</span>: $3\times3$ kernel for directional edge detection
- <span style = "color:lightblue">Sobel operator</span>: $3\times3$ kernel for edge detection

## Canny Edge Detector
The <span style = "color:lightblue">Canny edge detector</span> is an advanced edge detection algorithm.
1. **Low error rate**: all edges are found with no false edges
2. **Well-localized edge points**: 

# Thresholding

d
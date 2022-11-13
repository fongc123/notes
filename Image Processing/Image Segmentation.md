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
The <span style = "color:lightblue">Canny edge detector</span> is an advanced edge detection algorithm that creates thin edges.
1. **Low error rate**: all edges are found with no false edges
2. **Well-localized edge points**: the edges located must be close to the true edges
3. **Single edge point response**: only one point is returned for each true edge point

The algorithm consists of the following steps.
1. Smooth the image with a [[Spatial Filtering#Gaussian Filter|Gaussian filter]].
2. Compute the gradient magnitude and angle images (*see [[#Edge Detection|edge detection]]*).
3. Apply [[#Non-maxima Suppression|non-maximum suppression]] to the gradient magnitude image.
4. Apply [[#Hysteresis Thresholding|double thresholding]] and connectivity analysis to detect *and* link edges.

The example below shows a head CT image (a), the thresholded gradient of the smoothed image (b), and the image obtained using the **Canny edge detector** algorithm.

![[image-processing-canny-edge.png|600]]

All edges are thin and visible. Additionally, edges belonging to the spine are also highlighted.

### Non-maximum Suppression
<span style = "color:lightblue">Non-maximum suppression</span> removes unwanted pixels which may not constitute an edge. Each pixel is set to $0$ (i.e., suppressed) if it is <u>not</u> a local maximum in its neighborhood in the **direction** of the gradient.

For a $3\times3$ region, there are four basic edge directions: horizontal, $-45\degree$, vertical, and $+45\degree$.

![[image-processing-nonmax-supp-1.png|600]]

The basic direction $d_k$ that is closest to the actual gradient angle $\alpha$ is selected. For pixels that have a magnitude that is less than one or both of its neighbors (i.e., before and after in the direction), their magnitudes are set to $0$. This results in a binary image with thin edges.

> [!INFO]
> Non-maxima suppression is also used in **identifying the most optimal bounding box** in [[ML Basics|machine learning]] applications.

### Hysteresis Thresholding
With two thresholds (a low threshold $T_L$ or `minVal` and a high threshold $T_H$ or `maxVal`), <span style = "color:lightblue">hysteresis thresholding</span> or <span style = "color:lightblue">double thresholding</span> reduces false edge points. In addition to gradient thresholding, it performs connectivity analysis (e.g., 4-connectivity or 8-connectivity) to discern whether edges with weak gradients are true edges.

1. Edges with intensity gradient greater than $T_H$ are **sure-edges**, while those with intensity gradient less than $T_L$ are not edges and are **discarded**.
2. Edges that are greater than $T_L$ but less than $T_H$ are **weak edges**.
3. All **weak edges** that are connected to at least one **sure-edge** are marked as valid edges and are kept.
4. All **weak edges** that do not connect with at least one **sure-edge** are discarded.

![[image-processing-hysteresis-thresholding.png|600]]

In the above image, even though edge $C$ is a weak edge, it is considered a valid edge as it is connected to edge $A$, which is a sure-edge. On the other hand, edge $B$ is not connected to any sure-edges and, thus, is discarded.

# Thresholding
From a [[Intensity Transformations#Histogram Processing|histogram]], an image can be separated into multiple intensity groups. Thus, the success of <span style = "color:lightblue">intensity thresholding</span> is related directly to the width and depth of the valleys separating the histogram modes.

Several factors in properties of histogram valleys are listed below.
- **Separation between peaks:** the amount of overlap between peaks
- **Noise content**: the noise of intensity levels in the image (*affects separability as well*)
- **Sizes of object and background**: small objects are not apparent in the histogram
- **Uniformity of illumination**: uneven or shifted peaks
- **Uniformity of reflectance properties**

## Global
<span style = "color:lightblue">Basic global thresholding</span> segments the image with a threshold $T$ such that the threshold is the midpoint between the means of the two groups of pixels ($m_1$ and $m_2$).

$$T=\dfrac{m_1+m_2}{2}$$

The steps for this algorithm are listed below.
1. Randomly select an initial estimate for the global threshold $T$ <u>within the intensity range</u>.
2. Segment the image to produce two groups of pixels.
3. Compute the means of the groups.
4. Update the threshold with the above equation for $T$.
5. Repeat steps 2 to 4 until convergence.

An example is shown below, where the threshold converged at $T=125$.

![[image-processing-global-thresholding.png|600]]

## Otsu's Method

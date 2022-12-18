The goal of <span style = "color:lightblue">image segmentation</span> is to identify groups of pixels that belong together or are similar with each other.

Image segmentation partitions a region $R$ into smaller sub-regions $R_1,R_2,\dots,R_n$ with the following conditions.
1. The union of all sub-regions $R_i$ must equal the original region $R$.
2. All sub-regions $R_i$ are connected sets.
3. Any two sub-regions must not intersect.
4. There is a **logical predicate** $Q$ for any sub-region (i.e., they must be distinguishable).

Generally, there are two methods: <span style = "color:lightblue">discontinuity</span> (*edge-based*) and <span style = "color:lightblue">similarity</span> (*region-based*).

For example, the two images below are segmented by edges (c) and by the standard deviation of intensities in a region (f).

![[image-processing-segmentation.png|600]]

<span style = "color:lightblue">Semantic segmentation</span> classifies pixels under one label, while <span style = "color:lightblue">instance segmentation</span> partitions individual object instances.

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
3. Apply [[#Non-maximum Suppression|non-maximum suppression]] to the gradient magnitude image.
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
<span style = "color:lightblue">Otsu's thresholding method</span> finds the optimal thresholding value to separate classes by maximizing the <span style = "color:lightblue">between-class variance</span> or minimizing the <span style = "color:lightblue">weighted within-class variance</span>.

The steps for Otsu's algorithm are listed below.
1. Compute the [[Intensity Transformations#Histogram Processing|normalized histogram]] of the input image.
2. Compute the **cumulative sums** $p_1(k)$, the **cumulative means** $m(k)$, and the **global mean** $m_G$.
3. Calculate the **between-class variance** $\sigma_B^2(k)$.
4. Obtain the threshold $k^*$ which is the value of $k$ that maximizes $\sigma^2_B(k)$.
5. Compute the **global variance** $\sigma_G^2$ and the **separability measure** $\eta^*$.

$$g(x,y)=\begin{dcases}
1 & \text{if}\space f(x,y)>k^* \\
0 & \text{if}\space f(x,y)\leq k^*
\end{dcases}
$$

> [!INFO]
> If there are multiple values of $k$ that create the greatest between-class variance, all $k$ values are averaged.

> [!WARNING]
> Otsu's thresholding algorithm will fail when the foreground object is small compared to the background, as the intensity values will be dominated by the background pixels.

### Derivation
An image segmented is segmented into two classes$\textemdash$$c_1$ and $c_2$$\textemdash$with a threshold $k$, where pixels belonging to $c_1$ and $c_2$ will have intensity values ranging from $[0, k]$ and $[k+1,L-1]$ respectively. The expressions for the probability of a pixel assigned to $c_1$ or $c_2$ are shown below.

$$
\begin{gather}
p_i=\frac{n_i}{MN} \\
P_1(k)=\sum_{i=0}^{k}{p_i} \\
P_2(k)=\sum_{i=k+1}^{L-1}{p_i} =1-P_1(k)
\end{gather}
$$

With the [[Classification#Bayes Rule|Bayes' rule]], the means of the intensity values of pixels in both classes can be calculated.

$$
\begin{align}
m_1(k)&=\sum_{i=0}^{k}iP(i|c_1) \\
&=\sum_{i=0}^{k}i\dfrac{P(c_1|i)P(i)}{P(c_1)}\leftarrow\text{Bayes' rule} \\
&=\dfrac{1}{P_1(k)}\sum_{i=0}^{k}ip_i\\
m_2(k)&=\sum_{i=k+1}^{L-1}iP(i|c_2) \\
&=\dfrac{1}{P_2(k)}\sum_{i=k+1}^{L-1}ip_i
\end{align}
$$

> [!WARNING]
> $$P(i|c_1)\neq P(i)\neq P(c_1|i)$$
> - $P(i|c_1)$ is the probability of the intensity level $i$ <u>in the scope</u> of the class $c_1$
> - $P(i)$ is the probability of the intensity level $i$ out of <u>all</u> intensity levels
> - $P(c_1|i)$ is the probability of the class $c_1$ given an intensity level
> 
> In the case of the class $c_1$, since $i$ is restricted within the range of $[0,k]$, $P(c_1|i)$ will always evaluate to $1$.

Additionally, the cumulative mean $m(k)$ and the global mean $m_G$ are calculated.

$$
\begin{gather}
m(k)=\sum_{i=0}^{k}{ip_i} \\
m_G=\sum_{i=0}^{L-1}ip_i
\end{gather}
$$

Thus, we obtain the following.

$$P_1m_1+P_2m_2=m_G\quad\text{where}\space P_1+P_2=1$$

The global variance $\sigma_G^2$ can be calculated.

$$\sigma_G^2=\sum_{i=0}^{L-1}(i-m_G)^2p_i$$

Thus, the between-class variance can be calculated.

$$
\begin{align}
\sigma_B^2 &= P_1(m_1-m_G)^2+P_2(m_2-m_G)^2 \\
&=P_1P_2(m_1-m_2)^2 \\
&=\dfrac{(m_GP_1-m)^2}{P_1(1-P_1)}
\end{align}
$$

All integer values of $k$ are evaluated such that the maximum value of $\sigma_B^2$ is obtained.

$$k^*=\arg\max_{k}\sigma_B^2(k)\quad\text{for}\space 0\leq k\leq L-1$$

### Multiple Classes
Otsu's method can be extended to threshold the image into multiple classes.

$$
\begin{gather}
\sigma_B^2=\sum_{k=1}^{K}P_k(m_k-m_G)^2\\\text{where}\space P_k=\sum_{i\in c_k}{p_i}\space\text{and}\space m_k=\frac{1}{P_k}\sum_{i\in c_k}ip_i
\end{gather}
$$

Here, $K-1$ thresholds will threshold the image into $K$ classes.

$$k^*_1,k^*_2,\ldots,k^*_{K-1}=\arg\max_k\sigma_B^2(k_1,k_2,\ldots,k_{K-1})\quad\text{for}\space 0<k_1<\ldots<k_{K-1}<L-1$$

## Variable Thresholding
In <span style = "color:lightblue">variable thresholding</span>, the threshold value at each pixel changes based on specified properties in the pixel's local neighborhood.

### Local Image Properties
The output of a thresholding function based on <span style = "color:lightblue">local image properties</span> is dependent on a logical predicate $Q$ of the pixels in the region of a neighborhood $S_{xy}$.

$$
g(x,y)=\begin{dcases}
1 & \text{if}\space Q(\text{local parameters})\space\text{is True} \\
0 & \text{if}\space Q(\text{local parameters})\space\text{is False}
\end{dcases}
$$

An example is shown below, where the predicate is based on the local mean and standard deviation.

$$
Q(\sigma_{xy},m_{xy})=\begin{dcases}
\text{True} & \text{if}\space f(x,y)>a\sigma_{xy}\space\text{and}\space f(x,y)>bm_{xy}\\
\text{False} & \text{otherwise}
\end{dcases}
$$

The example below shows an image of yeast cells (a), the result after dual thresholding (i.e., two thresholds to create three classes) (b), the local standard deviations in a $3\times3$ neighborhood (c), and the result after local thresholding (d).

![[image-processing-local-variable-thresholding.png|600]]

As shown in (b), other thresholding methods improperly group nearby cells together, while local thresholding is successful in separating objects.

### Moving Averages
The output of a thresholding function based on <span style = "color:lightblue">moving averages</span> is dependent on the average of the pixel intensities of past pixels.

$$
\begin{gather}
g(x,y)=\begin{dcases}
1 & \text{if}\space f(x,y)>T_{xy} \\
0 & \text{if}\space f(x,y)\leq T_{xy}
\end{dcases} \\\\
\text{where}\space T_{xy}=cm_{xy}
\end{gather}
$$

The moving average $m_{xy}$ can be calculated with the following expression, where $n$ is the number of points used in computing the average.

$$
m(k+1)=\dfrac{1}{n}\sum_{i=k+2-n}^{k+1}{z_i}\quad\text{for}\space k\geq n-1
$$

The example below shows a text image corrupted by spot shading (left), the resultant image after [[#Otsu's Method|Otsu's thresholding]] (middle), and the resultant image after thresholding with moving averages (right).

![[image-processing-moving-averages.png|600]]

# Region Segmentation
In <span style = "color:lightblue">region segmentation</span>, the image is segmented into sub-regions with various methods.

[[Clustering#$k$-Means|K-means clustering]] can also be used as a segmentation technique, where the similarities between pixels are assessed.

## Region Growing
Segmentation by <span style = "color:lightblue">region growing</span> forms larger regions from pixels or sub-regions based on a pre-defined criterion for growth.

An example is shown below, where:
- `a`: X-ray image of weld
- `b`: histogram of `a`
- `c`: initial seed image
- `d`: final seed image
- `e`: absolute value difference between seed value ($255$) and `a`
- `f`: histogram of `e`
- `g`: image of `e` thresholded using dual thresholds
- `h`: image of `e` thresholded with the smallest dual thresholds
- `i`: segmentation result of region growing

![[image-processing-region-growing.png|600]]

## Region Splitting & Merging
Segmentation by <span style = "color:lightblue">region splitting and merging</span> splits and merges an image into quadrants based on a predicate $Q$.

![[image-processing-region-split-merge.png|600]]

1. Split any region $R_i$ for which $Q(R_i)$ is **false** into four disjoint quadrants.
2. When no further splitting is possible, merge any adjacent regions $R_j$ and $R_k$ for which $Q(R_j\cup R_k)$ is **true**.
3. Stop when no further merging is possible.

For example, an image of the Cygnus Loop supernova is segmented with this method, where the expression for the predicate is shown below.

$$Q(R)=\begin{dcases}
\text{True} & \text{if}\space \sigma_R>a\space\text{and}\space 0<m_R<b \\
\text{False} & \text{otherwise}
\end{dcases}
$$

![[image-processing-region-split-merge-ex.png|600]]

Here, the smallest sub-region is limited to $32\times32$ pixels (b), $16\times16$ pixels (c), and $8\times8$ pixels (d).

## Graph Cuts
Segmentation by <span style = "color:lightblue">graph cuts</span> views pixels as nodes of a graph and finds an **optimal partition** (i.e., cut) of the graph, where members within a group have high similarities and members across groups have low similarities.

$$G=(V,E)$$

Here, $G$ represents the graph, $V$ represents a set of nodes, $E\subseteq V\times V$ represents a set of undirected edges, and $\textbf{W}$ represents the similarity measure to characterize the edges. The similarity between nodes $i$ and $j$ can be represented as $w(i,j)$.

For example, the $3\times3$ image below shows the segmentation of an image using graph cuts with a similarity expression based <u>only</u> on intensity.

$$w(i,j)=\frac{1}{|I(n_i)+I(n_j)|+c}$$

![[image-processing-graph-cuts-ex.png|600]]

A more practical similarity equation uses <u>both</u> intensity and spatial distances, where $n_i$ and $n_j$ are two adjacent nodes, $\sigma_I^2$ and $\sigma_d^2$ represent the spread of the intensity and distance, and $r$ is a radial constant.

$$
w(i,j)=\begin{dcases}
\exp\left(-\dfrac{\left[I(n_i)-I(n_j)\right]^2}{\sigma_I^2}\right)\exp\left(-\dfrac{dist(n_i,n_j)}{\sigma_d^2}\right) & \text{if}\space dist(n_i,n_j)<r \\
0 & \text{otherwise}
\end{dcases}
$$

The <span style = "color:lightblue">minimum cut</span> is the optimum partition of a graph that minimizes the cut value.

$$cut(A,B)=\sum_{u\in A,v\in B}w(u,v)$$

Considering the edge weights (i.e., the cost), it is the **shortest path** (*see Dijkstra's algorithm*) between start and end **seed nodes**.

> [!INFO]
> Seed nodes are randomly selected start and end points to segment the graph.

However, the minimum cut favors small, meaningless sets of isolated nodes. A <span style = "color:lightblue">normalized cut</span> accounts for the **total edge connections** to all nodes in the graph as well.

$$
\begin{gather}
Ncut(A,B)=\frac{cut(A,B)}{assoc(A,V)}+\frac{cut(A,B)}{assoc(B,V)} \\\\
assoc(A,V)=\sum_{u\in A,z\in V}{w(u,z)} \\\\
assoc(B,V)=\sum_{v\in B,z\in V}{w(v,z)}
\end{gather}
$$

The $assoc$ terms are the sum of the weights of all edges from the nodes in sub-graph $A$ or $B$ to the nodes of the entire graph.
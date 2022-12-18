A <span style = "color:lightblue">feature</span> is a distinctive attribute or description of an object that can be **labeled** or **differentiated**. <span style = "color:lightblue">Feature detection</span> aims to find features in an image, while <span style = "color:lightblue">feature description</span> assigns quantitative attributes to the features.
- <span style = "color:lightblue">Boundary-based features</span>: pertaining to the outlining border
- <span style = "color:lightblue">Region-based features</span>: pertaining to the properties within a region

> [!INFO]
> A good feature descriptor should be invariant to scale, transition, rotation, illumination, viewpoint, etc. (*see [[Interpolation & Transformation|affine]] and [[Intensity Transformations|intensity]] transformations*).


# Boundary Features
There are several <u>basic</u> measures to describe the boundary of a feature.
- <span style = "color:lightblue">length</span>: the number of pixels along a boundary (i.e., perimeter)
- <span style = "color:lightblue">diameter</span>: the maximum distance between any two points on a boundary
- <span style = "color:lightblue">major axis</span>: the magnitude and the orientation (i.e., slope) of the diameter
	- **Points:** $(x_1,y_1)$ and $(x_2,y_2)$ (*extreme points*)
	- **Magnitude:** [[Clustering#Similarity|Euclidean distance]]
	- **Orientation:** $\theta=tan^{-1}\left[\frac{y_2-y_1}{x_2-x_1}\right]$
- <span style = "color:lightblue">minor axis</span>: the line **perpendicular** to the major axis with a **certain length** such that a box (i.e., a <span style = "color:lightblue">bounding box</span>) passing through all four points of the major and minor axes completely encloses the boundary
- <span style = "color:lightblue">curvature</span>: the overall rate of change of the slope
- <span style = "color:lightblue">tortuosity</span>: a measure of the twists and turns of a curve
	- $\tau=\sum_{i=1}^{n}|a_i|$
		- $n$: the number of elements
		- $a_i$: the values (i.e., slope changes) of the elements

The example below uses tortuosity to describe blood vessel morphology.

![[image-processing-tortuosity.png|600]]

A larger tortuosity ($\tau$) corresponds to a more crooked object.

## Statistical Moments

The <span style = "color:lightblue">statistical moment</span> is a descriptor applicable to one-dimensional renderings of two-dimensional boundaries. For example, the **distances** from the boundary center to the boundary edge can be compared with the **angle** (i.e., <span style = "color:lightblue">distance-versus-angle signatures</span>).

![[image-processing-statistical-moment.png|600]]

The expression for the $n$th moment of $z$ (i.e., the **discrete random variable** of the amplitude of $g$) about its mean is shown below. In the diagram above, $z$ would represent the distance.

$$
\begin{gather}
\mu_n(z)=\sum_{i=0}^{A-1}(z_i-m)^np(z_i) \\\\
m=\sum_{i=0}^{A-1}z_ip(z_i)
\end{gather}
$$

Generally, only the first few moments ($n\in[0,3]$) are required to differentiate between signatures of clearly distinct shapes.

# Region Features
Similarly, there are several <u>basic</u> features to describe the region of a feature. Here, $\rho$ represents the perimeter (i.e., the length of the boundary), while $A$ represents the area (i.e., the number of pixels in the region).
- <span style = "color:lightblue">compactness</span>: the size of the region
$$\text{compactness}=\frac{\rho^2}{A}$$
- <span style = "color:lightblue">circularity</span>: the roundness of the region
$$\text{circularity}=\frac{4\pi A}{\rho^2}$$
- <span style = "color:lightblue">eccentricity</span>: the ratio of the distance between the foci and the length of the major axis

$$\text{eccentricity}=\frac{c}{a}=\frac{\sqrt{a^2-b^2}}{a}=\sqrt{1-\left(\frac{b}{a}\right)^2}\quad\text{where}\space a\geq b$$

An example of eccentricity is shown below.

![[image-processing-eccentricity.png|600]]

Instead of a bounding box, an ellipse is used to approximate the region to calculate eccentricity. A comparison between the three feature descriptors is shown below.

![[image-processing-region-feat-comparisons.png|600]]

Eccentricity describes the **centrality** of an object. Due to [[Acquisition & Representation#Digitization|digitization]], the eccentricity values for the circle and the star are non-zero.

> [!INFO]
> Objects can be mapped onto an $n$-dimensional space, where $n$ is the number of features, to compare the similarity between objects based on selected features.

<span style = "color:lightblue">Topological features</span> study the properties of an object that are unaffected by deformation given that there is no tearing or joining of the object (i.e., <span style = "color:lightblue">rubber-sheet distortions</span>).

$$\text{Euler number }(E)=\text{no. of connected components }(C)-\text{no. of holes }(H)$$

![[image-processing-topological-features.png|600]]

## Texture
<span style = "color:lightblue">Texture-based features</span> measure the variations between pixels in a region, such as smoothness, coarseness, and regularity.

![[image-processing-texture-example.png|600]]

### Statistical
[[#Statistical Moments|Statistical moments]] can be used to measure the variability in the region. The expression for the <span style = "color:lightblue">relative intensity smoothness</span> $\color{lightblue}R$ is shown below.

$$
\begin{gather}
R(z)=1-\frac{1}{1+\sigma^2(z)} \\\\
\sigma^2(z)=\mu_2(z)
\end{gather}
$$

It approaches $0$ for areas with constant intensity and $1$ for large **variance** values.

> [!INFO]
> The variance $\sigma^2$ is the second statistical moment ($n=2$). The third moment ($n=3$) represents skewedness.

Additionally, the expressions for the <span style = "color:lightblue">uniformity</span> $\color{lightblue}U$ (i.e., the sum of squared probabilities) and the <span style = "color:lightblue">entropy</span> $\color{lightblue}e$ are shown below.

$$
\begin{gather}
U(z)=\sum_{i=0}^{L-1}p(z_i)^2 \\\\
e(z)=-\sum_{i=0}^{L-1}p(z_i)\log_2p(z_i)
\end{gather}
$$

> [!INFO]
> The maximum value of uniformity (i.e., $1$) is obtained when <u>all</u> pixels have the same intensity. Uniformity values close to $1$ are obtained when <u>most</u> pixels have the same intensity.

The three statistical measures of the sub-images above are shown below.

![[image-processing-texture-example-stats.png|600]]

### Co-occurrence Matrix
In a <span style = "color:lightblue">co-occurrence matrix</span> $\color{lightblue}\textbf{G}$, the element $g_{ij}$ is the number of times that pixel pairs with intensities $z_i$ and $z_j$ occur in an image in a position specified by a position operator $Q$, where $i$ and $j$ range from $0$ to the maximum intensity level $L-1$.

![[image-processing-cooccurrence-matrix-example.png|600]]

In the co-occurrence matrix above, the position operator $Q$ is defined as "one pixel immediately to the right." Since there is only **one** occasion where the pixel to the right of a pixel with an intensity value of $1$ also has an intensity value of $1$, the value $g_{11}$ is equal to $1$.

To **characterize** a co-occurrence matrix of size $K\times K$, the following descriptors can be used, where $p_{ij}$ is the normalized term of $g_{ij}$.
- <span style = "color:lightblue">maximum probability</span>: the strongest response in $\textbf{G}$ (i.e., maximum value)
- <span style = "color:lightblue">correlation</span>: how correlated a pixel is to its neighbor, where $m_r$ is the mean of row $i$ and $m_c$ is the mean of column $j$
$$\sum_{i=1}^K\sum_{j=1}^K\frac{(i-m_r)(j-m_c)p_{ij}}{\sigma_r\sigma_c}$$
- <span style = "color:lightblue">contrast</span>: the intensity contrast between a pixel and its neighbor
$$\sum_{i=1}^K\sum_{j=1}^K(i-j)^2p_{ij}$$
- <span style = "color:lightblue">uniformity</span>: the uniformity of the pixels (*similar to [[#Statistical|statistical methods]]*)
$$\sum_{i=1}^K\sum_{j=1}^Kp^2_{ij}$$
- <span style = "color:lightblue">homogeneity</span>: the spatial closeness to the diagonal of the distribution of elements in $\textbf{G}$
$$\sum_{i=1}^K\sum_{j=1}^K\frac{p_{ij}}{1+|i-j|}$$
- <span style = "color:lightblue">entropy</span>: the randomness of the elements in $\textbf{G}$
$$-\sum_{i=1}^K\sum_{j=1}^Kp_{ij}\log_2p_{ij}$$

A constant image would have a contrast of $0$ and a uniformity of $1$. A maximum homogeneity value is obtained when $\textbf{G}$ is a diagonal matrix (i.e., all zeros except along the diagonal).

#### Example
Three sample images are shown below.

![[image-processing-cooccurrence-matrix-example-images.png|600]]

The corresponding co-occurrence matrices of size $256\times256$ and their descriptor values are shown below.

![[image-processing-cooccurrence-matrix-example-matrices.png|600]]

# Hotelling Transform
The <span style = "color:lightblue">Hotelling transform</span> or the <span style = "color:lightblue">principal components transform</span> uses [[Data Preprocessing#Principal Component Analysis|principal components]] as feature descriptors.

Given a set of images (e.g., a set of six images), reconstructed images are obtained by using only a selected number of principal components.

![[image-processing-hotelling-1.png|600]]

Pixels in the same spatial location are arranged into an $n$-dimensional vector.

$$x=\begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{bmatrix}$$

![[image-processing-hotelling-2.png|600]]

A transformation matrix $A$, which represents the eigenvectors of the covariance matrix $C_x$ arranged in descending value of their eigenvalues, maps the vector $x$ to $y$, where $m_x$ represents the mean of $x$.

$$y=A(x-m_x)$$

![[image-processing-hotelling-3.png|600]]

Instead of using the original matrix $A$, the reconstruction of $x$ uses a new matrix $A_k$ that is constructed from the $k$ eigenvectors that correspond to the $k$ largest eigenvalues.

$$x=A^Ty+m_x\rightarrow\hat{x}=A_k^Ty+m_x$$

The difference between the original and reconstructed images can improve contrast.

# Scale-Invariant Feature Transform (SIFT)
The <span style = "color:lightblue">scale-invariant feature transform (SIFT)</span> is an algorithm for extracting invariant features (i.e., <span style = "color:lightblue">key points</span>) from an image. The features are predominantly invariant to **scale** and **rotation** and are robust to **affine distortions**, **changes in viewpoints**, **noise**, and **illumination**.

The algorithm consists of the following steps.
1. Detect [[#Local Extrema|local extrema]].
	1. Construct the [[#Scale Space|scale space]] with multiple Gaussian-filtered images.
	2. Obtain the initial key points by finding pixels with matching criteria in difference images.
2. [[#Key Point Localization|Localize key points]].
	1. Improve the accuracy of the location of the key points.
	2. Delete unsuitable keypoints (i.e., edges and low-contrast points).
3. Compute key point orientations.
	1. Calculate the **magnitude** and **angle** with the first-order x- and y-derivatives of the Gaussian-filtered image $L$.
4. Compute [[#Key Point Descriptor|key point descriptors]].
	1. Calculate orientation gradients in $4\times4$ sub-regions in a $16\times16$ neighborhood.
	2. Obtain an 8-directional orientation histogram for each sub-region and combine into a descriptor.
	3. The gradient magnitudes are weighted with a Gaussian weighting function with standard deviation equal to the half size of the region.
	4. The feature vectors are normalized to unit length.

> [!INFO]
> Instead of calculating the magnitude and angle at the location of the key point, the dominant orientation in a neighborhood around the key point may be assigned.

An example of the output feature descriptors is shown below.

![[image-processing-sift-feature-descriptors.png|600]]

For each key point, a $128$-dimensional vector is outputted ($4\space\text{rows}\times4\space\text{columns}\times8\space\text{orientations}$). With this, objects can be distinguished and matched.

## Local Extrema
The initial detection of local extrema searches across all possible **scales** of **Gaussian-filtered** images $L$ (*see [[#Scale Space|scale spaces]]*). Potential candidates are found in the **difference between scale spaces** (i.e., <span style = "color:lightblue">difference of Gaussian</span>).

$$D(x,y,\sigma)=L(x,y,k\sigma)-L(x,y,\sigma)$$

> [!INFO]
> The above expression is equivalent to the following.
> $$
> \begin{align}
> D(x,y,\sigma)&=\left[G(x,y,k\sigma)-G(x,y,\sigma)\right]\star f(x,y) \\
> &\approx\left[(k-1)\sigma^2\nabla^2G\right]\star f(x,y) \\
> &=\left[\sigma^2(k-1)\left(\frac{x^2+y^2-2\sigma^2}{\sigma^4}\exp\left[-\frac{x^2+y^2}{2\sigma^2}\right]\right)\right]\star f(x,y)
> \end{align}
> $$

![[image-processing-sift-local-extrema.png|600]]

> [!INFO]
> There will always be $n-1$ difference images $D$ generated from $n$ Gaussian-filtered images $L$.

The pixel of an extrema candidate is selected as an initial key point if its value is **smaller or larger than all of its 26 neighbors**, which originate from the current and adjacent difference images. 

![[image-processing-sift-local-extrema-neighbors.png|600]]

$9$ neighbors belong to the top image, $8$ neighbors belong to the current image, and $9$ neighbors belong to the bottom image.

### Scale Space
A scale space of a grayscale image $f$ is produced by the convolution of the image $f$ with a variable-scale Gaussian kernel $G$.

$$L(x,y,\sigma)=G(x,y,\sigma)\star f(x,y)$$

![[image-processing-sift-scale-space.png|600]]

Each consecutive octave **decreases the image size**. In each octave, images are generated with varying Gaussian standard deviations based on the power of $k$. In the above example, there are five images in each octave, as $s=2$.

![[image-processing-sift-scale-space-2.png|600]]

## Key Point Localization
A Taylor series expansion of the scale space is used to improve the accuracy of the key point locations.

$$
\begin{align}
\textbf{x}&=(x,y,\sigma) \\
D(x)&=D+\left(\frac{\partial D}{\partial\textbf{x}}\right)^T\textbf{x}+\frac{1}{2}\textbf{x}^T\frac{\partial}{\partial\textbf{x}}\left(\frac{\partial D}{\partial\textbf{x}}\right)\textbf{x} \\
&=D+(\nabla D)^T\textbf{x}+\frac{1}{2}\textbf{x}^T\textbf{H}\textbf{x} \\\\
\text{where}&\space\nabla D=\frac{\partial D}{\partial\textbf{x}}=\begin{bmatrix}
\partial D/\partial x \\
\partial D/\partial y \\
\partial D/\partial\sigma
\end{bmatrix}
\end{align}
$$

Gradients are evaluated by calculating the difference of neighboring pixels. The new location $\hat{\textbf{x}}$ is obtained by setting the derivative to zero.

$$\hat{\textbf{x}}=-\textbf{H}^{-1}(\nabla D)$$

To eliminate key points with low contrast and poorly localized flat regions, key points with a difference below a threshold are removed.

$$|D(\hat{\textbf{x}})|<0.03$$

Edge responses (i.e., simple lines) are characterized by high curvature in one direction and low curvature in a perpendicular direction. They are not helpful in characterizing an object. **Since the two eigenvalues of the Hessian matrix $\textbf{H}$ are proportional to the curvature, key points with ratios larger than a threshold are removed.**

$$r>10$$

### Edge Response Derivation
We know a more accurate localization of the key point from the [[#Key Point Localization|Taylor series expansion]]. We obtain the Hessian matrix $\textbf{H}$.

$$\textbf{H}=\begin{bmatrix}
\dfrac{\partial^2D}{\partial x^2} & \dfrac{\partial^2 D}{\partial x\partial y} \\
\dfrac{\partial^2D}{\partial y\partial x} & \dfrac{\partial^2D}{\partial y^2}
\end{bmatrix}=\begin{bmatrix}
D_{xx} & D_{xy} \\
D_{yx} & D_{yy}
\end{bmatrix}
$$

The two eigenvalues of the matrix $\textbf{H}$ (*two dimensions*) are represented as $\alpha$ (*larger*) and $\beta$ (*smaller*). The ratio between the two eigenvalues can characterize an edge response.

$$r=\frac{\alpha}{\beta}$$

We can also calculate the trace and the determinant of the matrix.

$$
\begin{gather}
\text{Tr}(\textbf{H})=D_{xx}+D_{yy}=\alpha+\beta \\
\text{Det}(\textbf{H})=D_{xx}D_{yy}-(D_{xy})^2=\alpha\beta
\end{gather}
$$

The ratio between the square of the trace and the determinant is at a minimum when the two eigenvalues are equal.

$$\frac{[\text{Tr}(\textbf{H})]^2}{\text{Det}(\textbf{H})}=\frac{(\alpha+\beta)^2}{\alpha\beta}=\frac{(r\beta+\beta)^2}{r\beta^2}=\frac{(r+1)^2}{r}$$

## Example
A sample image and the obtained key points are shown below.

![[image-processing-sift-ex-1.png|600]]

Even after scaling or rotation, the key points can still be used to match the altered image with the original image.

![[image-processing-sift-ex-2.png|600]]
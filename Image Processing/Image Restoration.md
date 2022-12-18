# Degradation-Restoration Model

<span style = "color:lightblue">Image degradation</span> can be caused due to [[#Modeling Noise|noise]] in transmission or imperfect image acquisition (e.g., quality of sensor or environmental conditions).

$$f(x,y)\rightarrow\text{degradation}\rightarrow\text{noise}\rightarrow\text{restoration}\rightarrow\hat{f}(x,y)$$
The degradation function $\mathcal{H}$ is assumed to be **linear** and **position-invariant**. The process is represented below in the spatial and frequency domains (*see [[Frequency Filtering#Filtering|frequency filtering]]*).

$$
\begin{gather}
	g(x,y)=h(x,y)\star f(x,y)+\eta(x,y) \newline \newline
	G(u,v)=H(u,v)F(u,v)+N(u,v)
\end{gather}
$$

<span style = "color:lightblue">Image restoration</span> refers to the process of removing distortion from an image to objectively recreate the original image (*many applications*). **The degradation can be modeled with prior knowledge, so that the inverse process can be applied.**

<span style = "color:lightblue">Image enhancement</span> refers to the process of *improving* an image subjectively.


> [!INFO]
> Noise can be deduced from areas with **reasonably constant background intensity** (e.g., black or white areas). Any deviation in these areas is caused by noise.

# Modeling Noise
<span style = "color:lightblue">Image noise</span> is random variation of brightness or color information in images and is usually an aspect of electronic noise. It is not present in the original image.
- In <span style = "color:lightblue">charged-coupled device (CCD)</span> cameras, noise is caused by light levels and sensor temperature.
- In <span style = "color:lightblue">magnetic resonance imaging (MRI)</span>, noise is caused by magnetic field strength and temperature.
- Images are also corrupted by interference during transmission.

When modeling additive noise, the following assumptions are made.
1. The noise is uncorrelated with the image.
2. The noise is independent of spatial location (*unless it's periodic noise*).

> [!INFO]
> **Periodic noise** is spatially dependent and can be filtered out by frequency domain filtering.

Several models of noise and their effect on an image and its histogram are demonstrated in the following sections.

![[image-noise-original.png|600]]

![[image-noise-summary.png|600]]

## Gaussian
The probability distribution function of the <span style = "color:lightblue">Gaussian noise</span> is shown below, where $z$ represents the intensity.

$$p(z)=\frac{1}{\sqrt{2\pi}\sigma}\exp\left[-\frac{(z-\bar{z})^2}{2\sigma^2}\right]$$
Gaussian noise can occur due to **poor illumination** or **high temperature**.

![[image-noise-gaussian.png|600]]

## Rayleigh
The probability distribution function of the <span style = "color:lightblue">Rayleigh noise</span> is shown below.

$$
\begin{gather}
	p(z)=
	\begin{dcases}
		\frac{2}{b}(z-a)\exp\left[-\frac{(z-a)^2}{b}\right] & \text{for }z\geq a \vphantom{\frac{0}{0}} \\
		0 \vphantom{\frac{0}{0}} & \text{for } z < a
	\end{dcases} \\
	\bar{z}=a+\sqrt{\frac{\pi b}{4}} \newline
	\sigma^2=\frac{b(4-\pi)}{4}
\end{gather}
$$
Compared to [[#Gaussian|Gaussian noise]] the density is skewed to the right, where $a$ creates an offset.

![[image-noise-rayleigh.png|600]]

It can be caused by **range imaging** or **background modeling for MRIs**.

## Erlang
The probability distribution function of the <span style = "color:lightblue">Erlang noise</span> is shown below, where $a>b$.

$$
\begin{gather}
	p(z)=
	\begin{dcases}
		\frac{a^bz^{b-1}}{(b-1)!}\exp(-az) \vphantom{\frac{0}{0}} & \text{for }z\geq0 \newline
		0 \vphantom{\frac{0}{0}} & \text{for } z < 0
	\end{dcases}
	\newline
	z=\frac{b}{a} \newline
	\sigma^2=\frac{b}{a^2}
\end{gather}
$$
Compared to [[#Rayleigh|Rayleigh noise]], the density is also skewed to the right but with no offset.

![[image-noise-erlang.png|600]]

It can be caused by **laser imaging**.

## Exponential
The probability distribution function of the <span style = "color:lightblue">exponential noise</span> is shown below, where $a>0$.

$$
\begin{gather}
	p(z)=
	\begin{dcases}
		a\exp(-az) \vphantom{\frac{0}{0}} & \text{for } z\geq0 \newline
		0 \vphantom{\frac{0}{0}} & \text{for } z < 0
	\end{dcases}
	\newline
	\bar{z}=\frac{1}{a} \newline
	\sigma^2=\frac{1}{a^2}
\end{gather}
$$
The exponential noise is a modification of the [[#Erlang|Erlang noise]] by setting $b$ to $1$.

![[image-noise-exponential.png|600]]

## Uniform
The probability distribution function of the <span style = "color:lightblue">uniform noise</span> is shown below. 

$$
\begin{gather}
	p(z)=
	\begin{dcases}
		\frac{1}{b-a} \vphantom{\frac{0}{0}} & \text{for }a\leq z\leq b\newline
		0 \vphantom{\frac{0}{0}} & \text{otherwise}
	\end{dcases}
	\newline
	\bar{z}=\frac{a+b}{2} \newline
	\sigma^2=\frac{(b-a)^2}{12}
\end{gather}
$$
It adds a flat value between $a$ and $b$.

![[image-noise-uniform.png|600]]

## Impulse Random Noise
The <span style = "color:lightblue">impulse random noise</span> is also referred to as the <span style = "color:lightblue">salt-and-pepper</span> noise.

$$
p(z)=
\begin{dcases}
	P_s \vphantom{\frac{0}{0}}& \text{for } z = 2^k - 1\newline
	P_p \vphantom{\frac{0}{0}}& \text{for } z = 0 \newline
	1-(P_s+P_p) \vphantom{\frac{0}{0}}& \text{for } z= V
\end{dcases}
$$
> [!INFO]
> Pepper noise is represented by $P_p$, while salt noise is represented by $P_s$.

If $P_s$ or $P_p$ is zero, the impulse noise is <span style = "color:lightblue">unipolar</span>.

If neither $P_s$ nor $P_p$ are zero (*especially if they're equal*), noise values will either be white (value of $2^k-1$) or black (value of $0$). **The noise will resemble salt and pepper granules distributed randomly over the image.**

![[image-noise-salt-pepper.png|600]]

# Estimation of Noise Parameters
In the spatial domain, the noise parameters are estimated from patches of **reasonably constant background intensity** in the image. On the other hand, periodic noise parameters are estimated from the [[Frequency Filtering#Spectrum Phase Angle|Fourier spectrum]].

$$\text{observe}\rightarrow\text{filter}\rightarrow\text{adjust}$$

If the imaging system is available, the parameters *may* be estimated from the system (e.g., capturing "flat" images). However, it is normally necessary to estimate them from image arrangements.

## Region of Interest
The <span style = "color:lightblue">image region of interest (ROI)</span> is a small strip obtained from the background of an image, where the mean $\bar{z}$ and variance $\sigma^2$ of the gray levels in the strip are calculated.

$$
\begin{gather}
	\bar{z} = \sum_{i=0}^{L-1}z_ip_s(z_i) \newline
	\sigma^2 = \sum_{i=0}^{L-1}(z_i-\bar{z})^2p_s(z_i)
\end{gather}
$$
Here, the pixel intensities $z_i$ which range from $0$ to $L-1$ are summarized, where:
- $S$: the strip of sub-image
- $p_s(z_i)$: the probability estimates (i.e., normalized histogram values) of the pixel intensities
- $L$: the maximum intensity value in the entire image (e.g., $256$ for an 8-bit image)

![[image-restore-roi.png|200]]

In the example above, by performing statistics on a strip of the background of the original image, the intensities follow a Gaussian distribution.

# Mean Filters
Since generated noise creates fluctuations in the pixel intensities, the objective of <span style = "color:lightblue">mean filters</span> is to average out the intensity values.

All mean filters perform averaging within an area (i.e., a kernel) defined by $S_{xy}$ with dimensions $m\times n$. New values in the restored image $\hat{f}$ are calculated from old values in the corrupted image $g$.

## Arithmetic
The <span style = "color:lightblue">arithmetic mean filter</span> is a linear filter that assigns new values based on the arithmetic mean.

$$\hat{f}(x,y)=\frac{1}{mn}\sum_{(r,c)\in S_{xy}}{g(r,c)}$$
A spatial kernel with size $m\times n$ will have coefficients of $\frac{1}{mn}$. It can remove continuous noise like [[#Gaussian|Gaussian noise]].

## Geometric
The <span style = "color:lightblue">geometric mean filter</span> is a non-linear filter that assigns new values based on the geometric mean.

$$\hat{f}(x,y)=\left[\prod_{(r,c)\in S_{xy)}}{g(r,c)}\right]^{\frac{1}{mn}}$$

This filter achieves **smoothing** comparable to an [[#Arithmetic|arithmetic mean filter]] but tends to **preserve more image detail**.

It can remove [[#Impulse Random Noise|salt noise]] (*values with maximum intensity*) but not [[#Impulse Random Noise|pepper noise]] (*values with no intensity*). This is because values of $0$ will cause the product to equate to $0$ as well.

## Harmonic
Like the [[#Geometric|geometric mean filter]], the <span style = "color:lightblue">harmonic mean filter</span> is a non-linear filter that works well for [[#Impulse Random Noise|salt noise]] but fails for [[#Impulse Random Noise|pepper noise]]. It also works well with [[#Gaussian|Gaussian noise]].

$$\hat{f}(x,y)=\frac{mn}{\sum_{(r,c)\in S_{xy}}{\frac{1}{g(r,c)}}}$$
## Contraharmonic
The <span style = "color:lightblue">contraharmonic mean filter</span> is a non-linear filter that combines the filters in the previous sections into a single equation.

$$\hat{f}(x,y)=\frac{\sum_{(r,c)\in S_{xy}}g(r,c)^{Q+1}}{\sum_{(r,c)\in S_{xy}}g(r,c)^{Q}}$$

The behavior of the filter is controlled by adjusting the order of the filter $Q$.
- $Q>0$: removes pepper noise
- $Q<0$: removes salt noise
- $Q=0$: arithmetic mean filter
- $Q=-1$: harmonic mean filter

### Example
An image corrupted with pepper noise with a probability of $0.1$ (a) and an image corrupted with salt noise with the same probability (b) are shown below. The resultant filtering with a $3\times 3$ contraharmonic filter with $Q=1.5$ (*good for pepper noise*) (c) and the resultant filtering with the same filter with $Q=-1.5$ (*good for salt noise*) (d) are also shown.

![[image-restore-contraharmonic-1.png|600]]

Alternatively, the image below shows the result if the $Q$ values were swapped with each other (i.e., not their intended use).

![[image-restore-contraharmonic-2.png|600]]

The pepper and salt noises worsen in their respective images.

# Order-statistic Filters
Similar to [[#Mean Filters|mean filters]], <span style = "color:lightblue">order-statistic filters</span> attempt to reduce image noise. However, they are non-linear, where they first sort and then perform statistic operations on the pixel values.

## Median
The <span style = "color:lightblue">median filter</span> assigns the pixel value based on the median of the sorted pixel values in the filter region. Median filters of varying radii are shown below.

![[image-processing-median-filter.png]]

Compared to linear filters, this filter removes impulse noise (e.g., [[#Impulse Random Noise|bipolar and unipolar noise]]), avoids excessive smoothing (i.e., less blurring), and preserves the image edges.

The figure below shows an image corrupted by [[#Impulse Random Noise|salt and pepper noise]] (a) which undergoes median filtering with a filter size of $3\times 3$ (b) and is repeated twice (c) (d).


![[image-processing-median-filter-2.png|600]]

> [!INFO]
> Repeated median filtering will remove most of the noise while increasing image blurring.

## Maximum
The <span style = "color:lightblue">maximum filter</span> finds the extreme points in the filter region.

$$\hat{f}(x,y)=\max_{(r,c)\in S_{xy}}\{g(r,c)\}$$

This filter is useful in finding the **brightest points** in an image or for **eroding dark regions adjacent to bright areas**.

## Minimum
Similar to the [[#Maximum|maximum filter]], the <span style = "color:lightblue">minimum filter</span> also finds the extreme points in the filter region.

$$\hat{f}(x,y)=\min_{(r,c)\in S_{xy}}\{g(r,c)\}$$

This filter is useful in finding the **darkest points** in an image or for **eroding light regions adjacent to dark areas**.

## Midpoint
Combining [[#Mean Filters|averaging]] and [[#Order-statistic Filters|order-statistics]], the <span style = "color:lightblue">midpoint filter</span> computes the midpoint between the brightest and darkest intensity values in the filter region.

$$\hat{f}(x,y)=\frac{1}{2}\left[\max_{(r,c)\in S_{xy}}\{g(r,c)\}+\min_{(r,c)\in S_{xy}}\{g(r,c)\}\right]$$

This filter is useful for reducing randomly distributed noise (e.g., [[#Gaussian|Gaussian noise]]) but performs poorly with impulse noise (*extreme values*).

![[image-processing-midpoint-ex.png|600]]

The resultant images of applying the midpoint filter to different noise types are shown above.

## Alpha-trimmed Mean
The <span style = "color:lightblue">alpha-trimmed mean filter</span> deletes the $d/2$ lowest and highest intensity values and averages the remaining $mn-d$ pixels in the filter region.

$$\hat{f}(x,y)=\frac{1}{mn-d}\sum_{(r,c)\in S_{xy}}g(r,c)$$

Here, $g$ represents the remaining $mn-d$ pixels. This filter becomes the [[#Arithmetic|arithmetic mean filter]] if $d=0$ and becomes the median filter if $d=mn-1$ (*the lowest and highest pixel values are removed*).

This filter is useful in images involving **multiple noise types**, such as a combination of [[#Impulse Random Noise|impulse noise]] and [[#Gaussian|Gaussian noise]].

# Adaptive Filters
<span style = "color:lightblue">Adaptive filters</span> change the filter behavior based on statistical characteristics, specifically the mean $\bar{Z}_{S}$, variance of the pixel intensities $\sigma^2_{S}$, and variance of the noise $\sigma^2_\eta$, of the filter region.

## Local Noise Reduction
The <span style = "color:lightblue">adaptive local noise reduction filter</span> returns different values based on conditions.

$$\hat{f}(x,y)=g(x,y)-\frac{\sigma^2_\eta}{\sigma^2_S}\left[g(x,y)-\bar{Z}_S\right]$$

The filter attempts to both **reduces local noise** and **preserves edges or boundaries**, based on the following conditions.
- $\sigma^2_\eta=0\rightarrow$ return the value of $g(x,y)$ (*no noise!*)
- $\sigma^2_S=\sigma^2_\eta\rightarrow$ return the [[#Arithmetic|local arithmetic mean]] of the filter region to reduce noise
- $\sigma^2_S>\sigma^2_\eta\rightarrow$ return a value close to $g(x,y)$ to preserve edges
- $\sigma^2_S<\sigma^2_\eta\rightarrow$ set the term for the ratio between the noise variance $\sigma^2_\eta$ and the intensity variance $\sigma^2_S$ to $1$

The figure below shows an image corrupted by additive [[#Gaussian|Gaussian noise]] of zero mean and variance of $1000$ (a), the result of [[#Arithmetic|arithmetic mean filtering]] (b), the result of [[#Geometric|geometric mean filtering]] (c), and the result of adaptive local noise reduction filtering (d). All filters have a size of $7\times 7$.

![[image-processing-local-noise-reduce.png|600]]

## Adaptive Median
The <span style = "color:lightblue">adaptive median filter</span> computes the median at two processing levels $A$ and $B$ based on the following algorithm.

$$
\begin{align}
	\text{Level A:} & \newline
	& if(Z_{min}<Z_{med}<Z_{max}): \newline
	& \quad\quad\text{go to $B$} \newline
	& else: \newline
	& \quad\quad\text{increase size of $S_{xy}$} \newline
	& if(S_{xy}\leq S_{max}):\newline
	& \quad\quad\text{repeat $A$} \newline
	& else: \newline
	& \quad\quad \text{return $Z_{med}$}\newline
	\text{Level B:} & \newline
	& if(Z_{min}<Z_{xy}<Z_{max}): \newline
	& \quad\quad \text{return $Z_{xy}$} \newline
	& else: \newline
	& \quad\quad \text{return $Z_{med}$}
\end{align}
$$

Here, level $A$ determines if the **median** is an impulse (*otherwise, increase the filter region size*), and level $B$ determines if the current **image intensity value** $Z_{xy}$ is an impulse.

# Periodic Noise Reduction
Periodic image noise is removed by modifying the Fourier spectrum of an image.

## Notch
The <span style = "color:lightblue">notch reject</span> $H_{NR}$ and <span style = "color:lightblue">notch pass</span> $H_{NP}$ filters prohibit and allow the specified region in the Fourier spectrum respectively.

$$
\begin{gather}
	H_{NR}(u,v)=\prod_{k=1}^{Q}H_k(u,v)H_{-k}(u,v) \newline
	H_{NP}=1-H_{NR}
\end{gather}
$$

In the above equation, $H_k$ and $H_{-k}$ are high-pass filter transfer functions centered at $(u_k, v_k)$ and $(u_{-k}, v_{-k})$ respectively.

For example, the [[Frequency Filtering#Butterworth|Butterworth]] notch reject filter transfer functions of order $n$ with **three** notch pairs are shown below.

$$H_{NR}(u,v)=\prod_{k=1}^{3}\left[\frac{1}{1+\left[D_{0k}/D_k(u,v)\right]^n}\right]\left[\frac{1}{1+\left[D_{0k}/D_{-k}(u,v)\right]^n}\right]$$

The figure below shows an image corrupted by sinusoidal interference (a), the spectrum causing the interference (b), the Notch reject filter used to eliminate the interference (c), and the resultant image after filtering (d).

![[image-processing-notch-reject.png|600]]

Alternatively, if a notch pass filter was used instead, only the spatial interference would be shown.

# Restoration
Theoretically, if the image degradation and the noise functions are known, the original image can be recovered.

The image degradation function can be estimated by **observation**, **experimentation**, or **mathematical modeling**.

## Inverse
Given that the degradation function $H$ is known, the original image $\hat{F}$ can be obtained from the degraded image $G$ by inverting the operation.

$$
\hat{F}(u,v)=\frac{G(u,v)}{H(u,v)}
$$

> [!INFO]
> In areas with strong signals, the effect of the noise is negligible. In strong noise areas, however, the image cannot be restored properly if noise is not known.

$$
\begin{gather}
	G(u,v)=\underbrace{F(u,v)}_{\text{original}}\underbrace{H(u,v)}_{\text{degrade}}+\underbrace{N(u,v)}_{\text{noise}} \newline \newline
	\hat{F}(u,v)=F(u,v)+\frac{N(u,v)}{H(u,v)}
\end{gather}
$$

### Zero Denominator Problem
If the value of $H$ becomes very small, however, the ratio will become exponentially large and will dominate the calculation.

To solve this problem, a cutoff threshold is implemented, where analysis is limited to frequencies near the origin. This reduces the probability of finding small values of $H$.

![[image-processing-inverse-filter.png|600]]

In the above figure, inverse filtering is done at different cutoff radii.

## Wiener
The <span style = "color:lightblue">Wiener filter</span> (<span style = "color:lightblue">minimum mean square error (MSE) filtering</span>) incorporates the degradation function and statistical characteristics of the noise (e.g., <span style = "color:lightblue">signal-to-noise ratio</span>) into the restoration process. It minimizes the mean square error and does not have the [[#Zero Denominator Problem|zero denominator problem]] of inverse filtering.

$$\hat{F}(u,v)=\left[\frac{1}{H(u,v)}\cdot\frac{|H(u,v)|^2}{|H(u,v)|^2+K}\right]G(u,v)\quad\text{where }K=\frac{|N(u,v)|^2}{|F(u,v)|^2}$$

The power spectrum of the noise is represented as $|N(u,v)|^2$, and that of the original image is represented as $|F(u,v)|^2$.

The figure below shows (1) full inverse filtering, (2) radially limited inverse filtering, and (3) Wiener filtering.

![[image-processing-wiener-filter.png|600]]

This filter is more robust to noise and preserves high-frequency details.
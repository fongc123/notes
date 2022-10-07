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

![[Pasted image 20221006234256.png|600]]

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
	\begin{cases}
		\frac{2}{b}(z-a)\exp\left[-\frac{(z-a)^2}{b}\right] & z\geq a \newline
		0 & z < a
	\end{cases}
	\newline
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
	\begin{cases}
		\frac{a^bz^{b-1}}{(b-1)!}\exp(-az) & z\geq0 \newline
		0 & z < 0
	\end{cases}
	\newline
	\bar{z}=\frac{b}{a} \newline
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
	\begin{cases}
		a\exp(-az) & z\geq0 \newline
		0 & z < 0
	\end{cases}
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
	\begin{cases}
		\frac{1}{b-a} & a\leq z\leq b\newline
		0 & \text{otherwise}
	\end{cases}
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
\begin{cases}
	P_s & \text{for } z = 2^k - 1\newline
	P_p & \text{for } z = 0 \newline
	1-(P_s+P_p) & \text{for } z= V
\end{cases}
$$
If $P_s$ or $P_z$ is zero, the impulse noise is <span style = "color:lightblue">unipolar</span>.

If neither $P_s$ nor $P_z$ are zero (*especially if they're equal*), noise values will either be white (value of $2^k-1$) or black (value of $0$). **The noise will resemble salt and pepper granules distributed randomly over the image.**

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

![[Pasted image 20221007180158.png|200]]

In the example above, by performing statistics on a strip of the background of the original image, the intensities follow a Gaussian distribution.

# Mean Filters
Since generated noise creates fluctuations in the pixel intensities, the objective of <span style = "color:lightblue">mean filters</span> is to average out the intensity values.

## Arithmetic
The <span style = "color:lightblue">arithmetic mean filter</span> is a linear filter that assigns 
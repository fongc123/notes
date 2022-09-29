# Frequency Filtering

Established by Jean-Baptiste Joseph Fourier, the <span style = "color:lightblue">Fourier transformation</span> converts spatial coordinates to frequency components.
- simplify problems
- decrease complexity
- some operations in the frequency domain are easier 

## Fourier Series

Fourier claims that a sufficient summation of sinusoidal signals will create any periodic signal.

$$A\sin(\omega x+\phi)$$

A <span style = "color:lightblue">Fourier series</span> can represent **any periodic function** as a discrete weighted sum of sine and cosine functions.

$$
\begin{gather}
	f(t)=\sum_{n=-\infty}^{n=+\infty}{c_n\exp(j\frac{2\pi n}{T}t)}=\sum_{n=-\infty}^{n=+\infty}{c_n\left[\cos(\frac{2\pi n}{T}t)+j\sin(\frac{2\pi n}{T}t)\right]} \newline \newline
	c_n=\frac{1}{T}\int_{-T/2}^{T/2}f(t)\exp(-j\frac{2\pi n}{T}t), \text{ where } n=0,\pm 1,\pm 2, \dots
\end{gather}
$$

<span style = "color:lightblue">Euler's formula</span> converts between the exponential form and the sinusoidal form.

## Fourier Transform

A <span style = "color:lightblue">Fourier transform</span> is a mathematical transform that decomposes **an arbitrary function with finite duration (non-periodic function)** into weighted integrals of sine and cosine functions.

> [!INFO]
> A Fourier transform is lossless (i.e., the original spatial function can be recovered from the frequency domain).

### 1D Continuous
The expression for a **continuous** one-dimensional Fourier transform is shown below, where the spatial domain is converted into the frequency domain.

$$
F(u)=\mathcal{F}\{f(t)\}=\int_{-\infty}^{\infty}{f(t)\exp(-j2\pi ut)dt}
$$
Additionally, the expression for the **continuous** inverse Fourier transform is also shown below, where the frequency domain is converted back to the spatial domain.

$$
f(t)=\mathcal{F}^{-1}\{F(u)\}=\int_{-\infty}^{\infty}{F(u)\exp(j2\pi ut)du}
$$

### 1D Discrete
The expressions for the discrete counterparts are shown below.

$$
\begin{gather}
	F(u)=\sum_{x=0}^{M-1}{f(x)\exp(-\frac{2\pi ux}{M})},\text{ where } u=0,1,\dots,M-1 \newline\newline
	f(x)=\frac{1}{M}\sum_{u=0}^{M-1}{F(u)\exp(\frac{j2\pi ux}{M})}, \text{ where }x=0,1,\dots,M-1
\end{gather}
$$

Both inputs and outputs are finite.

### 2D Discrete
The expression for the two-dimensional discrete counterparts are shown below, where $f(x,y)$ is a digital image of size $M\times N$.

$$
\begin{gather}
	F(u,v)=\sum_{x=0}^{M-1}\sum_{y=0}^{N-1}{f(x,y)\exp\left[-j2\pi\left(\frac{ux}{M}+\frac{vy}{M}\right)\right]} \newline \newline
	f(x,y)=\frac{1}{MN}\sum_{x=0}^{M-1}\sum_{y=0}^{N-1}{F(u,v)\exp\left[j2\pi\left(\frac{ux}{M}+\frac{vy}{N}\right)\right]}
\end{gather}	
$$

> [!INFO]
> The **average intensity of the image** is obtained when $u=0$ and $v=0$ in the frequency domain.
> $$F(0,0)=\sum_{x=0}^{M-1}\sum_{y=0}^{N-1}{f(x,y)}=MN\bar{f}$$

One-dimensional Fourier transform properties (e.g., time shift, frequency shift, rotation) apply to two-dimensional Fourier transform as well.

$$
\begin{align}
	\text{translation:}\quad & f(x,y)\exp\left[j2\pi\left(\frac{u_0 x}{M}+\frac{v_0 y}{N}\right)\right] \longleftrightarrow F(u-u_0,v-v_0) \newline \newline
	& f(x-x_0,y-y_0)\longleftrightarrow F(u,v)\exp\left[-j2\pi \left(\frac{ux_0}{M}+\frac{vy_0}{N}\right)\right] \newline\newline
	\text{rotation:}\quad & f(r,\theta+\theta_0)\longleftrightarrow F(\omega,\phi+\theta_0) \quad\small\text{(using polar coordinates)}
\end{align}
$$

### Spectrum & Phase Angle
Additional components related to the Fourier transform are listed below.

$$
\begin{align}
	\text{real \& imaginary:}\quad & F(u,v)=R(u,v)+jI(u,v) \newline\newline
	\text{2D polar form:}\quad & F(u,v)=|F(u,v)|\exp\left[j\phi(u,v)\right] \newline\newline
	\text{Fourier spectrum:}\quad & |F(u,v)|=\sqrt{R^2(u,v)+I^2(u,v)} \newline\newline
	\text{Power spectrum:}\quad & P(u,v)=|F(u,v)|^2 \newline\newline
	\text{Phase angle:}\quad & \phi(u,v)=\arctan\left[\frac{I(u,v)}{R(u,v)}\right]
\end{align}
$$

In image processing, the <span style = "color:lightblue">Fourier spectrum</span> determines the intensities in the image, while the <span style = "color:lightblue">phase angle</span> carries information about the location of discernible objects in the image. **The Fourier spectrum and the phase angle are both needed to faithfully reconstruct an image.**

> [!INFO]
> Amplitudes and phase angles of an image can be swapped with those from other images. This can be applied to deep learning to create additional training set images from one source image. The semantics of the source image are still retained. *See [A Fourier-based Framework for Domain Generalization](https://openaccess.thecvf.com/content/CVPR2021/papers/Xu_A_Fourier-Based_Framework_for_Domain_Generalization_CVPR_2021_paper.pdf).*
> 
> ![[image-processing-amp-phase-swap.png|600]]

### Properties
The properties of the Fourier transform are listed below.

![[image-processing-ft-properties.png|600]]

> [!TIP]
> Convolution in the spatial domain corresponds to multiplication in the frequency domain. Thus, it is computationally easier to perform a convolutional operation in the frequency domain than in the spatial domain.
> $$
> \begin{gather}
> 	f(t) \star h(t) \longleftrightarrow H(u)F(u) \newline \newline
> 	f(t)h(t) \longleftrightarrow H(u) \star F(u)
> \end{gather}
> $$


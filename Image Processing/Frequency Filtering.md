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


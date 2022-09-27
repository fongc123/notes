# Frequency Filtering

Established by Jean-Baptiste Joseph Fourier, the <span style = "color:lightblue">Fourier transformation</span> converts spatial coordinates to frequency components $u$ and $v$.
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
	c_n=\frac{1}{T}\int_{-T/2}^{T/2}f(t)\exp(-j\frac{2\pi n}{T}t)\space , \text{ where } n=0,\pm 1,\pm 2, \dots
\end{gather}
$$

## Fourier Transform

A <span style = "color:lightblue">Fourier transform</span> is a mathematical transform that decomposes **an arbitrary function with finite duration (non-periodic function)** into weighted integrals of sine and cosine functions.

> [!INFO]
> A Fourier transform is lossless (i.e., the original spatial function can be recovered from the frequency domain).

### Continuous
The expression for a **continuous** one-dimensional Fourier transform is shown below, where the spatial domain is converted into the frequency domain.

$$
F(u)=\mathcal{F}\{f(t)\}=\int_{-\infty}^{\infty}{f(t)\exp(-j2\pi ut)dt}
$$
Additionally, the expression for the **continuous** inverse Fourier transform is also shown below, where the frequency domain is converted back to the spatial domain.

$$
f(t)=\mathcal{F}^{-1}\{F(u)\}=\int_{-\infty}^{\infty}{F(u)\exp(j2\pi ut)du}
$$

### Discrete


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


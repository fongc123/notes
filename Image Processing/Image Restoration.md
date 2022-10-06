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

## Gaussian
The PDF of Gaussian noise is shown below, where $z$ represen

$$p(z)=\frac{1}{\sqrt{2\pi}\sigma}\exp\left[-\frac{(z-\bar{z})^2}{2\sigma^2}\right]$$
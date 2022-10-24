<span style = "color:lightblue">Image compression</span> refers to the process of **reducing the amount of data** to represent the same information (i.e., removal of redundant data).
- An image with six million pixels (size: $3000\times 2000$) takes 18 MB of size (56 pictures $\rightarrow$ 1 GB).
- A $352\times 240$ RGB video with 15 frames per second requires 3.8 MB per second.

> [!INFO]
> **Wikipedia**: "Data compression, or source coding, is the process of encoding information <span style = "color:mistyrose">using fewer bits</span> than an unencoded representation would use through the use of specific encoding schemes."

> [!WARNING]
> **Data** and **information** are different. Data is the means by which information is conveyed.

The <span style = "color:lightblue">relative data redundancy</span> $R$ measures the amount of redundant data between two representations, where $C$ is the compression ratio, $b$ is the number of bits of the uncompressed image, and $b'$ is the number of bits of the compressed representation.

$$
\begin{gather}
	R=1-\frac{1}{C} \\
	C=\frac{b}{b'}
\end{gather}
$$

The goal of compression is to **remove redundancy and reduce irrelevance**. Redundancy can be categorized into **coding redundancy**, **spatial redundancy**, and **irrelevant information**.
- <span style = "color:lightblue">irrelevance or perceptual redundancy</span>: not all visual information is perceived by the [[Acquisition & Representation#The Eye|eye]]
- <span style = "color:lightblue">redundancy</span>: unnecessary representation

# Redundancy
<span style = "color:lightblue">Information theory</span> models information as a probabilistic process to determine the **minimum amount of data required** without losing information during a redundancy reduction operation.

$$I(E)=\log_b{\frac{1}{P(E)}}=-\log_b{P(E)}$$

A random event $E$ with probability $P(E)$ contains $I(E)$ units of information, where $b$ is the unit used to measure information ($b=2$ for bit).
- $P(E)=1\rightarrow I(E)=0$: no information is attributed to the event, as it occurs all the time
- $P(E)=0.5\rightarrow I(E)=1$: information is $1$ bit (i.e., one of two equally likely outcomes)

$$\hat{H}=-\sum_{k=0}^{L-1}{p_r(r_k)\log_2{p_r(r_k)}}$$

The <span style = "color:lightblue">entropy</span> $\hat{H}$ is the average information per intensity source output. A <span style = "color:lightblue">zero-memory source</span> consists of random events (i.e., <span style = "color:lightblue">source symbols</span>) that are [[Data Preprocessing#Probability & Independence|statistically independent]].

> [!INFO]
> **Shannon's first theorem:** Given that the pixels are statistically independent, it is not possible to code the intensity values of the image source with fewer bits than $\bar{H}$ bits per pixel.

For example, the entropy in [[#Coding#Example|this example]] is calculated.

$$\bar{H}=-\left[0.25\log_20.25+0.47\log_20.47+0.25\log_20.25+0.03\log_20.03\right]\approx1.66\space\text{bits per pixel}$$

Thus, it is not possible to code the intensity values of the image sources with less than $1.66$ bits per pixel.

## Coding
In <span style = "color:lightblue">coding redundancy</span>, a simpler code is used to represent the data. A <span style = "color:lightblue">code</span> is a system of symbols used to represent information or a set of events.
- **natural $m$-bit fixed-length encoding**: binary code where each piece of information is assigned one of $2^m$ codes from an $m$-bit binary counting sequence
- **variable-length encoding**: assign bits to more probable intensity values with fewer bits

The expression for the average number of bits used to encode the intensities is shown below, where $m=8$ for a standard $8$-bit binary counting sequence and $l$ is the number of bits used to represent an intensity value.
$$L_{avg}=\sum_{k=0}^{m-1}l_1(r_k)p_r(r_k)$$
### Example
The intensity distribution of an image is shown below.

![[image-processing-compression-coding.png|600]]

The natural $8$-bit encoding can represent up to $256$ intensity values, but the image only has four distinct intensity values.

$$
\begin{align}
L_{avg}=&0.25(2)+0.47(1)+0.25(3)+0.03(3) \\
L_{avg}=&1.81\space\text{bits}
\end{align}
$$
By using only a maximum of $3$ bits, the image can be represented with $1.81$ bits, where the redundancy is approximately $77.4\%$.

$$
\begin{gather}
	C = \frac{8}{1.81}\approx4.42 \\
	R = 1-\frac{1}{C}\approx0.774
\end{gather}
$$

## Spatial
In <span style = "color:lightblue">spatial or temporal redundancy</span>, neighboring pixels usually have similar intensities and may be represented more efficiently (i.e., <span style = "color:lightblue">mapping</span>).

> [!WARNING]
> A mapping is **reversible** only if the original pixels can be reconstructed from the transformed representation.

<span style = "color:lightblue">Run-length coding</span> creates run-length pairs, where each pair represents (1) **the start of a new intensity value** and (2) **the number of consecutive pixels that have that intensity**.

<span style = "color:lightblue">Quantization</span> is an **irreversible** operation that maps a broad range of input values to a limited number of output values.

In <span style = "color:lightblue">perceptual redundancy</span>, there may be situations where an image is *seemingly* uniform but have clear details after histogram equalization. If spatial redundancy is reduced, information will be lost.

### Example
An image of horizontal lines with varying intensity and its corresponding histogram are shown below.

![[image-processing-compression-spatial-redundancy.png|600]]

Each pair can represent the intensity value and the number of pixels that have that intensity. In the original image, each pixel (for a total of $256\times256$ pixels) is represented by $8$ bits.

$$
\begin{align}
	\text{original: }&256\times256\times8 \\
	\text{transformed: }&(256+256)\times8 \\\\
	C&=128:1
\end{align}
$$

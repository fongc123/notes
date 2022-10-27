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
- **variable-length encoding**: assign varying number of bits to intensity levels based on their probability (e.g., less bits to more probable intensities)

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
# Model
The image compression model consists of the <span style = "color:lightblue">source encoder</span>, which reduces or eliminates any coding, interpixel, or psychovisual (i.e., perceptual) redundancies, and the <span style = "color:lightblue">decoder</span>, which performs the inverse operations of the encoder.
- <span style = "color:lightblue">mapper</span>: reversible process that transforms input image data to reduce interpixel redundancies (e.g., [[#Spatial|run-length coding]])
- <span style = "color:lightblue">quantizer</span>: **irreversible** process that reduces the accuracy of the mapper to reduce perceptual redundancies (i.e., account for fewer pixels)
- <span style = "color:lightblue">symbol coder</span>: reversible process that creates a fixed-length or variable-length code to represent the output of the quantizer

The output of the encoder is typically **non-visual**. Thus, the decoder must retrieve the image from the code.

> [!INFO]
> Normally, a [[#Coding|variable-length code]] is used to represent **mapped** and **quantized** outputs.

![[image-processing-compression-model.png|600]]

> [!INFO]
> Lossless and lossy systems produce different compressed images $\hat{f}$ of the original image $f$.
> - lossless system: $\hat{f}(x,y)=f(x,y)$
> - lossy system: $\hat{f}(x,y)\neq f(x,y)$

# Algorithms
The following compression algorithms pertain to the processes of the [[#Model|symbol coder and decoder]].

## Huffman
Since natural binary encoding of intensity values creates coding redundancy, <span style = "color:lightblue">Huffman encoding</span> performs **variable-length coding** to assign the shortest codes to the most probable intensity values.

> [!INFO]
> Huffman encoding is used in JPEG and MPEG file formats.

### Encoding

The steps of the **encoding** algorithm are detailed below.
1. Order the probabilities of each code.
2. Combine the two codes with the lowest probabilities into a single symbol.
3. Repeat **Step 2** until there are two codes left.
4. Code each reduced source starting with the smallest source and ending with the original source, where the codes in each source reduction step use an additional bit.

The figure below demonstrates steps 1-3.

![[image-processing-huffman-1.png|600]]

Lastly, the figure below demonstrates step 4.

![[image-processing-huffman-2.png|600]]

Thus, codes that represent intensities with high probabilities are assigned smaller bits (e.g., `1` or `00`) and codes that represent intensities with low probabilities are assigned larger bits (e.g., `01010` or `01011`).

### Decoding
A string of Huffman encoded symbols can be decoded simply by examining the individual symbols of the string from left to right. Due to the [[#Encoding|encoding process]], there won't be any duplicates. A decoding example of the [[#Encoding|above]] figures is shown.

$$
\begin{align}
\text{Huffman code:}&\space\underbracket{01010}_{a_3}\underbracket{011}_{a_1}\underbracket{1}_{a_2}\underbracket{1}_{a_2}\underbracket{00}_{a_6} \\\\
\text{Decoded:}&\space a_3\space a_1\space a_2\space a_2 \space a_6
\end{align}
$$

Huffman's procedure creates the optimal code for a set of symbols and probabilities. The code is **instantaneously and uniquely decodable**. After code creation, error-free coding and decoding are accomplished by a simple table lookup.

> [!INFO]
> In practice, a pre-computed Huffman coding table is used (e.g., JPEG and MPEG).

## Lossless Predictive
Since image pixels are often correlated (i.e., similar with each other), the prediction of consecutive pixels can lower the bit rate.

<span style = "color:lightblue">Lossless predictive coding</span> reduces the interpixel (i.e., [[#Spatial|spatial and temporal]]) redundancies by **coding only the new information in each pixel**.

$$\hat{f}(n)=\text{round}\left[\sum_{i=1}^{m}{a_if(n-i)}\right]$$

Normally, prediction is represented as a **linear combination** of $m$ previous samples.
- $\hat{f}(n)$: predicted intensity value
- $f(n)$: original intensity value at $n$
- $\text{round}$: denotes rounding (i.e., similarity) operation
- $m$: number of previous pixels
- $a_i$: coefficients

![[image-processing-lossless-predictive.png|600]]

The encoder consists of a <span style = "color:lightblue">predictor</span>, where only the error $e(n)$ between the original $f$ and the predicted value $\hat{f}$ is encoded using variable-length encoding.

$$e(n)=f(n)-\hat{f}(n)$$

The decoder consists of the same predictor used for encoding, where the image value is obtained by adding the error value to the predicted value.

> [!INFO]
> The error is <u>accurately</u> captured in the encoding process and requires a sufficient number of bits (*see [[#Lossy Predictive|lossy predictive]] for approximated errors*).

### Example
A view of the Earth from an orbiting space shuttle, the prediction error image, and their corresponding intensity histograms are shown below.

![[image-processing-lossless-predictive-ex.png|600]]

The predictions were generated from the equation below.

$$\hat{f}(x,y)=\text{round}\left[\alpha f(x,y-1)\right]$$

By only encoding the prediction error (i.e., the difference), the entropy is reduced from $7.25$ to $3.99$.

## Lossy Predictive
In addition to the predictive model in [[#Lossless Predictive|lossless predictive coding]], we add quantization to map values to a limited range. There is a trade-off between reconstruction accuracy and compression performance; however, the distortion can be tolerable, as the human eye cannot perceive minor differences (i.e., [[#Spatial|perceptual redundancy]]).

In <span style = "color:lightblue">lossy predictive coding</span>, the error between the predicted and the actual images is quantized to a limited range.

$$\dot{e}(n)=\frac{e(n)}{q}$$

The reconstructed image is now the sum of the predicted image and the quantized error $\dot{e}(n)$.

$$\dot{f}(n)=\hat{f}(n)+\dot{e}(n)$$

The predictor obtains new values based on the previous erroneous prediction.

$$\hat{f}(n)=\alpha\dot{f}(n-1)$$

> [!INFO]
> Note the change in notation from the original image $f$ and the erroneous image $\dot{f}$, as the image cannot be completely reconstructed due to the **quantizer**.

![[image-processing-lossy-prediction-model.png|700]]

### Delta Modulation
To achieve quantization, <span style = "color:lightblue">delta modulation</span> is a simple and popular technique that maps its input to two values.

$$\dot{e}(n)=\begin{dcases}
	+\delta & \text{for}\space e(n)>0 \\
	-\delta & \text{otherwise}
\end{dcases}
$$

The value of $\delta$ controls the range of values the input will be mapped to. **The output can be represented with only one bit**.

A small value of $\delta$ can account for **granular noise** (i.e., small errors) but cannot deal with **slope overload** (i.e., large errors). On the other hand, a large value of $\delta$ will disproportionate granular noise. This is demonstrated below, where $\alpha=1$ (*the predictor*) and $\delta=6.5$.

![[image-processing-delta-mod.png|700]]

# Quality Measures & Standards
There are two criteria for assessing compression quality: <span style = "color:lightblue">objective fidelty criteria</span> and <span style = "color:lightblue">subjective fidelty criteria</span>.

> [!INFO]
> **Fidelity** is the degree of exactness with which something is copied or reproduced.

The <span style = "color:lightblue">root mean square (RMS) error</span> and the <span style = "color:lightblue">mean-square signal-to-noise ratio (SNR)</span> are useful in objectively assessing image quality.

$$
\begin{gather}
	RMS = \left[\frac{1}{MN}\sum_{x=0}^{M-1}\sum_{y=0}^{N-1}\left[\hat{f}(x,y)-f(x,y)\right]^2\right]^{0.5} \\\\
	SNR = \dfrac{\sum_{x=0}^{M-1}\sum_{y=0}^{N-1}\hat{f}(x,y)^2}{\sum_{x=0}^{M-1}\sum_{y=0}^{N-1}\left[\hat{f}(x,y)-f(x,y)\right]^2}
\end{gather}
$$

The image quality can also be determined **subjectively**.

![[image-processing-quality-subjective.png|600]]


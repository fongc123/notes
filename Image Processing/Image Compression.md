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

# Coding Redundancy
In <span style = "color:lightblue">coding redundancy</span>, a simpler code is used to represent the data. A <span style = "color:lightblue">code</span> is a system of symbols used to represent information or a set of events.
- **natural $m$-bit fixed-length encoding**: binary code where each piece of information is assigned one of $2^m$ codes from an $m$-bit binary counting sequence
- **variable-length encoding**: assign bits to more probable intensity values with fewer bits

The expression for the average number of bits used to encode the intensities is shown below, where $m=8$ for a standard $8$-bit binary counting sequence.
$$L_{avg}=\sum_{k=0}^{m-1}l_1(r_k)p_r(r_k)$$
## Example
The intensity distribution and the corresponding image are shown below.


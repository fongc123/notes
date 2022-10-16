<span style = "color:lightblue">Image compression</span> refers to the process of **reducing the amount of data** to represent the same information (i.e., removal of redundant data).
- An image with six million pixels (size: $3000\times 2000$) takes 18 MB of size (56 pictures $\rightarrow$ 1 GB).
- A $352\times 240$ RGB video with 15 frames per second requires 3.8 MB per second.

> [!INFO]
> **Wikipedia**: "Data compression, or source coding, is the process of encoding information <span style = "color:mistyrose">using fewer bits</span> than an unencoded representation would use through the use of specific encoding schemes."

> [!WARNING]
> **Data** and **information** are different. Data are the means by which information is conveyed.

The <span style = "color:lightblue">relative data redundancy</span> $R$ measures the amount of redundant data between two representations, where $C$ is the compression ratio, $b$ is the number of bits of the uncompressed image, and $b'$ is the number of bits of the compressed representation.

$$
\begin{gather}
	R=1-\frac{1}{C} \\
	C=\frac{b}{b'}
\end{gather}
$$


Like [[Classification|classification]], image classification assigns a class label to input images. A classification system looks for a set of <span style = "color:lightblue">patterns</span> (i.e., a spatial arrangement of **features**) in an image that are characteristic to a class.

Features can be extracted [[Feature Extraction|manually]] (e.g., signature, boundary, region, texture, SIFT) or with [[Convolutional Neural Networks|data-driven methods]]. With neural networks, features and patterns are automatically learned, and the model uses them to distinguish between classes.

# Prototype Matching
<span style = "color:lightblue">Prototype matching</span> compares an unknown pattern against a set of prototypes and assigns the unknown pattern to the class of the <u>most similar</u> prototype.
- <span style = "color:lightblue">minimum-distance classifier</span>: [[Clustering#Similarity|Euclidean distance]] between the unknown and the pattern mean
- <span style = "color:lightblue">correlation</span>
- <span style = "color:lightblue">matching SIFT key points</span>

## Example: Decision Boundary
With the **minimum-distance classifier** and class means $\textbf{m}_1$ and $\textbf{m}_2$, a decision boundary is calculated.

$$
\begin{gather}
\textbf{m}_1=(4.3,1.3)^T \\
\textbf{m}_2=(1.5,0.3)^T
\end{gather}
$$

The expression for the decision boundary separating between class $c_i$ and $c_j$ is shown below.

$$
\begin{gather}
d_{ij}(\textbf{x})=d_i(\textbf{x})-d_j(\textbf{x}) \\
d_j=\textbf{m}^T_j\textbf{x}-\frac{1}{2}\textbf{m}^T_j\textbf{m}_j\quad\text{for}\space j=1,2,\ldots,N_c
\end{gather}
$$

The class means are inserted into the equation above.

$$
\begin{align}
d_1(\textbf{x})&=\textbf{m}_1^T\textbf{x}-\frac{1}{2}\textbf{m}_1^T\textbf{m}_1 \\
&=\begin{bmatrix}4.3 & 1.3\end{bmatrix}\begin{bmatrix}x_1\\x_2\\\end{bmatrix}-\frac{1}{2}\begin{bmatrix}4.3&1.3\end{bmatrix}\begin{bmatrix}4.3\\1.3\end{bmatrix} \\
&= 4.3x_1+1.3x_2-0.5(4.3^2+1.3^2) \\
&=4.3x_1+1.3x_2-10.09 \\
d_2(\textbf{x})&=\textbf{m}_2^T\textbf{x}-\frac{1}{2}\textbf{m}_2^T\textbf{m}_2 \\
&=1.5x_1+0.3x_2-0.5(1.5^2+0.3^2) \\
&=1.5x_1+0.3x_2-1.17
\end{align}
$$

The expressions are subtracted from each other and set to zero.

$$
\begin{align}
d_{ij}(\textbf{x})&=d_i(\textbf{x})-d_j(\textbf{x})\\
&=2.8x_1+1.0x_2-8.92=0
\end{align}
$$

The line separates between the two classes.

![[image-processing-decision-boundary.png|600]]
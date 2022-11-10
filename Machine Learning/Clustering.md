<span style = "color:lightblue">Clustering</span> groups data into clusters by the similarity of data objects. Unlike [[Classification|classification]], it is an <span style = "color:lightblue">unsupervised</span> learning, as there are no **class labels**.

# Similarity
A <span style = "color:lightblue">similarity measure</span>, such as <span style = "color:lightblue">cosine similarity</span>, calculates how **alike** two objects are.

$$
\cos(x_1,x_2)=\dfrac{x_1\cdot x_2}{||x_1||\cdot||x_2||}
$$

On the other hand, a <span style = "color:lightblue">dissimilarity measure</span>, such as the **Euclidean distance** ($\mathcal{l}_2$-distance) and the **Manhattan distance** ($\mathcal{l}_1$-distance), measures how **different** two objects are.

$$
\begin{align}
\text{Euclidean:} & \quad dist(x_1,x_2)=\sqrt{\sum_{i=1}^{d}{(x_{1i}-x_{2i})^2}} \\\\
\text{Manhattan:} & \quad dist(x_1, x_2)=\sum_{i=1}^{d}|x_{1i}-x_{2i}|
\end{align}
$$

> [!INFO]
> [[Data Preprocessing#Normalization|Normalization]] is necessary to calculate distances fairly.

# $k$-Means

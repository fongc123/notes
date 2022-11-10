<span style = "color:lightblue">Clustering</span> groups data into clusters by the similarity of data objects. Unlike [[Classification|classification]], it is an <span style = "color:lightblue">unsupervised</span> learning, as there are no **class labels**.

# Similarity
A <span style = "color:lightblue">similarity measure</span>, such as <span style = "color:lightblue">cosine similarity</span>, calculates how **alike** two objects are.

$$
\cos(x_1,x_2)=\dfrac{x_1\cdot x_2}{||x_1||\cdot||x_2||}
$$

The <span style = "color:lightblue">simple matching coefficient</span> calculates similarity between binary objects, where $f_{ij}$ represents the number of attributes that the first and second objects have $i$ and $j$ attributes respectively.

$$SMC=\dfrac{f_{11}+f_{00}}{f_{01}+f_{10}+f_{00}+f_{11}}$$

An example is shown below, where $x_1$ and $x_2$ are objects containing binary attributes.

$$
\begin{gather}
x_1=(1,0,0,0) \\ x_2=(0,1,0,0) \\\\
f_{00}=2\quad f_{01}=1\quad f_{10}=1\quad f_{11} = 0 \\\\
\therefore SMC=\dfrac{2}{4}=0.5
\end{gather}
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
The <span style = "color:lightblue">k-means</span> clustering method partitions a dataset $D$ with $N$ number of points into $k$ clusters, where objects in the same cluster $C_i$ are similar.

The expression for the <span style = "color:lightblue">centroid</span> or <span style = "color:lightblue">center of gravity</span> (i.e., the mean) of each cluster is shown below.

$$C_i=\dfrac{1}{N_i}\sum_{X\in C_i}X$$

The steps for a $k$-means clustering algorithm are listed below.
1. Randomly select $k$ points from $D$ as the <u>initial</u> centroids.
2. Form $k$ clusters by assigning each new point to its [[#Similarity|closest]] mean.
3. Recompute the mean for each cluster with the new point.
4. Repeat steps 2 and 3 until there are no changes in the centroid values.

## Limitations
Due to its simplicity, there are several limitations with this method.

1. The algorithm may converge on a <span style = "color:lightblue">local minimum</span> as the initial clusters are **randomly** selected, leading to suboptimal clustering.
	1. **Solution:** perform multiple runs and select the solution with the minimum <span style = "color:lightblue">sum squared error (SSE)</span>
2. The algorithm implicitly assumes that clusters have a circular shape.
3. The number of clusters $k$ has to be selected (*see [[ML Basics#Choosing Hyperparameters|parameter optimization]]*).
	1. **Solution:** perform multiple runs
4. The algorithm is affected by outliers.
	1. **Solution:** remove outliers

$$SSE=\sum_{i=1}^{k}\sum_{x\in C_i}||x-c_i||^2$$

# Hierarchical Clustering

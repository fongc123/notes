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

$$\arg\min_C(\sum_{i=1}^{k}\sum_{z\in C_i}||\textbf{z}-\textbf{m}_i||^2)$$

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
In <span style = "color:lightblue">hierarchical clustering</span>, data objects are grouped into a **tree of clusters** (i.e., clusters $\rightarrow$ sub-clusters $\rightarrow$ sub-sub-clusters). Again, [[#Similarity|similarity measures]] are used, where clusters are **merged** or **split** one at a time.

> [!INFO]
> A [[Multivariate Data#Layout Density|dendrogram]] or a nested cluster diagram are great visualization charts for this clustering method.

There are two types of hierarchical clustering methods.
- <span style = "color:lightblue">agglomerative</span> (*bottom-up*): start with <u>points</u> and <u>merge</u>
- <span style = "color:lightblue">divisive</span> (*top-down*): start with one, all-inclusive <u>cluster</u> and <u>split</u>

The steps for an <u>agglomerative</u> hierarchical clustering algorithm are listed below.
1. Compute <span style = "color:lightblue">distance matrix</span> of the dataset.
2. Initialize points as individual clusters.
3. Merge the two closest clusters.
4. Update distance matrix (*see [[#Cluster Distances|differences between clusters]]*).
5. Repeat steps 3 and 4 until one cluster remains.

## Cluster Distances
As each cluster is a **set of points**, different definitions of distance between clusters will lead to different clustering behavior.

### Single-link
The <span style = "color:lightblue">single-link distance</span> is the minimum distance between any object in a cluster $C_1$ and any object in another cluster $C_2$ (i.e., the closest objects in both clusters).

$$dist_{single}(C_1,C_2)=\min_{x_1,x_2}\{dist(x_1,x_2)|x_1\in C_1,x_2\in C_2\}$$

It is reliant on a distance metric, such as [[#Similarity|Euclidean distance]], and results in long clusters.

![[ml-hierarchical-clustering-single-link.png|600]]

As it is a **single** link between two objects, it is sensitive to noise or slight changes.

### Complete-link
Contrary to the [[#Single-link|single-link distance]], the <span style = "color:lightblue">complete-link distance</span> is the maximum distance between any object in a cluster $C_1$ and any object in another cluster $C_2$ (i.e., the most dissimilar pair of objects).

$$dist_{complete}(C_1,C_2)=\max_{x_1,x_2}\{dist(x_1,x_2)|x_1\in C_1,x_2\in C_2\}$$

It tends to result in tight clusters. As it considers the maximum distance, it is problematic if the clusters are elongated (i.e., non-circular).

### Group Average
The <span style = "color:lightblue">group average distance</span> is the average distance between any object in $C_1$ and any object in $C_2$, where $N_1$ is the number of elements in $C_1$ and $N_2$ is the number of elements in $C_2$.

$$dist_{avg}(C_1,C_2)=\dfrac{1}{N_1\cdot N_2}\sum_{x_1\in C_1, x_2\in C_2}dist(x_1,x_2)$$

It considers <u>all</u> objects in both clusters.
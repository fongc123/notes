<span style = "color:lightblue">Morphological image processing</span> refers to the process of extracting image components for representation and description of region shape, such as boundaries, skeletons, and convex hulls. Applications include edge detection and blob detection.

Morphological image processing is based on [[#Set Theory|set theory]].

# Set Theory
It is the branch of mathematics that studies <span style = "color:lightblue">sets</span>, which are the collections of objects.

An object $a$ can be <span style = "color:lightblue">an element</span> of the set $A$.

$$
\begin{align}
	\text{in:}&\quad a\in A \\
	\text{not in:}&\quad a\notin A
\end{align}
$$

A <span style = "color:lightblue">null</span> or <span style = "color:lightblue">empty</span> set does not have any elements.

$$A=\emptyset$$

Alternatively, a set's contents can be specified with curly braces. For example, the following set $C$ contains elements that are formed by multiplying the elements $d$ of set $D$ by $-1$.

$$C=\{w|w=-d,\space\text{for}\space d\in D\}$$

If $A$ is a <span style = "color:lightblue">subset</span> of $B$, then every element of $A$ is also an element of $B$.

$$A\subset B$$

The <span style = "color:lightblue">union</span> of set $A$ and $B$ is the set of all elements belonging to **either** $A$ or $B$.

$$A\cup B$$

The <span style = "color:lightblue">intersection</span> of set $A$ and $B$ is the set of all elements belonging to **both** $A$ and $B$.

$$A\cap B$$

The set $A$ and $B$ are <span style = "color:lightblue">mutually exclusive</span> (i.e., disjoint) if their intersection is an **empty set**. There are no elements that belong to *both* sets $A$ and $B$.

$$A\cap B=\emptyset$$

The <span style = "color:lightblue">complement</span> of set $A$ is the set of elements that are not contained in set $A$.

$$A^C=\{w|w\notin A\}$$

The <span style = "color:lightblue">difference</span> of sets $A$ and $B$ is the set of elements that belong to $A$ and not contained in $B$.

$$A-B=\{w|w\in A,w\notin B\}=A\cap B^C$$

![[image-processing-set-complement-difference.png|600]]

The <span style = "color:lightblue">reflection</span> of set $A$ about its origin is the negation of all elements in $A$.

$$\hat{A}=\{w|w=-a,\space\text{for}\space a\in A\}$$

The <span style = "color:lightblue">translation</span> of set $A$ about its origin is the addition of a scalar to all elements in $A$.

$$(A)_z=\{c|c=a+z,\space\text{for}\space a\in A\}$$

Reflection and translation are used in morphological image processing.

# Binary Morphology
In <span style = "color:lightblue">binary morphology</span>, an image is viewed as a subset of Euclidean space $\mathbb{R}^d$ or the integer grid $\mathbb{Z}^d$ for some dimension $d$, where operations, such as <span style = "color:lightblue">erosion</span> and <span style = "color:lightblue">dilation</span>, can be performed.

Here, $A$ and $B$ are sets in $Z^2$, where $A$ represents the original foreground object and $B$ represents the <span style = "color:lightblue">structuring element (SE)</span>.

> [!INFO]
> The shape and size of the structuring element controls the manner and the extent of the [[#Erosion|erosion]] or the [[#Dilation|dilation]] of the foreground object.

> [!INFO]
> [[#Erosion]] and [[#Dilation|dilation]] are complementary to each other.
> 
> $$
> \begin{gather}
> (A\ominus B)^c=A^c \oplus \hat{B} \\\\
> (A \oplus B)^c=A^c \ominus \hat{B}
> \end{gather}
> $$

In real images, opening removes white noise with [[#Erosion|erosion]] and removes black noise with [[#Dilation|dilation]]. Closing fills gaps found in the object of interest (e.g., the image of a fingerprint).

## Erosion
The <span style = "color:lightblue">erosion</span> of $A$ by $B$ **shrinks objects** and **removes details smaller than the structuring element** (i.e., eroding the object $A$).

$$A\ominus B=\{z|(B)_z\subseteq A\}\space\text{or}\space A\ominus B=\{z|(B)_z \cap A^c=\emptyset\}$$

It is the set of all [[#Set Theory|displacements]] $z$ such that $B$, translated by $z$, is contained in $A$. An example is shown below.

![[image-processing-erosion.png|600]]

Intuitively, the structuring element is moved around the image, and a value is outputted only when all pixels in the structuring element's region are also part of the object.

## Dilation
The <span style = "color:lightblue">dilation</span> of $A$ by $B$ **expands or thickens objects** and **bridges gaps smaller than the structuring element**.

$$A\oplus B=\{z|(\hat{B})_z\cap A\neq\emptyset\}=\{z|\left[(\hat{B})_z\cap A\right]\subseteq A\}$$

It is the set of all [[#Set Theory|displacements]] $z$ such that $\hat{B}$ overlaps by <u>at least one</u> element of $A$.

> [!WARNING]
> Note that the reflection of $B$ (i.e., $\hat{B}$) is also performed. Generally, however, the structuring element will be symmetric.

An example is shown below.

![[image-processing-dilation.png|600]]

Intuitively, the structuring element is moved around the image, and a value is outputted only when at least one pixel in the structuring element's region is part of the object.

## Opening
The <span style = "color:lightblue">opening</span> of $A$ by $B$ is the [[#Erosion|erosion]] of $A$ by $B$ followed by the [[#Dilation|dilation]] of the **result** by $B$.

$$A\circ B=(A\ominus B)\oplus B$$

It **smooths the contours of an object** (i.e., smoothed outer corners), **breaks narrow bridges** (i.e., isthmus), and **eliminate thin protrusions**.

$$A\circ B=\bigcup\{(B)_z|(B)_z\subseteq A\}$$
It is the union of all translations of $B$ such that $B$ fits entirely in $A$. The resultant image is a sub-image of $A$.

![[image-processing-opening.png|600]]

> [!INFO]
> It smooths outer corners and eliminates thin protrusions and bridges as the structuring element $B$ cannot fit inside these structures.

## Closing
The <span style = "color:lightblue">closing</span> of $A$ by $B$ is the [[#Dilation|dilation]] of $A$ by $B$ followed by the [[#Erosion|erosion]] of the result by $B$.

$$A\cdot B=(A\oplus B)\ominus B$$

It **smooths the contours of an object** (i.e., smooths inner corners), fills **narrow breaks and gaps**, **eliminates long and thin gulfs** (i.e., long holes), and **eliminates small holes**.

$$A\cdot B=\left[\bigcup\{(B)_z|(B)_z\cap A=\emptyset\}\right]^c$$

It is the complement of the union of all translations of $B$ that do not overlap with $A$ (i.e., the structuring element $B$ is translated outside $A$). The resultant image is a superset of $A$.

![[image-processing-closing.png|600]]

> [!INFO]
> Both [[#Opening|opening]] and [[#Closing|closing]] have the convergence property. Repeated operations will have the same effect as one operation.
> 
> $$(A\circ B)\circ B=A\circ B$$


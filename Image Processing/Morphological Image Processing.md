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
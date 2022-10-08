<span style = "color:lightblue">Deep learning</span> is a subset of [[ML Basics|machine learning]] that uses <span style = "color:lightblue">artificial neural networks (ANN)</span> to make predictions by mimicking the process (*neuron interactions*) of the human brain. 

In <span style = "color:lightblue">feedforward neural networks</span>, connections between nodes (i.e., neurons) do not form a cycle (i.e., <span style = "color:lightblue">forward propagation</span> $\rightarrow$ later neurons do not connect back to earlier neurons).

Different nodes look for different **features** in the input data.
- Nodes can be added to account for more features, creating a <span style = "color:lightblue">layer</span> of neurons (*wider*).
- Layers can be added, where the previous layer will be the input to the new layer (*deeper*).

Each neural network layer is a feature transformation, where increasingly complex features are learned in consecutive layers.

![[ml-nn.png|400]]

# Mathematical Representation
Similar to [[Classification#Binary Classification|what was mentioned in classification]], each neuron can be represented by a <span style = "color:lightblue">sigmoid function</span> of inputs $x$, weights $w$, and biases $b$.

$$
\begin{align}
	\text{one neuron: }&\quad\sigma(w^Tx+b) \\
	\text{multiple neurons: }&\quad z_j=\sigma(w_J^Tx+b_j) \quad\text{for }j=1,2,
\end{align}
$$


<span style = "color:lightblue">
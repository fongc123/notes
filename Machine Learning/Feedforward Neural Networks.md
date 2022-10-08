<span style = "color:lightblue">Deep learning</span> is a subset of [[ML Basics|machine learning]] that uses <span style = "color:lightblue">artificial neural networks (ANN)</span> to make predictions by mimicking the process (*neuron interactions*) of the human brain. 

In <span style = "color:lightblue">feedforward neural networks</span>, connections between nodes (i.e., neurons) do not form a cycle (i.e., <span style = "color:lightblue">forward propagation</span> $\rightarrow$ later neurons do not connect back to earlier neurons).

Different nodes look for different **features** in the input data.
- Nodes can be added to account for more features, creating a <span style = "color:lightblue">layer</span> of neurons (*wider*).
- Layers can be added, where the previous layer will be the input to the new layer (*deeper*).

Each neural network layer is a feature transformation, where increasingly complex features are learned in deeper layers.

![[ml-nn.png|400]]

# Mathematical Representation
Similar to [[Classification#Binary Classification|what was mentioned in classification]], each neuron can be represented by a <span style = "color:lightblue">sigmoid function</span> (*alternative functions can be used*) of inputs $x$, weights $w$, and biases $b$.

$$\text{neuron: }\quad\sigma(w^Tx+b)$$

The output of a neuron is the input of the next neuron or layer. In the final layer of **binary classification**, the neuron will predict between two classes.

$$p(y=1|x)=\sigma(W^{(L)T}z^{(L-1)}+b^{(L)})$$

In the above equation, the subscript denotes the layer number, where $L$ represents the number of layers. In multi-class classification, however, the final layer will have multiple neurons to predict multiple classes.

> [!INFO]
> Linear regression and logistic regression (classification) are very similar. The only difference is that the final layer of regression won't be a sigmoid function (i.e., direct values will be predicted).


<span style = "color:lightblue">
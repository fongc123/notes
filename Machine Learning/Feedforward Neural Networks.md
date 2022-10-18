<span style = "color:lightblue">Deep learning</span> is a subset of [[ML Basics|machine learning]] that uses <span style = "color:lightblue">artificial neural networks (ANN)</span> to make predictions by simulating the process (*neuron interactions*) of the human brain. 

In <span style = "color:lightblue">feedforward neural networks</span>, connections between nodes (i.e., neurons) do not form a cycle (i.e., <span style = "color:lightblue">forward propagation</span> $\rightarrow$ later neurons do not connect back to earlier neurons).

Different nodes look for different **features** in the input data.
- Nodes can be added to account for more features, creating a <span style = "color:lightblue">layer</span> of neurons (*wider*).
- Layers can be added, where the previous layer will be the input to the new layer (*deeper*).

There are different types of nodes and layers (input, hidden, and output), and each additional neural network layer is a feature transformation, where increasingly complex features are learned in deeper layers.

![[ml-nn.png|400]]

<span style = "color:lightblue">Neural architecture search (NAS)</span> is a technique for automating the design of ANNs.

# Neuron
Similar to [[Classification#Binary Classification|what was mentioned in classification]], each neuron is represented by an [[#Activation Functions|activation function]] (e.g., the <span style = "color:lightblue">sigmoid function</span>) of inputs $x$, weights $w$, and biases $b$.

$$\text{neuron: }\quad\sigma(w^Tx+b)$$

The output of a neuron is the input of the next neuron.

> [!INFO]
> The nonlinearity of the activation function allows the model to make nonlinear predictions. Normally, <span style = "color:lightblue">feature engineering</span> (i.e., adding or combining features such as $X_1^2$, $\sin(X_1)$ or $X_1X_2$) is done, but it is not needed in deep learning.

> [!EXAMPLE]
> In binary classification, the neuron will predict only two classes (e.g., $y=1$ and $y\neq1$).
> $$\vphantom{\frac{0}{0}} p(y=1|x)=\sigma(W^{(L)T}z^{(L-1)}+b^{(L)})$$
> The equation above represents the equation the **neuron in the final output layer**, where the superscript $L$ represents the total number of layers (i.e., the final layer).

> [!INFO]
> Linear regression and logistic regression (classification) are very similar. The only difference is that the final layer of regression won't be a sigmoid function (i.e., direct values will be predicted).

# Perceptron
A <span style = "color:lightblue">perceptron</span> is a feedforward neural network with only <u>one</u> layer of adjustable weights. Here, there are no **hidden layers**, as the inputs connect directly to the output. It is the simplest neural network.

![[ml-perceptron.png|600]]

With the step function as its 

# Activation Functions

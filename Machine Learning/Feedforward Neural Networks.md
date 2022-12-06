<span style = "color:lightblue">Deep learning</span> is a subset of [[ML Basics|machine learning]] that uses <span style = "color:lightblue">artificial neural networks (ANN)</span> to make predictions by simulating the process (*neuron interactions*) of the human brain. 

In <span style = "color:lightblue">feedforward neural networks</span>, connections between nodes (i.e., neurons) do not form a cycle (i.e., <span style = "color:lightblue">forward propagation</span> $\rightarrow$ later neurons do not connect back to earlier neurons); however, most neural network architectures are feedforward.

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
A <span style = "color:lightblue">perceptron</span> is a feedforward neural network with only <u>one</u> layer of adjustable weights. Here, there are no **hidden layers**, as the inputs connect directly to the output. It is the simplest type of neural network.

![[ml-perceptron.png|600]]

With the [[#Step Function|step function]] as its activation function, basic Boolean functions can be represented.

> [!INFO]
> The ability to represent basic Boolean functions (e.g., `AND`, `OR`, `NOT`) is favored, as *any* Boolean function can be represented with more layers of sufficiently many perceptrons (i.e.,  <span style = "color:lightblue">multi-layer perceptrons</span>).

However, due to its simplicity, only functions that are **linearly separable** can be represented.

![[ml-linear-separable.png|600]]

# Activation Functions
<span style = "color:lightblue">Activation functions</span> are additionally inserted in between neuron connections.

## Step Function
The <span style = "color:lightblue">step function</span> is an **abrupt** change from $0$ to $1$ when $x=0$.

$$
\begin{gather}
	O=\text{step}\left(\sum_{j=1}^{n}w_jI_j-\theta\right),\text{ where} \\
	\text{step}(x)=\begin{dcases}
		0 \vphantom{frac{0}{0}} & \text{if }x<0 \\
		1 \vphantom{frac{0}{0}} & \text{if }x\geq0
	\end{dcases}
\end{gather}
$$
This activation function is not commonly used as it cannot be differentiated.

## Sigmoid
The <span style = "color:lightblue">sigmoid function</span> is a smoothed and differentiable variant of the [[#Step Function|step function]].

$$\sigma(x)=\frac{1}{1+\exp(-x)}$$

It mimics the biological process of the neuron, as output values are mapped between $0$ and $1$. However, its output is centered around $0.5$. This is undesirable, as outputs centered around $0$ are preferred.

> [!INFO]
> The sigmoid activation function is still useful for the output of a binary classification model (i.e., probability between two outcomes). The activation functions of the hidden layers should be changed to some other function (e.g., [[#Softmax]]).

## Hyperbolic Tangent
The <span style = "color:lightblue">hyperbolic tangent (tanh)</span> creates the same shape as the [[#Sigmoid|sigmoid function]], but ranges from $-1$ and $1$.

$$\tanh(a)=\frac{\exp{(2a)}-1}{\exp{(2a)}+1}$$

Both the **hyperbolic tangent** and **sigmoid** activation functions suffer from the <span style = "color:lightblue">vanishing gradient problem</span>, as the gradients of their outputs are small. When multiplied together in each layer, the gradients become even smaller. Thus, layers close to the inputs were trained very slowly, preventing earlier neural networks from having many layers.

## ReLU
The <span style = "color:lightblue">rectified linear unit (ReLU)</span> is the most popular activation function for deep neural networks due to its **efficient computation** (*no exponential functions*) and **simple gradient**.
- if $x>0$, gradient is $1$
- if $x\leq 0$, gradient is $0$ (creates <span style = "color:lightblue">dead neurons</span>)

$$f(x)=\max(0,x)$$

Alternatively, the <span style = "color:lightblue">leaky rectified linear unit (LReLU)</span> accounts for the zero gradient found for inputs less than $0$, where those values now have a small slope instead of a flat slope. Other alternatives include the <span style = "color:lightblue">exponential linear unit (ELU)</span>.

## Softplus
The <span style = "color:lightblue">Softplus activation function</span> is similar to the [[#ReLU]] activation function but is differentiable at the origin.

$$\zeta(x)=\frac{1}{\beta}\log(1+\exp(\beta \cdot x)$$

The combination of logarithmic and exponential functions approximate a line for large values.

## Bionodal Root Unit
The <span style = "color:lightblue">bionodal root unit</span> improves upon the [[#ReLU]] activation function by taking inspiration from the action potential of a biological neuron.

$$f(z)=\begin{dcases}
	(r^2z+1)^\frac{1}{r}-\frac{1}{r} \vphantom{\frac{0}{0}} &\text{if}\space z\geq0 \\
	\exp{(rz)}-\frac{1}{r} \vphantom{\frac{0}{0}} & \text{if}\space z<0
\end{dcases}
$$

The paper can be found [here](https://arxiv.org/abs/1804.11237).

## Softmax
The <span style = "color:lightblue">Softmax activation function</span> maps inputs between $0$ and $1$, where the sum of $K$ possible outputs is equal to $1$.

$$\text{Softmax}(z)_i=\dfrac{\exp{(z_i)}}{\sum_{j=1}^{K}{\exp{(z_j)}}}$$

It is *technically* an activation function, but it is not meant for hidden layers. Instead, it is used as the output of a model (e.g., **probabilities** of classes in <span style = "color:lightblue">multi-class classification</span>).

> [!INFO]
> In PyTorch, the `nn.CrossEntropyLoss()` class already incorporates the Softmax activation function, regardless of whether the model is intended for binary classification or multi-class classification.
> 
> Alternatively, `nn.NLLLoss()` is the standalone cross entropy loss.

# Computational Graph
A <span style = "color:lightblue">computational graph</span> is a form of directed graph that represents a mathematical equation. In machine learning, it is used to represent the mathematical expressions in a neural network.

![[ml-comp-graph.png|600]]

Used in many machine learning models, such as [[Classification|classification]] and [[Regression|regression]], <span style = "color:lightblue">backpropagation</span> calculates gradients so that the weights and biases of the model can be updated accordingly. Essentially, backpropagation is the chain rule from calculus.
- **Addition:** input gradients equal upstream gradient (i.e., <span style = "color:lightblue">gradient distributor</span> or **add gate**)
- **Multiplication:** input gradients equal the **product** of the <u>other</u> input's local gradient *and* the upstream gradient (i.e., <span style = "color:lightblue">gradient switcher</span> or **mul gate**)
- **Max:** input gradient with the maximum value equal upstream gradient and (i.e., <span style = "color:lightblue">gradient router</span> or **max gate**) ($0$ for other inputs)

> [!INFO]
> Gradients add at branches.
> 
> ![[ml-comp-grad-branches.png|450]]

A [[#Sigmoid|sigmoid gate]] can be implemented as follows.

![[ml-comp-sigmoid.png|600]]

The derivatives of each gate are calculated.

$$
\begin{align}
f(x)=\frac{1}{x}&\rightarrow\frac{df}{dx}=-\frac{1}{x^2} \\\\
f(x)=e^x&\rightarrow\frac{df}{dx}=e^x\\\\
f(x)=x+c&\rightarrow\frac{df}{dx}=1\\\\
f(x)=ax&\rightarrow\frac{df}{dx}=a
\end{align}
$$

To calculate the gradient of the $\frac{1}{x}$ gate, the local gradient is multiplied (i.e., $\frac{df}{dx}=-\frac{1}{x^2}$) by the upstream gradient.

$$(-\frac{1}{1.37^2})(1.00)=-0.53$$

To calculate the gradient of the $\exp$ gate, the local gradient (i.e., $\frac{df}{dx}=e^x$) is multiplied by the upstream gradient.

$$(e^{-1})(-0.53)=-0.20$$

![[ml-comp-sigmoid-ans.png|600]]

## Example
In the above computational graph, we want to obtain the input gradients (i.e., $\frac{\partial f}{\partial x}$, $\frac{\partial f}{\partial y}$, and $\frac{\partial f}{\partial z}$) with respect to the output $f$. From the graph, we know the following.

$$
\begin{align}
q=x+y\quad\frac{\partial q}{\partial x}=1,\frac{\partial q}{\partial y}=1 \\
f=qz\quad\frac{\partial f}{\partial q}=z,\frac{\partial f}{\partial z}=q
\end{align}
$$

We can easily obtain $\frac{\partial f}{\partial z}$, as it is the value of $q$ ($-4\times1$). To obtain the gradients of $x$ and $y$, we use the chain rule.

$$
\begin{gather}
\frac{\partial f}{\partial x}=\frac{\partial f}{\partial q}\frac{\partial q}{\partial x}=z=-4 \\
\frac{\partial f}{\partial y}=\frac{\partial f}{\partial q}\frac{\partial q}{\partial y}=z=-4
\end{gather}
$$

![[ml-comp-graph-ans.png|600]]

Thus, the gradients are **propagated back** to the inputs.

# Code
A sample **artificial neural network** is constructed with PyTorch's `Sequential` object that is composed of multiple layers (*see [[PyTorch & CUDA Setup#Modular Programming|modules in PyTorch]]*).

```python
import torch.nn as nn

model = nn.Sequential(
	nn.Linear(784, 128),  # linear layer with 784 inputs (e.g. MNIST dataset)
	nn.ReLU(),
	nn.Linear(128, 10)    # 10 output classes
)
```

Alternatively, a custom model of the above `Sequential` module can be customized and implemented manually with [[Classes|object-oriented programming (OOP)]].

```python
class ANN(nn.Module):
	def __init__(self):
		super(ANN, self).__init__()
		self.layer1 = Linear(784, 128)
		self.layer2 = ReLU()
		self.layer3 = Linear(128, 10)
	def forward(self, x):
		x = self.layer1(x)
		x = self.layer2(x)
		x = self.layer3(x)

		return x

# initialize the model
model = ANN()
```
- The class inherits the `nn.Module` class (i.e., the class is a PyTorch module).
- The layers are defined in the constructor method.
- The `forward` method applies the layers to an input `x`.


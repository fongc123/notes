# Regression

A linear regression model (a <span style = "color:lightblue">regressor</span>) is based on a simple linear equation.

$$\hat{y}=mx+b$$
> [!INFO]
> The $\hat{y}$ denotes a prediction. A $y$ variable without the symbol would refer to the true value or target which is not applicable in this context.

Predictions are made by inputting a value in $x$ and obtaining and output in $y$.

## Mean Squared Error
Given a dataset consisting of $x$ and $y$ values, a <span style = "color:lightblue">loss function</span> determines how well certain $m$ and $b$ values fit an equation to the dataset.

The <span style = "color:lightblue">mean squared error (MSE)</span> is the average of the squared difference between individual data points and the fitted line.

$$
\begin{align}
	MSE & =\frac{1}{N}\sum_{i=1}^{N}(y_i-\hat{y}_i)^2 \\
	MSE & = \frac{1}{N}\sum_{i=1}^{N}[y_i-(mx_i+b)]^2
\end{align}
$$

A poorly fit equation has a **larger error**, while a well-fit equation has a **smaller error**. A perfectly fit equation (*rare*) has an error value of zero.

The goal is to find values of $m$ and $b$ to minimize the loss of the mean squared error ($L$ for loss). Mathematically, this can be achieved by finding the derivative(s) of the loss function and equating it to zero, so that the parameter(s) can be obtained.
$$
\begin{align}
	\frac{\partial L}{\partial m}=0;\space \frac{\partial L}{\partial b}=0
\end{align}
$$

> [!INFO]
> The method of finding derivatives and equating them to zero *only* works for a linear regression problem (*see [[#Gradient Descent]]*).

## Gradient Descent
<span style = "color:lightblue">Gradient descent</span> is an **iterative** first-order optimization **algorithm** that is used to find the local minimum or maximum or a function. Each iteration of the descent is referred to as an <span style = "color:lightblue">epoch</span>.
1. Initial parameters start at a randomly initialized point.
2. Find the gradient of the loss with respect to current parameters.
3. Step in gradient direction to obtain new parameters (i.e., the `optimizer.step()` method).
4. Iterate until minimum is reached.

> [!INFO]
> Most of the time, it is impossible to solve for the gradient of the loss function analytically.

When there are multiple features, this method finds the feature(s) that has the most effect on the loss function and adjusts accordingly.

## Code Template
A code template for creating a linear regression model is shown below. Although there may be a few adjustments, the template is applicable to other machine learning problems as well.

```python
import torch
import torch.nn as nn
import numpy as np

# create the linear regression model
model = nn.Linear(1, 1) # arguments: no. of input, no. of output

# define a loss and an optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr = 0.1)

# convert data to tensor
X = X.reshape(N, 1)
Y = Y.reshape(N, 1)

# convert type so that PyTorch can read
inputs = torch.from_numpy(X.astype(np.float32))
targets = torch.from_numpy(Y.astype(np.float32))

# iterate through epochs to train the model
losses = []
num_epochs = 30
for it in range(num_epochs):
	# zero the parameter gradients
	optimizer.zero_grad()

	# forward pass
	outputs = model(inputs)
	loss = criterion(outputs, targets)

	# keep losses so that it can be plotted later
	losses.append(loss.item())

	# backward and optimize
	loss.backward()  # calculate gradient
	optimizer.step() # gradient descent step
```

An <span style = "color:lightblue">epoch</span> (i.e., an iteration) is one complete pass of the training dataset through the algorithm.

Internally, PyTorch accumulates gradients in each epoch. Thus, the parameter gradients must be set to zero before starting the next epoch with `optimizer.zero_grad()`.

The <span style = "color:lightblue">learning rate</span> is the step size at each iteration while moving towards a minimum in a loss function. A small learning rate requires many iterations before reaching the minimum point, while a large learning rate swiftly reaches it. Too large of a learning rate causes drastic updates, which lead to divergent behavior.

> [!INFO]
> The learning rate is modified by powers of $10$ (e.g., $0.1$, $0.01$, $0.001$, etc.).

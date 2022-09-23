# Introduction

<span style = "color:lightblue">Machine learning</span> is a geometry problem. Given a dataset, a curve is fitted to best describe the data; however, the meaning of the curve changes according to the problem and data.
- <span style = "color:lightblue">classification</span>: the curve separates data points into **classes**
- <span style = "color:lightblue">regression</span>: the curve estimates the trend of data points as close as possible

The simplest curve-fitting is linear, where there are only two variables and a line is drawn based on their data. For a more advanced model, additional <span style = "color:lightblue">features</span> (i.e., variables) can be included or the possibility of nonlinearity can be considered.

While each <span style = "color:lightblue">machine learning model</span> is trained on different data, the task is still the same and can be applied to other datasets (i.e., *all data is the same*).

$$build\rightarrow train \rightarrow predict$$

## Regression
A linear regression model (a <span style = "color:lightblue">regressor</span>) is based on a simple linear equation.

$$\hat{y}=mx+b$$
> [!INFO]
> The $\hat{y}$ denotes a prediction. A $y$ variable without the symbol would refer to the true value or target which is not applicable in this context.

Predictions are made by inputting a value in $x$ and obtaining and output in $y$.

### Loss Function
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

### Gradient Descent
<span style = "color:lightblue">Gradient descent</span> is an **iterative** first-order optimization **algorithm** that is used to find the local minimum or maximum or a function. Each iteration of the descent is referred to as an <span style = "color:lightblue">epoch</span>.

When there are multiple features, this method finds the feature(s) that has the most effect on the loss function and adjusts accordingly.

### Code Template
Several lines of code related to creating a linear regression model are shown below. Although there may be a few adjustments, the template is applicable to other machine learning problems as well.

## Classification

A classification model (a <span style = "color:lightblue">classifier</span>) takes as input <span style = "color:lightblue">non-class attribute values</span> and returns a <span style = "color:lightblue">class value</span>. Several classification algorithms include **decision tree**, **rule-based**, **Bayesian**, **neural networks**, **support vector machines (SVM)**, and ***k*-nearest neighbors (KNN)**.

A <span style = "color:lightblue">confusion matrix</span> is a tool to analyze how well a classifier can recognize tuples of different classes.

Alternatively, other accuracy measures include sensitivity and specificity. <span style = "color:lightblue">Precision</span> is the fraction of correctly predicted classes (true positives; retrieved and relevant documents) out of all data points (true positives and false positives; all documents).

$$\text{precision}=\frac{\text{TP}}{\text{TP}+\text{FP}}$$

<span style = "color:lightblue">Recall</span> is the fraction of correctly predicted classes (true positives) out of all <u>class</u> data points (true positives and false negatives; all <u>relevant</u> documents).

$$\text{recall}=\frac{\text{TP}}{\text{TP}+\text{FN}}$$

An ideal system maximizes both precision and recall values; however, there is a trade-off between precision and recall. To increase precision, a small number of data points is predicted to increase the chance of a correct classification. To increase recall, a large number of data points is predicted to increase the number of class-specific data points evaluated.

The <span style = "color:lightblue">F-measure</span> is the harmonic mean which can be calculated with precision and recall values.

$$\text{F-measure}=\frac{2\times \text{recall}\times\text{precision}}{\text{recall}+\text{precision}}$$

For a general accuracy indicator, the <span style = "color:lightblue">accuracy</span> can be calculated as shown below.

$$\text{accuracy}=\frac{\text{TP}+\text{TN}}{\text{TP}+\text{TN}+\text{FP}+\text{FN}}$$


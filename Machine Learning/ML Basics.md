# Machine Learning Basics

<span style = "color:lightblue">Machine learning</span> is a geometry problem. Given a dataset, a curve is fitted to best describe the data; however, the meaning of the curve changes according to the problem and data.
- <span style = "color:lightblue">classification</span>: the curve separates data points into **classes**
- <span style = "color:lightblue">regression</span>: the curve estimates the trend of data points as close as possible

The simplest curve-fitting is linear, where there are only two variables and a line is drawn based on their data. For a more advanced model, additional <span style = "color:lightblue">features</span> (i.e., variables) can be included or the possibility of nonlinearity can be considered.

While each <span style = "color:lightblue">machine learning model</span> is trained on different data, the task is still the same and can be applied to other datasets (i.e., *all data is the same*).

$$build\rightarrow train \rightarrow predict$$

Most machine learning algorithms are **greedy**. A <span style = "color:lightblue">greedy algorithm</span> makes the locally optimal choice at each stage, but it does not consider a globally optimal solution. However, a greedy heuristic can yield locally optimal solutions that approximate a globally optimal solution in a reasonable amount of time.

## Over-fitting
An <span style = "color:lightblue">over-fitted</span> model is **more complex** than an original model, where the over-fitted model will fit noisy data better than an original model.

Special anomalies may have been incorporated into the model. This affects the accuracy of the model on the test set.

Over-fitting prevention methods of various approaches are listed below.
- [[Decision Tree#Over-fitting|decision trees]]

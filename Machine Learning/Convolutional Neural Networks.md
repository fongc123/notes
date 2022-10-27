<span style = "color:lightblue">Convolutional neural networks</span> are commonly used in image classification and object recognition. This type of neural network automatically *learns* image kernels to achieve tasks (*see [[Spatial Filtering|convolution and filtering]]*).

Due to the **small convolution kernel**, convolutional neural networks have a local <span style = "color:lightblue">receptive field</span>, as layers are only connected to a <u>local</u> subset of units in the previous layer.

![[ml-cnn-receptive-field.png|600]]

More input pixels and, thus, more complex features are learned as the receptive field grows (i.e., propagate into deeper layers).

> [!INFO]
> Conventional multilayer [[Feedforward Neural Networks#Perceptron|perceptrons]] (MLP) are **fully connected**. Thus, there are many weights to learn, and an abundance of data is needed.

Additionally, the same spatial parameters are shared across all spatial locations. This **allows features to be detected regardless of position** and **reduces the number of free parameters to learn**.

![[ml-cnn-shared-parameters.png|600]]


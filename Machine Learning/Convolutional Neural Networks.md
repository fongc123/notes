<span style = "color:lightblue">Convolutional neural networks</span> are commonly used in image classification and object recognition. This type of neural network automatically *learns* image kernels to achieve tasks (*see [[Spatial Filtering|convolution and filtering]]*).

Convolutional neural networks have specific design features that are suited for images.
1. **Local receptive field**: layers are only connected to a <u>local</u> subset of units in the previous layer (i.e., not fully connected)
2. **Shared spatial parameters**: weights of the same color (e.g., red, green, blue) are shared

![[ml-cnn-receptive-field.png|600]]

Despite a local receptive field, more complex features of the <u>entire</u> image are learned as the receptive field grows (i.e., propagate into deeper layers).

> [!INFO]
> Conventional multilayer [[Feedforward Neural Networks#Perceptron|perceptrons]] (MLP) are **fully connected**. Thus, there are many weights to learn, and an abundance of data is needed.

![[ml-cnn-shared-parameters.png|600]]

Sharing parameters **allows features to be detected regardless of position** and **reduces the number of free parameters to learn**.


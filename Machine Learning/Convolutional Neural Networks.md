<span style = "color:lightblue">Convolutional neural networks</span> are commonly used in image classification and object recognition. This type of neural network automatically *learns* image kernels to achieve tasks (*see [[Spatial Filtering|convolution and filtering]]*).

The components of a convolutional neural network, which normally consist of [[#Convolutional Layer|convolutional layers]] and [[#Pooling Layer|pooling layers]], are shown below.

![[ml-cnn-components.png|600]]

An example classification architecture for classifying a $256\times256\times3$ colored image to one of $1000$ classes is shown below.

![[ml-cnn-example.png|600]]

Here, there are two convolutional layers (each with $64$ feature maps) with ReLU and two pooling layers (stride 4). Lastly, the resulting matrix is reshaped into a vector of size $16384$ and converted into $1000$ classes with the [[Feedforward Neural Networks#Activation Functions#Softmax|softmax]] function.

# Design

Convolutional neural networks have specific design features that are suited for images.
1. **Local receptive field**: layers are only connected to a <u>local</u> subset of units in the previous layer (i.e., not fully connected)
2. **Shared spatial parameters**: weights of the same color (e.g., red, green, blue) are shared

![[ml-cnn-receptive-field.png|600]]

Despite a local receptive field, more complex features of the <u>entire</u> image are learned as the receptive field grows (i.e., propagate into deeper layers).

> [!INFO]
> Conventional multilayer [[Feedforward Neural Networks#Perceptron|perceptrons]] (MLP) are **fully connected**. Thus, there are many weights to learn, and an abundance of data is needed.

![[ml-cnn-shared-parameters.png|600]]

Sharing parameters **allows features to be detected regardless of position** and **reduces the number of free parameters to learn**.

The table below shows the efficiency of convolution, where the input size is $320\times280$, the kernel size is $2\times1$, and the output size is $319\times280$.

|   **Type**    | **Convolution** |            **Dense Matrix**            |      **Sparse Matrix**       |
|:-------------:|:---------------:|:--------------------------------------:|:----------------------------:|
| No. of values |       $2$       | $319\times280\times320\times280 > 8e9$ | $2\times319\times280=178640$ |

# Convolutional Layer
Multiple <span style = "color:lightblue">feature maps</span> (i.e., kernel or filter) look at the same region of input. They perform **convolution** to obtain features from the input.
- <span style = "color:lightblue">maps</span>: number of feature extractors
- <span style = "color:lightblue">pool size</span>: distance between each set of feature maps
- <span style = "color:lightblue">RF size</span>: size of kernel (i.e., region of input to look at)

![[ml-cnn-conv-layer.png|600]]

The resultant feature maps are stacked in the depth dimension. For example, an input image with size $256\times256\times3$ may output a size of $256\times256\times64$ for $64$ feature extractors.

Since convolution (i.e., moving the kernel around the image) shrinks the output, [[Spatial Filtering#Zero-padding|zero-padding]] is done to preserve the original size of the input. Zeros are added at each layer.

## Activation Function
Since convolution is a linear operation, the inclusion of [[Feedforward Neural Networks#Activation Functions|activation functions]] (e.g., ReLU) after a convolution layer is needed to add nonlinearity.

> [!INFO]
> Two convolution layers would be no more powerful than a single convolution layer.

# Pooling Layer
A <span style = "color:lightblue">pooling layer</span> **reduces the representation size** (*less computation*) and **provides spatial invariance**. Once features are detected, only an <u>approximate</u> location is needed.

The input to the next layer is the result of an operation of each sub-region in the previous layer. <span style = "color:lightblue">Max-pooling</span> outputs the **maximum** value in the sub-region to the next layer.

![[ml-cnn-pool-layer.png|600]]

Other pooling methods include <span style = "color:lightblue">average pooling</span> and <span style = "color:lightblue">global pooling</span>. Pooling accounts for spatial variance of features in the image, as the output will not be significantly affected by changes in pixel values.

<span style = "color:lightblue">Stride</span> is the down sampling factor. For example, a stride of $2$ means that the dimensions $W\times H$ will be sampled by a factor of two to $0.5W\times0.5H$. The filter size (e.g., $2\times2$) also determines the sampling factor.

## 
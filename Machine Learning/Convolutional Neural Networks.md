<span style = "color:lightblue">Convolutional neural networks</span> are commonly used in [[Image Classification|image classification]] and object recognition. This type of neural network automatically *learns* image kernels to achieve tasks (*see [[Spatial Filtering|convolution and filtering]]*).

A convolutional neural network normally consists of (1) a series of [[#Convolutional Layer|convolutional layers]] and [[#Pooling Layer|pooling layers]] (*feature extraction*) and (2) one or a few fully-connected or dense layers (*classification or regression*).

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

Sharing parameters **allows features to be detected regardless of position** and **reduces the number of free parameters to learn**. Reducing computational cost allows features to be extracted from <u>multiple locations</u> in the image, which would not be possible in a dense network.

The table below shows the efficiency of convolution, where the input size is $320\times280$, the kernel size is $2\times1$, and the output size is $319\times280$.

|   **Type**    | **Convolution** |            **Dense Matrix**            |      **Sparse Matrix**       |
|:-------------:|:---------------:|:--------------------------------------:|:----------------------------:|
| No. of values |       $2$       | $319\times280\times320\times280 > 8e9$ | $2\times319\times280=178640$ |

# Convolutional Layer
Multiple <span style = "color:lightblue">feature maps</span> (i.e., kernel or filter) look at the same region of input. They perform **convolution** to obtain features from the input.
- <span style = "color:lightblue">maps</span>: number of feature extractors
- <span style = "color:lightblue">pool size</span>: distance between each set of feature maps
- <span style = "color:lightblue">RF size</span>: size of kernel (i.e., region of input to look at)

The neuron equation from [[Feedforward Neural Networks#Neuron|typical]] neural networks is also used in convolutional neural networks.

![[ml-cnn-conv-layer.png|600]]

The resultant feature maps are stacked in the depth dimension. For example, an input image with size $256\times256\times3$ may output a size of $256\times256\times64$ for $64$ feature extractors.

> [!INFO]
> As the output of convolution between a three-dimensional input (e.g., a colored image) and a three-dimensional kernel is still a two-dimensional object (i.e., $H\times W\times 3$), the feature maps are stacked to create the third dimension in the output (i.e., $H\times W\times \text{features}$).

Since convolution (i.e., moving the kernel around the image) shrinks the output, [[Spatial Filtering#Zero-padding|zero-padding]] is done to preserve the original size of the input. Zeros are added at each layer.

## Activation Function
Since convolution is a linear operation, the inclusion of [[Feedforward Neural Networks#Activation Functions|activation functions]] (e.g., ReLU) after a convolution layer is needed to add nonlinearity.

> [!INFO]
> Two convolution layers would be no more powerful than a single convolution layer.

## Convolutional Arithmetic
Given input parameters, the output size after a convolution operation can be calculated.
- <span style = "color:lightblue">kernel size</span>: size of the kernel (e.g., $3\times3$)
- <span style = "color:lightblue">padding</span>: zero padding of input
	- `valid`: no padding (*output shrinks*)
	- `same`: padding to ensure input and output have the same size
- <span style = "color:lightblue">stride</span>: down sampling factor (*see [[#Pooling Layer|pooling layers]]*)
- <span style = "color:lightblue">dilation</span>: spacing between kernel points

The formula for calculating the output shape can be found in the [PyTorch documentation](https://pytorch.org/docs/stable/generated/torch.nn.Conv2d.html), where $H$ represents the height, $W$ represents the width, $C$ represents the color, and $N$ represents the number of samples.

$$
\begin{gather}
	H_{out} = \left\lfloor\dfrac{H_{in}+2\times\text{padding}[0]-\text{dilation}[0]\times(\text{kernel\_size}[0]-1)-1}{\text{stride}[0]} + 1\right\rfloor\\\\
	W_{out} = \left\lfloor\dfrac{W_{in}+2\times\text{padding}[1]-\text{dilation}[1]\times(\text{kernel\_size}[1] -1)-1}{\text{stride}[1]} + 1\right\rfloor
\end{gather}
$$

The $\lfloor$ and $\rfloor$ symbols denote the floor operation.

> [!INFO]
> In PyTorch, an error is raised when the input and output sizes don't match. In Keras, the size is automatically inferred.

> [!WARNING]
> The PyTorch convention for arranging image dimensions is different, where the color channel is presented first.
> $$\underbracket{(N, C_{in}, H_{in}, W_{in})}_{\text{input}}\rightarrow\underbracket{(N,C_{out}, H_{out}, W_{out})}_{\text{output}}$$
> Other Python libraries, such as OpenCV, Tensorflow, Matplotlib, and Pillow, present the color channels last.
> $$N\times H\times W\times C$$
> This can be demonstrated by comparing the shape of an element from `dataset.data` with that of from a data loader.

### Example
In this [[#Code|example]], there are **three** convolutional layers, where the input size is $28\times28\times3$, the padding is $0$, the dilation is $1$, the kernel size is $3\times3$, and the stride is $2$. First, the shape of the output after the first convolution is calculated.

$$H_{1,out},W_{1,out}=\left\lfloor\dfrac{28+2\times0-1\times(3-1)-1}{2}+1\right\rfloor=13$$

The height and width after the first convolution are equal. Next, the shapes of the second and third convolutions are calculated.

$$
\begin{gather}
H_{2,out},W_{2,out}=\left\lfloor\dfrac{13+2\times0-1\times(3-1)-1}{2}+1\right\rfloor=6 \\\\
H_{3,out},W_{3,out}=\left\lfloor\dfrac{6+2\times0-1\times(3-1)-1}{2}+1\right\rfloor=2
\end{gather}
$$

Thus, the output after the three convolutional layers is $2\times2$.

# Pooling Layer
A <span style = "color:lightblue">pooling layer</span> **reduces the representation size** (*less computation*) and **provides spatial invariance**. Once features are detected, only an <u>approximate</u> location is needed.

The input to the next layer is the result of an operation of each sub-region in the previous layer. <span style = "color:lightblue">Max-pooling</span> outputs the **maximum** value in the sub-region to the next layer.

![[ml-cnn-pool-layer.png|600]]

> [!INFO]
> As the kernel size is constant and pooling layers shrink the input, increasingly larger patterns are found, allowing for more complex shapes to be recognized.

Other pooling methods include <span style = "color:lightblue">average pooling</span> and <span style = "color:lightblue">global pooling</span> (*both max and average*). Pooling accounts for spatial variance of features in the image, as the output will not be significantly affected by changes in pixel values.

<span style = "color:lightblue">Stride</span> is the down sampling factor (i.e., the step size between kernel placements when moving the kernel around). For example, a stride of $2$ means that the dimensions $W\times H$ will be sampled by a factor of two to $0.5W\times0.5H$. The filter size (e.g., $2\times2$) determines the size of the sub-region and will also affect the down sampling.

# Hyperparameters
Like [[ML Basics#Choosing Hyperparameters|other neural networks]], hyperparameters have to be carefully selected. For convolutional neural networks, however, there are standard conventions.
- Filter size is relative to image (e.g., $3\times3$, $5\times5$, or $7\times7$).
- A series of convolutional layers followed by pooling layers are repeated.
- Number of feature maps are increased (e.g., $32\rightarrow64\rightarrow128$)

# Code
Similar to building [[Feedforward Neural Networks#Code|ANNs]], a custom convolutional neural network is implemented with PyTorch.

```python
import torch.nn as nn

class CNN(nn.Module):
	def __init__(self, K):
		super(CNN, self).__init__()

		# define the convolution layers
		self.conv = nn.Sequential(
			nn.Conv2d(1, 32, kernel_size = 3, stride = 2), # input: 2, output: 32
			nn.ReLU(),
			nn.Conv2d(32, 64, kernel_size = 3, stride = 2),
			nn.ReLU(),
			nn.Conv2d(64, 128, kernel_size = 3, stride = 2),
			nn.ReLU()
		)

		# define the fully-connected linear layers
		self.dense = nn.Sequential(
			# calculate output of convolution
			nn.Linear(128 * 2 * 2, 512), # no. of channels * width * height
			nn.ReLU(),
			nn.Linear(512, K)
		)

	def forward(self, X):
		out = self.conv(X)
		out = out.view(out.size(0), -1)
		out = self.dense(out)

		return out
```

The `Conv2d` module is used for convolution.
- `in_channels`: number of **input channels** ($1$ and $3$ for grayscale and images respectively)
- `out_channels`: number of **output channels** produced by convolution
- `kernel_size`: size of the kernel
- `stride`: stride

> [!INFO]
> <span style = "color:lightblue">Dropout regularization</span> can be performed to drop out random nodes in the input based on a probability $p$. This prevents the model on relying on certain inputs too much.
> ```python
> nn.Dropout(p = 0.2)
> ```

It is important to calculate the input and output sizes (*see [[#Convolutional Arithmetic|convolutional arithmetic]]*). Equivalently, a convolutional neural network can be implemented with the `Sequential` module.

```python
model = nn.Sequential(
	nn.Conv2d(3, 32, kernel_size = 3, stride = 2),
	nn.ReLU(),
	nn.Conv2d(32, 64, kernel_size = 3, stride = 2),
	nn.ReLU(),
	nn.Conv2d(64, 128, kernel_size = 3, stride = 2),
	nn.ReLU(),
	nn.Flatten(),
	nn.Linear(128 * 2 * 2, 512), # no. of channels * width * height
	nn.ReLU(),
	nn.Linear(512, K)
)
```

The `Flatten` module substitutes the `view` method.

Next, training the model is the same as any [[Regression#Code Template|other]] machine learning model.

> [!INFO]
> The `model.train()` line should be added before training is done, while the `model.eval()` line should be added before evaluation is done.
> 
> Some layers, such as `Dropout` and `BatchNorm`, behave differently under different [modes](https://stackoverflow.com/questions/51433378/what-does-model-train-do-in-pytorch).


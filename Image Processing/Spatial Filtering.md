# Spatial Filtering

<span style = "color:lightblue">Spatial filtering</span> modifies an image by replacing each pixel value with the output from a function that relies on the value of the pixel and the values of the neighboring pixels.



## Highpass Filters

<span style = "color:lightblue">Highpass filters</span> create sharpening in an image, where intensity transitions and details are highlighted. This filter **allows high frequencies and restricts low frequencies.** 

A highpass filter is achieved using <span style = "color:lightblue">differentiation</span>.

### First Derivative

A first-derivative filter can be used for edge enhancement.

### Second Derivative

The <span style = "color:lightblue">Laplacian operator</span> is the simplest second-order isotropic derivative operator.

$$\nabla^2f=\frac{\partial^2f}{\partial x^2}+\frac{\partial^2f}{\partial y^2}$$

Some Laplacian kernels are shown below.


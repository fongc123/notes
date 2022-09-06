# Acquisition & Representation

## Human Visual System
A <span style = "color:lightblue">human visual system</span> consists of the eyes which are responsible for creating sensory signals and the central nervous system which is responsible for processing the sensory signals.

### The Eye
To perform its functions, the human eye consists of several important structures.
- <span style = "color:lightblue">cornea and sclera</span>: protects the eye with tough and transparent tissue
- <span style = "color:lightblue">choroid</span>: provide nutrients through blood vessels and control the size of the pupil
- <span style = "color:lightblue">retina</span>: contains light receptors
- <span style = "color:lightblue">lens</span>: focuses light on to the retina

There are two types of <span style = "color:lightblue">light receptors</span>: cones and rods. <span style = "color:lightblue">Cones</span> are responsible for photopic vision (i.e., higher light levels). They provide color and spatial details and are denser in the center of the retina. <span style = "color:lightblue">Rods</span> are responsible for scotopic vision (i.e., lower light levels). Rods are more abundant than cones by approximately twentyfold.

By varying the **shape of the lens**, the <span style = "color:lightblue">focus length</span> is adjusted, and, accordingly, focusing at different distances is achieved. The light receptors convert the focused light into electrical energy which is decoded by the brain.

### Inconsistencies
The human eye is susceptible to **brightness discrimination** and **optical illusions**. As such, the perceived brightness by the human eye is not a simple function of intensity. For example, as shown below, the <span style = "color:lightblue">Mach band effect</span> describes the phenomenon where the perceived brightness at the edges are darker or lighter than their actual intensity.

![[image-processing-mach-band.png | center | 450]]

## Acquisition

Light originating from an **energy source** is reflected by the **imaging object** and is then received by the **imaging sensor**. Some energy sources include sun, radar, infrared, and X-Ray and ultraviolet.
$$
source \space \rightarrow \space object \space \rightarrow \space sensor
$$
#### Sensor
A <span style = "color:lightblue">sensor</span> consists of a sensing material (i.e., <span style = "color:lightblue">photodiode</span>) and outputs a current when light intensity is detected. The sensor's voltage output is proportional to the ligh intensity.

A <span style = "color:lightblue">charged-coupled device (CCD)</span> is an integrated circuit containing an array of capacitors, where the response of each sensor is proportional to the integral of the light energy projected onto the surface of the sensor. CCD technology is built upon the <span style = "color:lightblue">metal-oxide-semiconductor (MOS)</span> structure.

### Image Formation

The image formation model is shown below.
$$
f(x,y)=i(x,y)r(x,y)
$$
- $f$ represents the energy received by the imaging system
- $i$ represents the illumination of the energy source and ranges from $0$ to $\infty$
- $r$ represents the reflectance (**or transmittance**) of the object and ranges from $0$ to $1$

<span style = "color:lightblue">Reflectance</span> is the property of an object to *reflect* light. Light that is reflected by an object is received by an imaging sensor. On the other hand, <span style = "color:lightblue">transmittance</span> is the propery of an object to *absorb* light. Light can still be transmitted <u>through</u> an object to an image sensor.

> [!INFO]
> An object appears to be a specific color because only the color's wavelengths are reflected.
> 
> For example, green objects reflect wavelengths between 500 to 570 nanometers.

The images below show the typical illumination and reflectance values respectively.

![[image-processing-illumination-val.png|650x300]]

![[image-processing-reflectance-val.png|650x300]]

### Digitization

<span style = "color:lightblue">Sampling</span> and <span style = "color:lightblue">quantization</span> convert a pixel's coordinate position and light amplitude to a discrete value respectively.

Since computers can only process discrete values, a digital image is only an **approximation** of a real, continuous scene. Each digital image consists of a finite number of pixel elements, where each element has a particular **location and value**.

## Representation

In the spatial domain, an image is represented by a grid of pixels with size $M \times N$, where each pixel $f(x,y)$ corresponds to a finite brightness.

<span style = "color:lightblue">Amplitude digitization</span> (i.e., quantization of brightness) requires the number of intensity levels $L$. Due to digital storage and hardware considerations, the number of intensity levels is $2^{k}$ (power of two), where $k$ is an arbitrary number, and the intensity levels range from $0$ to $2^{k} - 1$. Typically, there are 256 levels, where $k$ is equal to $8$. Thus, an $M \times N$ image with 256 intensity levels needs $M \times N \times k$ bits of storage (much less when considering compression).

Reducing the intensity levels will cause <span style = "color:lightblue">false contouring</span>, causing loss of detail in the image (e.g., grey pixels are directly mapped to black).

![[image-processing-false-contouring.png|600x350]]

> [!INFO]
> The image with intensity level $L$ equal to $2$ has the lowest **intensity resolution**.

There are also multi-value image formats, such as <span style = "color:lightblue">color image</span> or <span style = "color:lightblue">RGBA image</span>, where each pixel corresponds to additional values to represent the color of each pixel. Multi-coordinate images are also possible (e.g., medical images).

The <span style = "color:lightblue">pixel count</span> is commonly the resolution of an image. However, additional pixels can be artificially added through <span style = "color:lightblue">interpolation</span> and will not improve the resolution of the image. Pixels have *no physical size* and is applicable to any image of any scale.

The <span style = "color:lightblue">spatial resolution</span> is the smallest discernible detail, while the <span style = "color:lightblue">intensity resolution</span> is the smallest discernible change in intensity level in the image. Typically, spatial resolution is evaluated by <span style = "color:lightblue">dots per inch (dpi)</span>.
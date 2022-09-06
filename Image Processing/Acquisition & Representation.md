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
- $i$ represents the illumination of the energy source and ranges from 0 to $\infty$
- $r$ represents the reflectance (**or transmittance**) of the object and ranges from 0 to 1

<span style = "color:lightblue">Reflectance</span> is the property of an object to *reflect* light. Light that is reflected by an object is received by an imaging sensor. On the other hand, <span style = "color:lightblue">transmittance</span> is the propery of an object to *absorb* light. Light can still be transmitted <u>through</u> an object to an image sensor.

> [!INFO]
> An object appears to be a specific color because only the color's wavelengths are reflected.
> 
> For example, green objects reflect wavelengths between 500 to 570 nanometers.

The images below show the typical illumination and reflectance values respectively.

![[image-processing-illumination-val.png]]



### Digitization
<span style = "color:lightblue">Sampling</span> is the conversion of a pixel's coordinate position into a discrete value, while <span style = "color:lightblue">quantization</span> is the conversion of a pixel's light amplitude into a discrete value. Since computers can only process discrete values, a digital image is an **approximation** of a real, continuous scene.

## Representation

An image is represented by a grid of pixels with size $M \times N$. 

Reducing the intensity levels will cause <span style = "color:lightblue">false contouring</span>, causing loss of detail in the image (e.g., grey pixels are directly mapped to black).


Multi-coordinate images are also possible (e.g., medical images).

The <span style = "color:lightblue">pixel count</span> is commonly the resolution of an image. However, additional pixels can be artificially added through <span style = "color:lightblue">interpolation</span> and will not improve the resolution of the image.
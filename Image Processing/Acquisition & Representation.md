# Acquisition & Representation

## Human Visual System
A <span style = "color:lightblue">human visual system</span> consists of the eyes which are responsible for creating sensory signals and the central nervous system which is responsible for processing the sensory signals.

### The Eye
The human eye consists of several structures for the eye to perform its functions.
- <span style = "color:lightblue">cornea and sclera</span>: protects the eye with tough and transparent tissue
- <span style = "color:lightblue">choroid</span>: provide nutrients through blood vessels and control the size of the pupil
- <span style = "color:lightblue">retina</span>: contains light receptors
- <span style = "color:lightblue">lens</span>: focuses light on to the retina

There are two types of <span style = "color:lightblue">light receptors</span>: cones and rods. <span style = "color:lightblue">Cones</span> are responsible for photopic vision (i.e., higher light levels). They provide color and spatial details and are denser in the center of the retina. <span style = "color:lightblue">Rods</span> are responsible for scotopic vision (i.e., lower light levels). Rods are more abundant than cones by approximately twentyfold.

By varying the **shape of the lens**, the <span style = "color:lightblue">focus length</span> is adjusted, and, accordingly, focusing at different distances is achieved. The light receptors convert the focused light into electrical energy which is decoded by the brain.

### Brightness Discrimination & Optical Illusions


## Acquisition

The image formation model is represented below.
$$
f(x,y)=i(x,y)r(x,y)
$$
- $f$ represents the energy received by the imaging system
- $i$ represents the illumination
- $r$ represents the reflectance (**or transmittance**)

Reflectance is the property of an object to reflect light. Light that is reflected by an object is received by an imaging sensor.

### Digitization
<span style = "color:lightblue">Sampling</span> is the conversion of a pixel's coordinate position into a discrete value, while <span style = "color:lightblue">quantization</span> is the conversion of a pixel's light amplitude into a discrete value. Since computers can only process discrete values, a digital image is an **approximation** of a real, continuous scene.

## Representation

An image is represented by a grid of pixels with size $M \times N$. 

Reducing the intensity levels will cause <span style = "color:lightblue">false contouring</span>, causing loss of detail in the image (e.g., grey pixels are directly mapped to black).


Multi-coordinate images are also possible (e.g., medical images).

The <span style = "color:lightblue">pixel count</span> is commonly the resolution of an image. However, additional pixels can be artificially added through <span style = "color:lightblue">interpolation</span> and will not improve the resolution of the image.
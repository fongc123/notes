# Introduction

Image processing pertains to the manipulation, such as geometric transformation, enhancement, restoration, image segmentation, feature extraction and object recognition, of images which consist of **multiple finite elements** (i.e., a <span style = "color:lightblue">pixel</span>).

## Image Basics

An <span style = "color:lightblue">image</span> is defined as a **two-dimensional** function $f(x,y)$, where $x$ and $y$ are spatial coordinates and $f$ is the intensity or gray level of the image at that point.

Some images include natural image, satelite image, MRI image, microscopy image, CT scans, ultrasound scans, and infrared images. Images are inputted into computers as **an array of numbers**.

<span style = "color:lightblue">Digital image processing</span> refers to the process of performing image processing using a digital computer.

In low-level digital image processing, both the input and output of the process are images. For example, the output of an image compression process is still an image despite the size reduction. Some examples include acquisition, formation, enhancement, restoration, color, and compression.

In a high-level digital image processing, the <span style = "color:lightblue">semantics</span> of the image is further analyzed. The input is an image, but the output is different (e.g., the number of cats detected in the image). Some examples include segmentation (asserting object boundaries), object recognition, and scene understanding.

![An image processing system.|550](image-processing-system.png)


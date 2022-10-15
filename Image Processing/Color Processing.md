Unlike previous [[Intensity Transformations|transformations]], [[Spatial Filtering|spatial filtering]], and [[Frequency Filtering|frequency filtering]], this section describes image processing with colored images instead of only grayscale images (*see [[Color|color]] and [[Acquisition & Representation#Human Visual System|human visual system]]*).

There are two types of color image processing.
- <span style = "color:lightblue">pseudocolor image</span>: assigning colors to gray values
- <span style = "color:lightblue">full color image process</span>: manipulating colored images

# Pseudocolor Processing
Humans can distinguish different colors better than different shades of gray, as found in medical images. Additionally, pseudocolor processing can be used when giving color to originally grayscale images.

<span style = "color:lightblue">Intensity slicing</span> can be performed to assign pixels within above a threshold one color and pixels below the threshold another color. Alternatively, <span style = "color:lightblue">multi-level intensity slicing</span> maps multiple intensity ranges to multiple colors.

![[Pasted image 20221015214621.png|600]]


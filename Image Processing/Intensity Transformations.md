# Intensity Transformations

Specific parts of the image can be enhanced or diminished based on the use case (e.g., for clarity). Primarily, the focus of image transformations is on <u>grayscale images</u>.

<span style = "color:lightblue">Intensity transformations (gray-level mapping)</span> changes the intensity level of an image based on an intensity transformation or mapping function.

$$
s = T(r)
$$
It is usually implemented in a <span style = "color:lightblue">look-up table (LUT)</span> for maximum efficiency.

## Threshold
A threshold function, before or after a certain point the original intenxity level will be retained or lossed.

## Negative
The intensity levels are inverted (i.e., black becomes white).

## Log Transformation
A *log* transformation maps a narrow range of low intensity values in the input to a wider range of output levels. The low intensity values are stretched, while the high intensity values are compressed.

$$c \log(1 + r)$$
## Power-law ($\gamma$) Transformations
$$s = cr^{\gamma}$$
Similar to log transformations. For transformations with $\gamma < 1$, the transformation will stretch low intensity levels and compress high intensity values. It **preserves details with low intensity values**. At low $\gamma$ values, the image becomes increasingly light.

For transformations with $\gamma > 1$, the transformation will stretch high intensity values and compress low intensity values. It **shows more details and greater contrast**.

### $\gamma$ Correction
With the power-law transformation, the <span style = "color:lightblue">power law effect</span> can be corrected using <span style = "color:lightblue">gamma correction</span> or <span style = "color:lightblue">gamma encoding</span>. Both low and high intensity values can be stretched or compressed based on the image.

## Piece-wise Linear Transformations
- Contrast stretching: specifically expand the range of intensity values
- Intensity-level slicing: highlight a specific range of intensities


# Color

Color exists to **highight**, **identify**, and **group** elements. All colors are part of the visible light portion of the electromagnetic spectrum (400 nm - 700 nm).

> [!REVIEW]
> A longer wavelength corresponds to lower energy, while a shorter wavelength corresponds to higher energy.

In the human vision system, cones and rods are responsible for receiving color input. *See [[Acquisition & Representation#The Eye]]* for more details.

## Color Space

To communicate colors precisely, <span style = "color:lightblue">color theories</s and color spaces were created to capture color information.

When color is displayed on a monitor, the RGB (additive) system is used. On the other hand, when color is printed with a printer, the CMYK (subtractive) system is used.

In data visualization, color is used to label, quantify, and highlight graphical elements. Some color selection tips are listed below.
- Red and blue should not be together.
- Blue is not sensitive to human eyes.
- Red-green is a good color combination.

**Rule One: The maximum number of colors used is normally between 6 and 12, where there is a wide range of hues.**

> [!TIP]
> Encoding certain attributes to certain colors based on their semantic meaning improves pre-attentive understanding (e.g., <span style = "color:lightgreen">correct</span>, <span style = "color:indianred">wrong</span>).

Color palettes should be colorful, robust, and perceptually uniform. This [site](https://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3) aids in color palette selection in visualization.

**Rule Two: Sequential data should use a sequence that varies monotonically of at least one of the color channels.** Saturation or lightness can also be used.

**Rule Three: For data that has sequential extremes, paired sequential color schemes based on two different hues is preferred.** The colors diverge toward dark colors of different hues from one common light color.

Other color considerations include temperature, emotion and semantics, and color transparency ($\alpha$ value).

> [!INFO]
> Transparency can display the density and intensity of the data points.

## Harmony & Aesthetic

> [!QUESTION]
> What color combinations are visually pleasing to humans?

<span style = "color:lightblue">Monochromatic</span>: useful for single subjects
<span style = "color:lightblue">Analogous</span>: adjacent colors; peaceful and comfortable mood; seen in nature
<span style = "color:lightblue">Complementary</span>: opposing colors on the color wheel

Viewers with color blindness should also be considered.
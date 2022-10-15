All colors are part of the visible light portion of the electromagnetic spectrum (400 nm - 700 nm), where 400 nm corresponds to violet and 700 nm corresponds to red. A light wave with equal energy in all visible bands appears white.

> [!REVIEW]
> A longer wavelength corresponds to lower energy, while a shorter wavelength corresponds to higher energy.

In the human vision system, cones and rods are responsible for receiving color input and brightness (*see [[Acquisition & Representation#The Eye|the human eye]]*).



# Color Space
To communicate colors precisely, <span style = "color:lightblue">color theories</span> and <span style = "color:lightblue">color spaces</span> were created to capture color information. Each color is assigned a set of coordinates (e.g., RGB) with respect to some color space.

The <span style = "color:lightblue">International Commission on Illumination (CIE)</span> created the <span style = "color:lightblue">CIE RGB</span> and <span style = "color:lightblue">CIE XYZ</span> color spaces. In the CIE XYZ color space, $X$ is a mix of three CIE RGB curves, $Y$ is the luminance or brightness, and $Z$ is quasi-equal to blue of the CIE RGB color space. The <span style = "color:lightblue">CIE XY chromaticity diagram</span> is shown below.

![[data-vis-cie-chromaticity.png|500x450]]

This diagram displays all colors visible to the average human eye. Additionally, a mixture of any two colors (e.g., pure red and pure green) can be found with this chart (*cannot be done by other diagrams*).

# Color Models
Commonly, color can be seen as a combination of three primary colors: red, green, and blue. Color also has additional characteristics.
- <span style = "color:lightblue">brightness</span>: achromatic (*unrelated to color*) notion of intensity
- <span style = "color:lightblue">hue</span>: the dominant color as perceived by an observer (e.g., redness or greenness)
- <span style = "color:lightblue">saturation</span>: the relative purity (i.e., how much white light is mixed)

A <span style = "color:lightblue">color model</span> is a specification of a coordinate system to facilitate the specification of colors in the system's standards.
- <span style = "color:lightblue">RGB model</span>: red, green, blue (*color monitors and video cameras*)
- <span style = "color:lightblue">CMY and CMYK models</span>: cyan, magenta, yellow, black (*printers*)
- <span style = "color:lightblue">HSI model</span>: hue, saturation, intensity (*similar to human visual system*)

The RGB model is the most common, where color is a combination of three primary colors

When color is displayed on a monitor, the <span style = "color:lightblue">RGB (red, green, blue) (additive) system</span> is used. On the other hand, when color is printed with a printer, the <span style = "color:lightblue">CMYK (cyan, magenta, yellow, black) (subtractive) system</span> is used.

![[data-vis-rgb-cmyk.png]]

# Color in Visualization

In data visualization, color is used to **label, quantify, and highlight** graphical elements.

## Color Selection Rules

**Qualitative: The maximum number of colors used is normally between 6 and 12, where there must be a wide range of hues.**

Color palettes should be colorful, robust, and perceptually uniform. This [site](https://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3) aids in color palette selection in visualization.

> [!TIP]
> Encoding certain attributes to certain colors based on their semantic meaning improves pre-attentive understanding (e.g., <span style = "color:lightgreen">correct</span>, <span style = "color:indianred">wrong</span>).

**Sequential: Data should use a sequence that varies monotonically of at least one of the color channels**. Variation in saturation or lightness is also effective.

![[data-vis-selection-sequential.png|400x300]]

**Diverging: For data with sequential extremes, paired sequential color schemes based on two different hues are preferred.** The colors diverge toward dark colors of different hues from one common light color.

![[data-vis-selection-diverging.png|300x25]]

### Additional Considerations

Specific color combinations and their viability are listed below.
- Red and blue should be avoided.
- Blue is not sensitive to human eyes.
- Red-green is a good color combination.
- Color appearance is affected by adjacent colors.
- Contrast affects legibility (e.g., dark text on dark background).

Other color considerations include temperature, emotion and semantics (e.g., <span style = "color:indianred">red</span> for danger, and color transparency ($\alpha$ value).

> [!INFO]
> Transparency can display the density and intensity of the data points.

## Harmony & Aesthetic

> [!QUESTION]
> **Q:** What color combinations are visually pleasing to humans?
> 
> **A:**
> 
> ![[data-vis-selection-harmony.png|400]]

### Color Blindness

Color blindness is present in $6-8\%$ of the population and is typically caused by genetic errors, causing a deficiency in one of the cones.
- <span style = "color:lightblue">protanopia</span>: loss of red cone
- <span style = "color:lightblue">deuteranopia</span>: loss of green cone
- <span style = "color:lightblue">tritanopia</span>: loss of blue cone

A visualization that cannot be comprehended by viewers with color blindness is not a good visualization.

> [!TIP]
> **Solution:** If elements are still distinguishable in grayscale, the visualization should be still be effective.


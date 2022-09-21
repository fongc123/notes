# Visual Channels

<span style = "color:lightblue">Munzner's nested model of visualization design</span>.

Data abstraction $\rightarrow$ idiom design (visual encoding)
- dataset types (e.g., tables, trees, networks)
- data file formats
- attribute types (e.g., categorical or ordered) and ordering direction (e.g., sequential, diverging, cyclic)

A composition of visual encoding consists of <span style = "color:lightblue">marks</span> (i.e., attribute type of a visual element) and <span style = "color:lightblue">visual channels</span> (i.e., attribute value of a visual element). Visual channels, such as color, position, size, and orientation, control the appearance of marks, such as points and lines.

| **Mark** | **Dimensions** |    **Meaning**    | **Encodings**       |
|:--------:|:--------------:|:-----------------:| :-------------------: |
|  Point   |       0        |     Position      | Size, shape, color  |
|   Line   |       1        | Position & length | Width, color, shape |
|   Area   |       2        |         -         | Size & color        |

![[data-vis-visual-channels.png|550]]


> [!WARNING]
> In the below chart, the third dimension is not used. It is unclear whether the number of sales is encoded by **height** or by **volume**.
> 
> ![[data-vis-visual-channels-bad.png|500]]

The <span style = "color:lightblue">Cleveland & McGill experiments</span> showed that visualizations with an aligned axis are more likely to be estimated correctly compared to other forms.

<span style = "color:lightblue">Simkin & Hastie</span> proposed that tasks using various graph types can be understood in terms of **elementary mental processes**.
- <span style = "color:lightblue">anchoring</span>: segment a component to create a comparison standard
- <span style = "color:lightblue">scanning</span>: k
- <span style = "color:lightblue">superimposition</span>:
- <span style = "color:lightblue">projection</span>:

<span style = "color:lightblue">Expressiveness</span> is the sole encoding of information in data, where each data characteristic is matched with a visual channel. <span style = "color:lightblue">Effectiveness</span> is the encoding of only the most important attributes, where accuracy, discriminability, and separability are concerned.

> [!WARNING]
> Some encodings (e.g., width and height or red and green) when combined with each other cannot be decoded separately.


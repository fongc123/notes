<span style = "color:lightblue">Munzner's nested model of visualization design</span> provides guidelines on the process of creating appropritate visualizations. It consists of four layers:
1. **Characterize** the task and data in the problem.
2. **Abstract** the data into operations and data types.
3. Design **visual encoding** and interaction techniques.
4. Create **algorithms** to execute techniques effectively.

![[data-vis-munzner.png|650]]

# Data Abstraction

In <span style = "color:lightblue">data abstraction</span>, the <u>type</u> of the dataset (e.g., tables, trees, networks) and the <u>attributes</u> (e.g., categorical or ordered) to represent those datasets should be considered.

Ordered attributes are categorized as ordinal or as quantitative (*see [[Visualization Basics#Data Types]]*). In ordered attributes, the ordering direction (e.g., sequential, diverging, cyclic) must also be determined. 

Additionally, the format of the data and any preprocessing steps must also be considered. For example, information must be extracted out of data stored in a JSON format.

# Visual Encoding

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

<span style = "color:lightblue">Expressiveness</span> is the sole encoding of information in data, where each data characteristic is matched with a visual channel. <span style = "color:lightblue">Effectiveness</span> is the encoding of only the most important attributes, where accuracy, discriminability, and separability are concerned.

![[data-vis-expressive-effective.png|600]]

> [!WARNING]
> Some encodings (e.g., width and height or red and green) when combined with each other cannot be decoded separately.

# Experimentation

<span style = "color:lightblue">Steven's power law</span> showed the following correlation for many domains.

$$\text{sensation} \propto \text{intensity}^{\space p}$$

![[data-vis-stephen-power-law.png|450]]

A value greater than one indicates that human perception outweighs the actual changes, whereas a value less than one indicates the opposite. It provided ways to assess the accuracy of magnitude estimation for visual encodings. **Length judgements are the most accurate.**

The <span style = "color:lightblue">Cleveland & McGill experiments</span> showed that visualizations with an aligned, baseline axis (e.g., a bar chart) are more likely to be estimated correctly compared to other forms (e.g., rectangular area chart).

<span style = "color:lightblue">Simkin & Hastie</span> proposed that tasks using various graph types can be understood in terms of **elementary mental processes**.
- <span style = "color:lightblue">anchoring</span>: segment a component to create a comparison standard
- <span style = "color:lightblue">scanning</span>: visual sweep across a distance in a graph
- <span style = "color:lightblue">superimposition</span>: mentally move elements to a new, overlapping location
- <span style = "color:lightblue">projection</span>: detect difference in the size of two components.

![[data-vis-simkin-hastie.png]]

Projection creates a more accurate estimate than superimposition.

<span style = "color:lightblue">Scalability</span> should also be considered in extremely large datasets. Gestalt's principles can aid in the grouping of visual encoding (*see [[Principles]]*).


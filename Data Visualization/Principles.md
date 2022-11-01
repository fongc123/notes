<span style = "color:lightblue">Tufte's principles</span> serve as a guide on how to accurately portray data using visual elements. These principles define rules and standards in achieving <span style = "color:lightblue">graphical excellence</span> which is the well-designed presentation of interesting data$\textemdash$a matter of substance, of statistics and of design.
- **graphical integrity**: the accurate and truthful display of data
- **least ink**: create the greatest meaning with the shortest time and the least ink (i.e., maximization of data-ink ratio with good reasons)

# Graphical Integrity

Based on how the data is represented visually, it can be interpreted differently, conveying misleading messages to the audience. The principles present three guidelines to represent data accurately and truthfully.

## I: Lie Factor
The <span style = "color:lightblue">lie factor</span> is a numerical indication of the integrity between data and visualization. **The representation of numbers, as physically measured on the surface of the graph itself, should be directly proportional to the numerical quantities represented.**

$$
\begin{align}
	lie\space factor & =\frac{size\space of \space graphic \space effect}{size \space of \space data \space effect} \newline \newline
	size\space of \space effect & = \frac{|second\space value - first\space value|}{first \space value}
\end{align}
$$

Visualizations with lie factors close to (away from) a value of $1.0$ indicate an accurate (exaggerated) representation of the data. The lie factor should range between $0.95$ and $1.05$.

In the chart below, the line representing 18 miles per gallon in 1978 is 0.6 inches long, while the that of representing 27.5 miles per gallon in 1985 is 5.3 inches long. The lie factor for this graph is $14.8$.

![[data-vis-lie-factor.png|600]]

**Clear labeling should be used to defeat graphical distortion and ambiguity.** The advertisement below gives the impression that the company is generating significant revenue; however, the zero line is positioned differently for each bar chart.

![[data-vis-hidden-0-point.png|600]]

**Data variation should be shown instead of design variation.** Lastly, **the number of dimensions that carry information should not exceed the number of dimensions in the data.** Only design choices that complement the data should be used.

### Misperception of Area
The perception of area versus magnitude varies per person. **For example, the perceived area of a circle grows more slowly than the actual area.**

$$perceived\space area = (actual\space area)^{0.8 \pm 0.3}$$

Thus, volume or area encoding should be avoided. To provide an accurate display, **only** the use of height is needed.

## II: Consistent Scale
A chart must use a consistent scale for all of its data. Typically, a linear scale is sufficient, but a logarithmic scale should be used for logarithmic data.

The chart below makes the income trend appear linear by using an inconsistent scale. The real correlation is exponential.

![[data-vis-consistent-scale.png|500]]

## III: Data in Context

The entire context of the data should be shown. Additionally, the direction of improvement should be indicated.

![[data-vis-data-context.png|300]]

For example, in the chart above, the rank of Cornell University is shown. The chart is interpreted negatively, as a downward trend conveys negative conotations; however, a smaller digit (e.g., $1$) corresponds to a better ranking.

# Least Ink
The <span style = "color:lightblue">data-ink ratio</span> is the ratio of non-white data pixels to the total ink used in the graphic.

$$data\textendash ink \space ratio=\frac{non\textendash redundant\space ink}{total\space ink}$$
Ink usage should prioritize the showcase of data above everything else.

## Chart Junk
<span style = "color:lightblue">Chart junk</span> is the excessive and unnecessary use of graphical elements in visualization for demonstrating the graphic ability of the design *rather* than the display of data.

Excessive chart junk can cause **vibration**, **illusions**, or **visual distortion**.

> [!INFO]
> Chart junk *may* be useful to convey further messages to the viewer, but analytics relies on efficiency and simplicity. Presentation graphs have a low data-ink ratio, while analytical graphs have a high data-ink ratio.

Occassionally, redundancy is useful to demonstrate continuity, especially in a timeline.

Axes and markers should also be properly revised, especially axis aspect ratios, the necessity of dual axes, and axis normalization.

# Tips & Suggestions

Several tips for aesthetics and techniques are listed below.
1. The format and design of the chart should be properly chosen (e.g., a bivariate chart for bivariate data).
2. Words, numbers, and drawings should be used together; words help *explain* the ambiguous parts of the drawing.
3. A balanced, proportionate, and relevant scale should be established.
4. An **accessible** (i.e., not overwhelming) complexity of data should be displayed.
5. A narrative quality is an advantage.
6. The chart is drawn professionally.

<span style = "color:lightblue">Grice's maxims of polite conversation</span> also provides additional graphical design choices. The maxims emphasize the **quantity**, **quality**, **relevance**, and **manner** of visualizations.
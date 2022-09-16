# Principles

<span style = "color:lightblue">Graphical excellence</span> is the well-designed presentation of interesting data$\textemdash$a matter of substance, of statistics and of design.

## Tufte's Principles

<span style = "color:lightblue">Tufte's principles</span> aim to create graphical excellence.
- greatest meaning from shortest time and least ink (maximization of data-ink ratio with good reasons)
- telling the truth

Given specific representations, the data can be interpreted differently, creating completely different meaning.

### I: Lie Factor
The <span style = "color:lightblue">lie factor</span> is a numerical indication of the data-graphic integrity. Visual attribute values should be directly proportional to the actual data attribute value.

$$
\begin{align}
	lie\space factor & =\frac{size\space of \space graphic \space effect}{size \space of \space data \space effect} \newline \newline
	size\space of \space effect & = \frac{|second\space value - first\space value|}{first \space value}
\end{align}
$$

Visualizations with lie factors closer to $1.0$ give a more accurate representation of the data. A lie factor greater than $1.0$ indicates an overstatement.

The advertisement below gives the impression that the company is generating significant revenue; however, the zero line is positioned differently for each bar chart.

![[data-vis-hidden-0-point.png|600]]

#### Perception of Area
The perception of area versus magnitude varies per person.

Volume or area encoding should be avoided. Alternatively, height only is a more accurate display.

### II: Consistent Scale
A chart must use be consistent with its scale. Typically, a linear scale is sufficient, but a logarithmic scale should be used for logarithmic data.

The chart below makes the income trend appear linear by using an inconsistent scale. The real correlation is exponential.

> insert image for scale


### III: Data in Context

The entire context of the data should be shown. Additionally, the direction of improvement should be indicated.

![[data-vis-data-context.png|300]]

For example, in the chart shown, the rank of Cornell University is shown. The chart is interpreted negatively, as a downward trend conveys negative conotations; however, the smaller the rank, the better the university.

## Data-Ink Ratio
The <span style = "color:lightblue">data-ink ratio</span> is the ratio of non-white data pixels to the total ink used in the graphic.

### Chart Junk
<span style = "color:lightblue">Chart junk</span> is the excessive and unnecessary use of graphical elements in visualization for demonstrating the graphic ability of the design *rather* than the display of data.

Excessive chart junk can cause **vibration**, **illusions**, or **visual distortion**.

> [!INFO]
> Chart junk may be useful to convey further messages to the viewer, but analytics relies on efficiency and simplificty. Presentation graphs have a low data-ink ratio, while analytical graphs have a high data-ink ratio.






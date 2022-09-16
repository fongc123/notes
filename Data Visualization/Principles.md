# Principles

<span style = "color:lightblue">Graphical excellence</span> is the well-designed presentation of interesting data$\textemdash$a matter of substance, of statistics and of design.

## Tufte's Principles

<span style = "color:lightblue">Tufte's principles</span> aim to create graphical excellence.
- greatest meaning from shortest time and least ink (maximization of data-ink ratio with good reasons)
- telling the truth

Given specific representations, the data can be interpreted differently, creating completely different meaning.

### Lie Factor
Visual attribute values should be directly proportional to the actual data attribute value.

$$
\begin{align}
	lie\space factor & =\frac{size\space of \space graphic \space effect}{size \space of \space data \space effect} \newline \newline
	size\space of \space effect & = \frac{|second\space value - first\space value|}{first \space value}
\end{align}
$$

Visualizations with lie factors closer to $1.0$ give a more accurate representation of the data. A lie factor greater than $1.0$ indicates an overstatement.

The advertisement below gives the impression that the company is generating significant revenue; however, the zero line is positioned differently for each bar chart.

![[data-vis-hidden-0-point.png|600]]


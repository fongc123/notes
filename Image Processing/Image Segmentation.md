The goal of <span style = "color:lightblue">image segmentation</span> is to identify groups of pixels that belong together or are similar with each other.

Image segmentation partitions a region $R$ into smaller sub-regions $R_1,R_2,\dots,R_n$ with the following conditions.
1. The union of all sub-regions $R_i$ must equal the original region $R$.
2. All sub-regions $R_i$ are connected sets.
3. Any two sub-regions must not intersect.
4. There is a **logical predicate** $Q$ for any sub-region (i.e., they must be distinguishable).

Generally, there are two methods: <span style = "color:lightblue">discontinuity</span> (*edge-based*) and <span style = "color:lightblue">similarity</span> (*region-based*).

For example, the two images below are segmented by edges (c) and by the standard deviation of intensities in a region (f).

![[image-processing-segmentation.png|600]]

# Detection of Sharp Intensity Changes
The following image characteristics produce sharp local changes.
- <span style = "color:lightblue">edge pixels</span>: abrupt change of intensity
- <span style = "color:lightblue">edges</span>: set of connected **edge pixels**
- <span style = "color:lightblue">lines</span>: an edge segment where both sides of the line segment have significantly different intensities
- <span style = "color:lightblue">point</span>: foreground pixel (*brighter*) <u>surrounded</u> by background pixels (*darker*)

## Derivatives
To obtain the **differences** between pixels, <span style = "color:lightblue">derivatives</span> are used. The <span style = "color:lightblue">forward difference</span> considers the next and current pixels, while the <span style = "color:lightblue">backward difference</span> considers the previous and current pixels. Generally, however, <span style = "color:lightblue">central differences</span>, which consider the next and previous pixels, are used.

| **Derivative** | 
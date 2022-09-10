# Perception

<span style = "color:lightblue">Perception</span> is the processing of input signals, while <span style = "color:lightblue">cognition</span> is the understanding and interpretation of those signals.
- encoding: transform data into visual form
- decoding: transform visual form into insights

<span style = "color:lightblue">Heuristics</span> is the process of applying known concepts to the understanding of new concepts.

A graphical method is successful only if the decoding is effective. It should be <span style = "color:lightblue">salient</span>, so that users can **easily** detect patterns and extract insights from the graphical visualization.

## Human Visual System
The human visual system has a high bandwidth to the brain as it is responsible for 70% of all receptors in the brain, 40% of the cortex, and four billion neurons. It retrieves much more visual stimuli than the brain can process.

## Static Patterns
<span style = "color:lightblue">Gestalt psychology</span> is a school of psychology that "emphasizes that organisms perceive entire patterns or configurations and not merely individual components".

> [!INFO]
> In German, *Gestalt* is interpreted as "pattern" or "configuration".

### Proximity
The relationship of objects is emphasized by the proximity and the spatial concentration of the objects.

![[data-vis-gestalt-proximity.png|300x250]]

Due to the proximity arrangement, it is assumed that the circles on the left are related with each other, while that of on the right are not in the above figure.

### Similarity
The relationship of objects is emphasized by the similarity of properties that the objects possess. For example, objects with the same shape (e.g., circles and triangles) or the same texture are assumed to be related.

![[data-vis-gestalt-similarity.png]]

### Connection
A relationship can be created by displaying a visual connection (e.g., a line) between objects.

![[data-vis-gestalt-connection.png|300x250]]

### Enclosure
The principle of **enclosure** is also known as **common area**, and a relationship is created when objects are enclosed by lines or placed in a common container.

![[data-vis-gestalt-enclosure.png|300x150]]

This principle is thought to be the strongest principle. Different frames of reference can also be created using enclosure containers.

### Continuity
Visual entities are perceived as smooth and continuous. An intersection between two objects is more likely to be perceived as individual, uninterrupted objects.

![[data-vis-gestalt-continuity.png|300x250]]

> [!INFO]
> In diagrams, connections between nodes are easily expressed using smooth lines rather than straight lines.

### Common Fate
Visual entities with the same moving direction are perceived as part of the same collection or unit.

![[data-vis-gestalt-common-fate.png|600x250]]

### Symmetry
Symmetric visual entities are viewed as the foreground and are remembered better. Additionally, symmetric forms are preferred, as it creates stability, consistency, and harmony.

![[data-vis-gestalt-symmetry.png]]

The principle of symmetry is especially useful when comparing <span style = "color:lightblue">time-series data</span>.

### Closure
Visual entities that are grouped by closure are part of the same whole. Gaps and complete contours are ignored to create familiar shapes and images.

![[data-vis-gestalt-closure.png|300x200]]

### Figure-ground
The principle of figure-ground refers to the perception of multiple objects by alternating between the foreground and the background.

![[data-vis-gestalt-figure-ground.png]]

<span style = "color:lightblue">
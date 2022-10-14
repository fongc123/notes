<span style = "color:lightblue">Perception</span> is the processing of input signals, while <span style = "color:lightblue">cognition</span> is the understanding and interpretation of those signals.
- encoding: transform data into visual form
- decoding: transform visual form into insights

<span style = "color:lightblue">Heuristics</span> is the process of applying known concepts to the understanding of new concepts.

A graphical method is successful only if the decoding is effective. It should be <span style = "color:lightblue">salient</span>, so that users can **easily** detect patterns and extract insights from the graphical visualization.

The [[Acquisition & Representation#Human Visual System|human visual system]] has a high bandwidth to the brain as it is responsible for 70% of all receptors in the brain, 40% of the cortex, and four billion neurons. It retrieves much more visual stimuli than the brain can process.

# Gestalt Psychology
<span style = "color:lightblue">Gestalt psychology</span> is a school of psychology that "emphasizes that organisms perceive entire patterns or configurations and not merely individual components".

> [!INFO]
> In German, *Gestalt* is interpreted as "pattern" or "configuration".

According to Gestalt psychology, the following statements are observed.
- visual entities are *seen* (perceived) by the brain
- external stimului is understood as **a whole** rather than the sum of its parts
- visual entities are experienced on a regularly, orderly, symmetric and simple basis

## Proximity
The relationship of objects is emphasized by the proximity and the spatial concentration of the objects.

![[data-vis-gestalt-proximity.png|300x250]]

Due to the proximity arrangement, it is assumed that the circles on the left are related with each other, while that of on the right are not in the above figure.

## Similarity
The relationship of objects is emphasized by the similarity of properties that the objects possess. For example, objects with the same shape (e.g., circles and triangles) or the same texture are assumed to be related.

![[data-vis-gestalt-similarity.png]]

## Connection
A relationship can be created by displaying a visual connection (e.g., a line) between objects.

![[data-vis-gestalt-connection.png|300x250]]

## Enclosure
The principle of **enclosure** is also known as **common area**, and a relationship is created when objects are enclosed by lines or placed in a common container.

![[data-vis-gestalt-enclosure.png|300x150]]

This principle is thought to be the strongest principle. Different frames of reference can also be created using enclosure containers.

## Continuity
Visual entities are perceived as smooth and continuous. An intersection between two objects is more likely to be perceived as individual, uninterrupted objects.

![[data-vis-gestalt-continuity.png|300x250]]

> [!INFO]
> In diagrams, connections between nodes are easily expressed using smooth lines rather than straight lines.

## Common Fate
Visual entities with the same moving direction are perceived as part of the same collection or unit.

![[data-vis-gestalt-common-fate.png|600x250]]

## Symmetry
Symmetric visual entities are viewed as the foreground and are remembered better. Additionally, symmetric forms are preferred, as it creates stability, consistency, and harmony.

![[data-vis-gestalt-symmetry.png]]

The principle of symmetry is especially useful when comparing <span style = "color:lightblue">time-series data</span>.

## Closure
Visual entities that are grouped by closure are part of the same whole. Gaps and complete contours are ignored to create familiar shapes and images.

![[data-vis-gestalt-closure.png|300x200]]

## Figure-ground
The principle of figure-ground refers to the perception of multiple objects by alternating between the foreground and the background.

![[data-vis-gestalt-figure-ground.png]]

# Additional Principles
In addition to Gestalt psychology, there are additional principles that dictate the perception of visual entities.
- smaller components are typically seen as figures against a larger background
- **horizontal and vertical orientations** are preferred

## Weber's Law of Just Noticeable Difference
The <span style = "color:lightblue">just noticeable difference (JND)</span> is the threshold that a stimulus difference can be perceived. 

$$\frac{\Delta I}{I}=k$$

The <span style = "color:lightblue">Weber's law of JND</span> states that the **proportion between the stimulus difference threshold $\Delta I$ and the initial stimulus intensity $I$** is equal to a constant $k$. A larger initial stimulus intensity necessitates a larger threshold in order to be perceived.

## Past Experience & Context
In general, the perception of a visual entity is influenced by previous experiences and expectations. An initial piece of information (i.e., the **anchor**) or an exposure to one stimulus (i.e., the **primer**) is used to make a judgement or decision.


# Illusions
An <span style = "color:lightblue">illusion</span> is a perception that arguably differs from reality and is categorized into three main classes.
- physical: caused by physical environment (e.g., water distortion)
- physiological: caused by visual pathway (e.g., an afterimage)
- cognitive: assumptions that cause *unconscious interferences*

Additionally, each class is categorized into four types.
- distortion: contortions in size, length, position, or curvature
- ambiguity: a switch between alternative interpretations
- paradox: visual entities that are physically impossible
- fiction: a figure is perceived even though it is not in the stimulus


![[data-vis-illusion.png|600x275]]

In data visualization, the **surrounding context influences the judgement of shapes and objects**.

![[data-vis-illusion-types.png]]

Some examples of illusions are shown above, where the perceptions of object magnitudes are significantly altered based on the surrounding arrangement.
- <span style = "color:lightblue">Muller-Lyer</span>: the horizontal line segments have identical length
- <span style = "color:lightblue">Ebbinghaus</span>: the circles in the center have identical radius
- <span style = "color:lightblue">Ponzo</span>: the horizontal line segments have identical length

# Pre-attention
Information should be organized into patterns to quickly emphasize similarities and differences.

![[data-vis-pre-attention-types.png]]

By changing object properties, individual objects can be emphasized (i.e., popout effect); however, too many features, especially those that are increasingly similar, will not pop out and will be hard to identify.

> [!INFO]
> Objects of interest should be rapidly identified (~ 10 msec per item).

Some encoding tips are listed below.
- encodings that are easily decodable are preferred
- quantitative variables are shown with position or length
- color or other attributes (e.g., shape and size) are preferred
- symbols should not be overloaded


# Design Rules
The basic design principles and suggestions are listed below and should be followed.
- <span style = "color:lightblue">proximity</span>: group related items together
- <span style = "color:lightblue">alignment</span>: adhere to a static alignment (e.g., comparisons)
- <span style = "color:lightblue">repetition</span>: unify style and consistencies across the entire chart
- <span style = "color:lightblue">contrast</span>: drastically differentiate non-identical objects

> [!INFO]
> In addition to grouping related items together, *unrelated* items should be clearly distinguishable.

The use of <span style = "color:lightblue">chained sequences</span> may be useful for expression dependencies, where the output of the current is the input of the next.

## 3D
**Unnecessary use of three-dimensional displays should be avoided.** In most cases, it adds complexity to a simple problem.
- planar spatial positioning is more effective than depth (*see [[Visual Channels#Experimentation|Steven's power law]]*)
- image plane is acquired more quickly than image depth
- three-dimensional objects create occlusion
- perspective distortion causes loss of information
- three-dimensional text is not legible
- comparisons are harder to make

However, the costs of three-dimensional displays could be outweighed by their benefits in the following scenarios.
- shape perception of three-dimensional data
- spatial data (e.g., geographical map)

Constrained navigational steps through carefully designed three-dimensional viewpoints could offer a new perspective to a two-dimensional chart.

## 2D
Similar to [[#3D|three-dimensional displays]], **the necessary use of two-dimensional displays should be considered.**

> [!QUESTION]
> Does network data require a two-dimensional spatial layout?

Benefits outweigh costs when topological structure or context are important for the design task.

> [!WARNING]
> Just because the data is geographic does not mean that a map must be used. Maps are unsuitable for comparison tasks.

## Eyes & Memory
**It is easier to rely on external cognition than on internal memory.** Comparing side-by-side views is easier than comparing a visible item with an item from memory.

### Animation
The use of animation could be used for **choreographed storytelling** or **transitions between states**. Any changes over time can be *literally* shown with time.

However, animations make comparisons difficult. Additionally, even major changes are difficult to notice if the mental buffer is wiped.

Alternatively, <span style = "color:lightblue">small multiples</span> could be used instead of animations, where one subplot instance is shown for each condition.

![[data-vis-small-multiples.png|600]]

## Resolution & Immersion
**Resolution should be prioritized over immersion.** Immersion (e.g., artificial reality and virtual reality) are only useful in the display of physical objects found in the real world.

## Visualization Mantra
<span style = "color:lightblue">Shneiderman's visualization mantra</span> states that **a good viewing process follows three steps: (1) overview first, (2) zoom and filter, and (3) details on demand.** Each step dives into a deeper level of detail in the visualization.

The mantra is useful for presentation and storytelling and is helpful in explaining complex concepts. To aid in the difficulty during scaling, the overview step may be omitted.

## Function & Form
**Functionality should be prioritized over aesthetics,** which can be refined later. That said, aesthetics should not be ignored, as it improves the experience of viewing the visualization.

## Responsiveness
**User actions should take appropriate response times.** The table below displays three rough categories of <span style = "color:lightblue">visual feedback</span>.

|      **Action**       | **Time (s)** |      **Example**       |
|:---------------------:|:------------:|:----------------------:|
| Perceptual processing |    $0.1$     | Mouseover highlighting |
|  Immediate response   |     $1$      |      Mouse click       |
|      Brief task       |     $10$     | Heavyweight operation                       |

<span style = "color:lightblue">Fitts' law of limits on motor control</span> states that the amount of time required for a person to move a pointer (e.g., a mouse cursor) to a target area is a function of the distance to the target divided by the size of the target.

$$MT=a+b\log_2{2\frac{D}{W}}$$



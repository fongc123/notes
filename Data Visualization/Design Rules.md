# Design Rules

The use of <span style = "color:lightblue">chained sequences</span> is useful for expressing dependencies, where the output of the current is the input of the next.

- no unjustified 3D
	- planar spatial position is more effective than depth
	- danger of depth
	- occlusion
	- perspective distortion $\rightarrow$ loss of information
	- tilted text in 3D is not legible
	- makes comparisons harder
- no unjustified 2D
- eyes beat memory
- resolution over immersion
- visualization mantra
- prioritize function

## Three-dimensional
### Benefits

### Don't use
- useful for shape perception in three-dimensional spatial data
- constrained navigation steps through carefully designed viewpoints (*an animation or interaction*)

## 2D
Two-dimensional representation should be considered when network data requires a two-dimensional spatial layout. Topological structure and context may be important for the task.

## Eyes & Memory
It is easier to compare side-by-side views that are currently shown than comparing views from memory.

<span style = "color:lightblue">Animation</span> is not recommended, as it makes **comparisons difficult**. It may be used for animated transitions.

> [!INFO]
> Even major changes are difficult to notice if mental buffer is wiped.

## Resolution & Immersion
Resolution should be prioritized over immersion. Three-dimensional representations to create immersion are only useful in virtual reality or when displaying data over physical objects found in the real world.

## Shneiderman's Visualization Mantra

<span style = "color:lightblue">Shneiderman's visualization mantra</span> states that the viewing process is (1) overview first, (2) zoom and filter, and (3) details on demand.

This is useful for presentation and storytelling and is helpful in explaining complex concepts. It may be difficult when scaling, and the overview could be omitted.

## Function First, Form Next
Functionality should be prioritized over aesthetics.

## Responsiveness
Three rough categories of <span style = "color:lightblue">visual feedback</span> are listed below.
- $0.1$ seconds: perceptual processing
- $1$ second: immediate response
- $10$ seconds: brief task



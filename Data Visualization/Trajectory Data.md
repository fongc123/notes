A <span style = "color:lightblue">trajectory</span> is the path made by a moving entity through the space it moves (i.e., position over time). Trajectory data can be described by **geometric shape**, **length** (*distance traveled*), **duration** (*time traveled*), **speed**, and **direction**.

As trajectory data consists of <u>a set of localization points of an object's position</u>, trajectory data preprocessing involves two steps: **sampling** (*control the number of points*) and **interpolation** (*connect the curve from points*). Lastly, the trajectory is visualized onto a map.

Trajectory data is present in many real-world applications, most notably transportation, tourism, aviation, and location-based services. Challenges in visualizing trajectory data include **sampling uncertainty**, **noisy data** (e.g., trajectory to a river), and **scalability** (e.g., visual occlusion).

# Patterns
In many applications, objects follow similar trajectory patterns. Trajectories are similar if there exists a time interval such that the distance between the trajectory locations during the time interval is within a spatial threshold (e.g., trucks within a **one-mile** radius of each other **every morning**).

Trajectories can also be clustered together.
- <span style = "color:lightblue">moving object cluster</span>: a set of objects that move close together for an extended period of time
- <span style = "color:lightblue">density-based</span>: average distances between objects for every timestamp
- <span style = "color:lightblue">partition-and-group framework</span>: identification of sub-trajectories (i.e., a common origin of trajectories)

> [!INFO]
> Machine learning techniques can be used to [[Classification|classify]] moving objects based on their trajectories and properties (e.g., <span style = "color:lightblue">the hidden Markov model (HMM)</span> or <span style = "color:lightblue">trajectory-based classification</span>).

# Visualization
The visualization of trajectory data is often challenging due to visual occlusion.
- **spatial**: points, lines, and areas
- **temporal**: animations, color, layout (e.g., clock), three-dimensional views

Other attributes, such as speed and density, can also be encoded by color.

> [!INFO]
> The length and width of the spatial marks can also represent other properties (e.g., magnitude of a trajectory).

[[Design Tasks#Interaction Design|User interaction]] can also be useful in controlling the focus of the visualization (e.g., overview $\leftrightarrow$ detailed).

To reduce clutter, the following techniques may be useful.
- <span style = "color:lightblue">force-directed layout</span>: arrange nodes and edges by attracting and repelling forces (*nodes repel and edges attract*)
- <span style = "color:lightblue">edge bundling</span>: combine [[#Patterns|similar]] trajectories into a bigger trajectory


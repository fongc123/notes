Like [[Classification|classification]], image classification assigns a class label to input images. A classification system looks for a set of <span style = "color:lightblue">patterns</span> (i.e., a spatial arrangement of **features**) in an image that are characteristic to a class.

Features can be extracted [[Feature Extraction|manually]] (e.g., signature, boundary, region, texture, SIFT) or with [[Convolutional Neural Networks|data-driven methods]]. With neural networks, features and patterns are automatically learned, and the model uses them to distinguish between classes.

# Prototype Matching
<span style = "color:lightblue">Prototype matching</span> compares an unknown pattern against a set of prototypes and assigns the unknown pattern to the class of the <u>most similar</u> prototype.
- <span style = "color:lightblue">minimum-distance classifier</span>: [[Clustering#Similarity|Euclidean distance]] between the unknown and the pattern mean
- <span style = "color:lightblue">correlation</span>
- <span style = "color:lightblue">matching SIFT key points</span>


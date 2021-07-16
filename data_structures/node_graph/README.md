# Breadth-First Traversal of a Graph

**Author**: Toby
**Version**: 1.0.0

## Overview
<!-- Provide a high level overview of what this application is and why you are building it, beyond the fact that it's an assignment for a Code Fellows 401 class. (i.e. What's your problem domain?) -->
In this repository, I implement a breadth-first search of a a graph class based on graph node class.


## Challenge
<!-- Description of the challenge -->
* One big challenge of this is visiting management compared to breadth-first search of trees.
* A new graph class based on node. My previous graph class was more like a dictionary structure and didn't use any node class. To make this class more practical and useful, I rewrote the graph class.


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
![](https://github.com/tobyatgithub/data_structure_and_algorithms/blob/master/assets/breadth_first_search_whiteboard.jpeg)
For breadth first search, we only visit each node once (which is nice.)

| Function | Big O Time | Big O Space |
| :------ |:--- | :--- |
| addNode | O(1) | O(1) |
| getNode | O(1) | O(1) |
| addEdge | O(1) | O(1) |
| Breadth-first-search | O(n) | O(n) |



## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->
To run the graph.py code on your machine, you will need python 3.6.

To run the test_graph.py via pytest, you will need both python 3.6 and pytest.
```bash
pip install pytest
pytest -v
```


## API
<!-- Provide detailed instructions for your applications usage. This should include any methods or endpoints available to the user/client/developer. Each section should be formatted to provide clear syntax for usage, example calls including input data requirements and options, and example responses or return values. -->
No API available yet.


## Change Log
<!-- Use this are to document the iterative changes made to your application as each feature is successfully implemented. Use time stamps. Here's an example:-->

1/7/19: first submission on. Both function and documents ready. Passed all test with 81% coverage.

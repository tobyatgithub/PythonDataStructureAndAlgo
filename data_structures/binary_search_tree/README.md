# Find the Maximum Value in a Binary Tree
<!-- Short summary or background information -->
Write a function called find-maximum-value which takes binary tree as its only input. Without utilizing any of the built-in methods available to your language, return the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.


## Challenge
<!-- Description of the challenge -->
Traverse through the binary tree and find the maximum value.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
this function takes in a binary tree as input, and return the maximum value within the tree as output. There are two ways of doing that,
one is modify the tree class such that we add one .max_val to the self. And modifying the insert process accordingly.
The other one is to use any kind of traverse to visit every single node in
the tree, and find out the one with maximum value

## Solution
<!-- Embedded whiteboard image -->
![find_max_binary_tree](https://github.com/tobyatgithub/data_structure_and_algorithms/blob/master/assets/find_max_binary_tree.jpeg)

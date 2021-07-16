# Queue

**Author**: Toby  
**Version**: 1.0.0

## Overview
<!-- Provide a high level overview of what this application is and why you are building it, beyond the fact that it's an assignment for a Code Fellows 401 class. (i.e. What's your problem domain?) -->
In this repository, I implement a queue class based on a standard node class.  
One huge advantage and reason to use queue is its amazing efficiency (constent big O) when coming to add and remove from front and back.   
This can be very handy if you only add and drop at front or back, and don't need to grab value via index.  


## Challenge
<!-- Description of the challenge -->
* This class should be aware of a default None value assigned to front when the isntance is created
* This class should be aware of a default None value assigned to back when the isntance is created
* This class should be aware of the len of the queue, which represents the count of Nodes in the queue at any time
* This class should have the ability to accept an iterable as an argument when instantiated, such as [1, 2, 3, 4], and creates a new Node in the queue for each value in the iterable
* Define any further magic methods such as len and str to support user functionality and informative responses
* Define a method called enqueue which takes any value as an argument and adds that value to the back of the queue with an O(1) Time performance
* Define a method called dequeue which takes no arguments and removes / returns the Node at the front of the queue

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
For queue, we have two handler for the class, one is front, and the other one is back.  
By well managing these two hanlders, we can add at the back and drop at the front with O(1) efficiency.   
We also kept a size feature for the queue to make len() request O(1)  

| Function | Big O Time | Big O Space |
| :------ |:--- | :--- |
| enqueue | O(1) | O(1) |
| dequeue | O(1) | O(1) |
| len() | O(1) | O(1) |
| peek | O(1) | O(1) |
  
  

## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->
To run the queue.py code on your machine, you will need python 3.6.
To run the test_queue.py via pytest, you will need both python 3.6 and pytest.


## API
<!-- Provide detailed instructions for your applications usage. This should include any methods or endpoints available to the user/client/developer. Each section should be formatted to provide clear syntax for usage, example calls including input data requirements and options, and example responses or return values. -->
No API available yet.


## Change Log
<!-- Use this are to document the iterative changes made to your application as each feature is successfully implemented. Use time stamps. Here's an example:-->

12/7/18: first submission on. Both function and documents ready.

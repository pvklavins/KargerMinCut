# Karger Minimum Cut in Python
This is a python 3.0+ implementation of the Karger Minimum Cut Algorithm
This program uses a simple node-network class system.

The program:

*An edge is randomly selected

*The two nodes on that edge are combined

*Self loops are destroyed

*Repeat until there are only two super nodes remaining

*The number of edges between the two super nodes is one possible minimum cut

*This process must be repeated n^2 times to ensure that it is actually the minimum cut (based on probabilities)


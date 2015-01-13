# UniformCost_AI_py
Uniform Cost Search Algorithm implemented in Python.  This is a school project for Artificial Intelligence. 

There are 2 versions available.  Version "maynard_hw1_r1.py" is a NetworkX implementation that solves the problem with Dijkstra algorithm.  Version "maynard_hw1_r5.py" implements the Uniform-Cost Search (UCS) algorithm. 

The pseudo-code for the algorithm is as follows:

# UCS Pseudocode:
# Let fringe be a priority queue containing initial state
# Loop
#     if fringe is empty 
#         return failure
#     node = remove-first(fringe)
#     if node is goal
#         return path from initial state to node
#     else
#         generate all successors of node and put the newly generated
#         nodes into fringe according to their cost values
#
# References: 
# Korzhova, Lecture 5
# "Artificial Intelligence A Modern Approcah", Russell, Norvig
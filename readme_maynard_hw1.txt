There are 2 versions of problem 3 available.  Version "maynard_hw1_r1.py" is a NetworkX implementation that solves the problem with Dijkstra algorithm.  Version "maynard_hw1_r3.py" is an attempt to implement the Uniform-Cost Search (UCS) algorithm.  

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
# Korzhova, Lecture 5, slide 16
# "Artificial Intelligence A Modern Approcah", Russell, Norvig

Everything nearly works but there are some issues adding an pulling children from the fringe priority queue.  I had to comment out some of the code in order to ensure that it compiles and runs.  This is not a complete solution but is 90% there and could be implemented with a little more time and help from my instructor.  I honestly put a LOT of work into this solution but didn't quite make it by the deadline.  I would sincerely love to see a working solution in Python. 

To run the code simply put the input file "input.txt" into the same working dirctory and from a linux / unix command line terminal type "python maynard_hw1_r1.py" or "python maynard_hw1_r3.py".  r1 requires the import of Network X.  
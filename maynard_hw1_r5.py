# ############################################################################
#
# Jason Maynard, U30503758
# HW 1, Problem 3, Directed Graph shortest path 
#
# INPUTS: Weighted directed graph (G), prompt user for 2 verticies (u,v)
#
# OUTPUTS: Shortest path, total weight of shortest path
# 
# Finds shortest path with Uniform-Cost Search (UCS) algorithm.
#
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
# http://aima.cs.berkeley.edu (Online Code Repository)
# 
# ############################################################################

from Queue import PriorityQueue

# ----------------------------------------------------------------------------
# Create node class (Figure 3.10, pg. 79 of text)
# ----------------------------------------------------------------------------
class Node():
    """Nodes are data structures from which the search tree is constructed.
    Each has a parent, a state, and various bookkeeping fields."""

    def __init__(self, path_cost, state, parent):
        """The node constructor. Requires input for path_cost, state,
        parent."""
        self.path_cost = path_cost
        self.state = state 
        self.parent = parent
        
    def expand(self, graph):
        # First get the children
        children = []
        for child in graph[self.state]:
            children.append(Node(child[0] + self.path_cost, child[1], self))        
        
        # We now have a list of children as node objects
        # Next step is to add them to the fringe queue
        
        print '\nExpanding nodes...'
        for child in children:
            if child.state not in closed_list:  
                open_list.put((child.path_cost, child))

    def get_path(self):
        node = self  # Start with myself and see who my parents are
        path = []        
        
        # Build the list of parents to trace back
        while node:
            path.append(node.state)
            node = node.parent
            
        # Return the list that represents the shortest path
        return list(reversed(path))
            
        
# end Node() -----------------------------------------------------------------

# Get the data ---------------------------------------------------------------
# Read the input file and put data into a clean list
# This could be improved with a try / catch block for error checking...
with open ("input.txt") as the_file:
    data = [line.strip().split() for line in the_file]

# Transform the data into a dictionary that represent the nodes, edges, 
# and weights on the graph. 
graph = {}   
for edge in data:
    start, end, cost = edge
    graph.setdefault(start, []).append((int(cost), end))

# Prompt user for starting and ending nodes
# This could be improved with more error checking...
print "Please choose from the following list of available nodes: ", \
      graph.keys() 
start = raw_input("\nEnter a starting node: ")
goal = raw_input("Enter an ending node: ")

# Initialize data structures -------------------------------------------------
open_list = PriorityQueue()
node = Node(0, start, None)  # (path_cost, state, parent)
open_list.put((node.path_cost, node))
closed_list = set()  # we use a set here to ensure no repeated entries

# Run the Uniform Cost algorithm ---------------------------------------------
while not open_list.empty():
    
    print '\nNodes on the open_list:'
    for n in open_list.queue:
        print 'node.state = %s, path_cost = %d' % (n[1].state, n[1].path_cost)
    
    # Pop the node with the highest priority from the fringe queue
    node = open_list.get()
    
    print '\nPopped node %s with path_cost of %d' % \
          (node[1].state, node[1].path_cost)
    
    if node[1].state == goal:
        print '\n============================================================='
        print 'Found solution!'
        print 'Path from %s to %s' % (start, goal)
        print 'Total cost of %d' % node[1].path_cost        
        print "The path from start to finish is: ", node[1].get_path()
        print '============================================================='
        
        break
    
    print 'Goal not found. Keep looking...'
    
    closed_list.add(node[1].state)
    print '\nClosed list: '
    for i in closed_list:
        print i

    node[1].expand(graph)
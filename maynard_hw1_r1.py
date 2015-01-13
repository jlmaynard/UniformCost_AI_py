# ###############################################################################
#
# Jason Maynard, U30503758
# HW 1, Problem 3, Directed Graph shortest path 
#
# INPUTS: Weighted directed graph (G), prompt user for 2 verticies (u,v)
#
# OUTPUTS: Shortest path, total weight of shortest path
# 
# Uses NetworkX directed graphs to model graph
# www.networkx.com
#
################################################################################

import networkx as nx  # Network modeling and analysis
import matplotlib.pyplot as plt  # Graph plotting
import numpy as np  # Numerical Python for matrix
import sys


# Create a new networkX graph object
# DiGraph() indicates that it is a directed graph
G = nx.DiGraph()

# Open files -------------------------------------------------------------------
print 'Opening files'

# Error checking on opening file
# Exit gracefully
try:
    the_file = open('input1.txt', 'r')

except IOError:
    print 'Could not open file'
    sys.exit()


# GET DATA ---------------------------------------------------------------------
# This reads the file, and inputs the raw data into a list.  If there are
# extra new line chars at the end they are also in the list which is
# not desired.
raw_data = []

for the_line in the_file:
    the_line = the_line.strip().split()
    raw_data.append(the_line)

print raw_data

# Count the number of lines in file.
# This prevents problems with extra new line chars at the end of the file.
with open('input1.txt') as the_file:
    num_lines = sum(1 for the_line in the_file if the_line.rstrip('\n'))


# BUILD GRAPH ------------------------------------------------------------------
# Array to hold values read from file
clean_data = np.zeros([num_lines, 3], dtype=int)

# Populate array with values from data
for row in range(num_lines):
    for col in range(3):
        clean_data[row][col] = raw_data[row][col]

print "The clean data as an array: \n", clean_data

# Add edges to build NetworkX graph
G.add_weighted_edges_from(clean_data)

# Draw graph -------------------------------------------------------------------
pos = nx.circular_layout(G)  # set the position variable here
nx.draw_circular(G)
nx.draw_networkx_edge_labels(G, pos, label_pos=0.35)
plt.show()


# ANALYZE GRAPH ----------------------------------------------------------------
start = int(raw_input("\nEnter a starting node: "))
end = int(raw_input("Enter an ending node: "))

print '\nAnalyzing graph with NetworkX'

if nx.has_path(G, start, end):
    path = nx.dijkstra_path(G, start, end)
    length = nx.dijkstra_path_length(G, start, end)

    # RESULTS ------------------------------------------------------------------
    print "\nThe shortest path is: ", path
    print "Total weight: ", length

else:
    print 'No path between those nodes!!!'

# Close files ------------------------------------------------------------------
print '\nClosing files'
the_file.close()
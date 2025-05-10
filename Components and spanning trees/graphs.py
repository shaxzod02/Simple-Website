# An undirected graph is a tree if the graph is connected 
# and acyclic. For example, the following graph is a tree:

# Unlike the trees we have seen previously on this course, this kind of a tree has no root, and the nodes have no children or parents. However, the tree has leaves: The leaves are the nodes with exactly one connecting edge. For example, the leaves of the above tree are 
# 1
# 1, 
# 2
# 2 and 
# 5
# 5.

# When a graph of 
# n
# n nodes is a tree, it has exactly 
# n
# −
# 1
# n−1 edges. If any edge is removed from a tree, it is no longer connected. If a new edge is added to a tree, it is no longer acyclic.

# A spanning tree of a graph is a tree that contains all the nodes of the graph and some subset of the edges. The following figure shows a graph on the left, and one of the spanning trees of the graph on the right:

# Typically a graph has multiple different spanning trees, because there are multiple ways of choosing the edges so that the result is a tree.

# When the graph is weighted, the weight of a spanning tree is computed as the sum of the weights of its edged. As an example, the following figure shows a weighted graph and two of its spanning trees:

# The weight of the first spanning tree is 
# 4
# +
# 1
# +
# 2
# +
# 5
# =
# 12
# 4+1+2+5=12, and the weight of the second spanning tree is 
# 2
# +
# 1
# +
# 2
# +
# 5
# =
# 10
# 2+1+2+5=10.

# In this case, the second spanning tree happens to be a minimum spanning tree of the graph, i.e., a spanning tree with the smallest possible weight. There can be multiple minimum spanning trees.

# Kruskal’s algorithm
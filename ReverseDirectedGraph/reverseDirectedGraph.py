# Given a directed graph, reverse the directed graph so all directed edges are reversed.

# Example:
# Input:
# A -> B, B -> C, A ->C

# Output:
# B->A, C -> B, C -> A

#Proposed Solution: O(V + E)
# For each node visit the adjacency list
# For each adjacent node add an item to a hashmap with k = adjacent node value and V = parent node.value
# Rivisit the tree and for each node swap the adjacent node with the adjacecy list in the hashmap at key Node.value 

from collections import defaultdict
import copy

class Node:
  def __init__(self, value):
    self.adjacent = []
    self.value = value

def reverse_graph(graph):
	# Fill this in.
	reverted = {}

	for _,n in graph.items():
  		for adj in n.adjacent: 
  			if adj.value in reverted:
  				reverted[adj.value] += [n]
  			else:
  				reverted[adj.value] = [n]
  	
  	for _,n in graph.items():
  		if n.value in reverted:
			n.adjacent = reverted[n.value]
		else:
			n.adjacent = []
  	return graph


a = Node('a')
b = Node('b')
c = Node('c')

a.adjacent += [b, c]
b.adjacent += [c]

graph = {
    a.value: a,
    b.value: b,
    c.value: c,
}


for _, val in graph.items():
	print(val.adjacent)
print("")
for _, val in reverse_graph(graph).items():
	print(val.adjacent)


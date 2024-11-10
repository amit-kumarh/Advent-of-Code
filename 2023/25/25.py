import sys
import networkx as nx
import re
import math

with open(sys.argv[1]) as f:
    contents = f.read().strip().splitlines()

graph = nx.Graph()
for line in contents:
    nodes = re.findall(r'[a-z]{3}', line)
    for n in nodes[1:]:
        graph.add_edge(nodes[0], n)

graph.remove_edges_from(nx.minimum_edge_cut(graph))
print(math.prod(len(c) for c in nx.connected_components(graph)))

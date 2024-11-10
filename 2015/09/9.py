import sys
from itertools import permutations
from collections import defaultdict

with open(sys.argv[1]) as f:
    contents = f.read().splitlines()

g, locs = defaultdict(dict), set()
for line in contents:
    source, _, dest, _, distance = line.split()
    locs.update({source, dest})
    g[source][dest] = int(distance)
    g[dest][source] = int(distance)

distances = [sum(g[way[i]][way[i+1]] for i in range(len(way)-1)) for way in permutations(locs)]

print(min(distances))
print(max(distances))





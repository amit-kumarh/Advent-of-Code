import sys
from collections import defaultdict
from itertools import permutations

with open(sys.argv[1], 'r') as f:
    contents = f.read().splitlines()

SIGN = {'lose': -1, 'gain': 1}

def gen_graph(contents, p2=False):
    G = defaultdict(dict)
    for line in contents:
        source, _, dir, num, _, _, _, _, _, _, dest = line.split()
        G[source][dest[:-1]] = int(num) * SIGN[dir]

    if p2:
        G['me'] = {}
        for k in G.keys():
            G[k]['me'] = 0
            G['me'][k] = 0
    return G

def solve(G):
    ans = 0
    for way in permutations(G.keys()):
        total = 0
        for i, p in enumerate(way):
            total += G[p][way[(i+1)%len(way)]] + G[p][way[(i-1)%len(way)]]
        ans = max(ans, total)
    print(ans)

solve(gen_graph(contents))
solve(gen_graph(contents, True))

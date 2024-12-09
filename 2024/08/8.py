import sys
import itertools
from collections import defaultdict

with open(sys.argv[1]) as f:
    contents = f.read().strip().splitlines()
    grid = {complex(r, c): char for r, row in enumerate(contents) for c, char in enumerate(row)}

antennas = defaultdict(set)
for k, v in grid.items():
    if v == '.':
        continue
    antennas[v].add(k)

find_next_antinode = lambda a, b: complex(a.real + (a.real - b.real),  (a.imag + (a.imag - b.imag)))

p1 = set()
for freq, antenna in antennas.items():
    for a, b in itertools.permutations(antenna, 2):
        if (an := find_next_antinode(a, b)) in grid:
            p1.add(an)

print(len(p1))

p2 = set()
for freq, antenna in antennas.items():
    for a, b in itertools.permutations(antenna, 2):
        p2.update({a, b})
        while (an := find_next_antinode(a, b)) in grid:
            p2.add(an)
            a, b = an, a

print(len(p2))

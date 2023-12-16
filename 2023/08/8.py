import sys
import itertools
import re
import math

with open(sys.argv[1]) as f:
    c = f.read().strip()

dir, rest = c.split('\n\n')
dir = itertools.cycle(dir)

grid = {}
for line in rest.splitlines():
    curr, L, R = re.findall(r'[0-9A-Z]{3}', line)
    grid[curr] = (L, R)

curr, ans = 'AAA', 0
while curr != 'ZZZ':
    ans += 1
    d = next(dir)
    match d:
     case 'L': 
         curr = grid[curr][0]
     case 'R': 
         curr = grid[curr][1]

print(ans)

dir = itertools.cycle(dir)
curr = [c for c in grid if c[-1] == 'A']
res = [0 for _ in range(len(curr))]
while not all(c[-1] == 'Z' for c in curr):
    d = next(dir)
    for i, c in enumerate(curr):
        if c[-1] == 'Z':
            continue
        match d:
         case 'L': 
             res[i] += 1
             curr[i] = grid[c][0]
         case 'R': 
             res[i] += 1
             curr[i] = grid[c][1]

print(math.lcm(*res))
    

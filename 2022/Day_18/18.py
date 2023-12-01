import numpy as np
import functools
from collections import Counter, deque, defaultdict
import re
import sys

infile = sys.argv[1] if len(sys.argv)>1 else 'input'

def get_input():
    with open(infile, 'r') as file:
        contents = file.read().strip().split('\n')
    
    return contents

ADJ = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
def sides(cube):
    return [(cube[0]+dx, cube[1]+dy, cube[2]+dz) for dx, dy, dz in ADJ]


def p1():
    contents = get_input()
    ans = 0
    cubes = set()
    for line in contents:
        cube = [int(x) for x in re.findall(r'-?\d+', line)]
        cubes.add(tuple(cube))
        ans += 6
        for adj in sides(cube):
            if adj in cubes:
                ans -= 2
    print(ans)

def p2():
    contents = get_input()
    ans = 0
    cubes = set()
    for line in contents:
        cubes.add(tuple([int(x) for x in re.findall(r'-?\d+', line)]))

    # Floodfill with BFS
    q = [(-1, -1, -1)]
    seen = set()
    while q:
        curr = q.pop()
        seen.add(curr)
        for adj in sides(curr):
            if adj not in cubes and adj not in seen and all(-1<=c<=25 for c in adj):
                q.append(adj)
        seen |= {curr}

    print(sum((s in seen) for c in cubes for s in sides(c)))
    
if __name__ == '__main__':
    p1()
    p2()


import sys

with open(sys.argv[1]) as f:
    contents = f.read().strip().splitlines()
    L = len(contents)
    grid = {complex(i, j): char for i, line in enumerate(contents) for j, char in enumerate(line)}

stops = [64, 65, 131+65, 131*2+65]
q = {complex(65, 65)}
points = []
for rep in range(1, stops[-1]+1):
    nq = set()
    for curr in q:
        for d in (1, -1, 1j, -1j):
            next = curr + d
            wrapped = complex(next.real % L, next.imag % L)
            if grid[wrapped] != '#':
                nq.add(next)
    q = nq
    if rep in stops:
        match rep:
            case 64: print(f"Part 1: {len(q)}")
            case _: points.append(len(q))

b = points[1]-points[0]
a = points[2]-(2*points[1]) + points[0]
x = 202300 # 26501365 - 65 % 131
print(f"Part 2: {points[0] + b*x + a*(x*(x-1)//2)}")

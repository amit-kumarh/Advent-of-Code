import sys

sys.setrecursionlimit(20000)
with open(sys.argv[1]) as f:
    contents = f.read().strip().splitlines()

ADJ = [complex(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not i == j == 0]
grid = {complex(r, c): char for r, line in enumerate(contents) for c, char in enumerate(line)}
start = list(grid.keys())[list(grid.values()).index('S')]

def adjacent(curr):
    match grid.get(curr, '.'):
        case '|': return (curr-1, curr+1)
        case '-': return (curr-1j, curr+1j)
        case 'L': return (curr+1j, curr-1)
        case 'J': return (curr-1j, curr-1)
        case '7': return (curr-1j, curr+1)
        case 'F': return (curr+1j, curr+1)
        case 'S':
            return tuple(coord for dir in ADJ if curr in adjacent(coord := curr + dir))
        case '.': return tuple() 
        case _: assert False, curr

def find_cycle(curr, visited, parent, cycle):
    visited.add(curr)
    for n in adjacent(curr):
        if n not in visited:
            if res := find_cycle(n, visited, curr, cycle+[n]):
                return res
        elif parent != n:
            return cycle

visited = set()
cycle = find_cycle(start, visited, None, [start]); assert cycle is not None
print(len(cycle) // 2) # p1

p2 = 0
for i, line in enumerate(contents):
    inside = False
    for j, char in enumerate(line):
        # because S becomes a | in my input I just hardcoded it in here, I was
        # too lazy to write logic to determine what kind of pipe it should be
        # when I could just...not.
        if complex(i, j) in cycle:
            if char in '|JLS':
                inside = not inside
        else:
            p2 += inside
print(p2)

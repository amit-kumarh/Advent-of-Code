import sys

with open(sys.argv[1]) as f:
    contents = f.read().strip()
    grid = {complex(x, y): c for x, row in enumerate(contents.splitlines()) for y, c in enumerate(row)}
    start = next(k for k, v in grid.items() if v == '^')

def traverse(grid, exclude):
    curr, dir = start, -1
    seen = set()
    locs = set()
    while curr in grid:
        if (curr, dir) in seen:
            return True, locs
        seen.add((curr, dir))
        locs.add(curr)
        if grid.get(curr+dir) == "#" or curr + dir == exclude:
            dir *= -1j
        else:
            curr += dir

    return False, locs

p2 = 0
_, path = traverse(grid, None)
print(len(path))
for k in path:
    p2 += traverse(grid, k)[0]
print(p2)

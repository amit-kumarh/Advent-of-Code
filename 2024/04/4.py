import sys

with open(sys.argv[1]) as f:
    contents = f.read().strip().splitlines()
    grid = {complex(i, j): c for i, row in enumerate(contents) for j, c in enumerate(row)}

ADJ = [complex(i, j) for i in range(-1, 2) for j in range(-1, 2) if i or j]
XMAS = 'XMAS'
p1 = 0
for pos, val in grid.items():
    for a in ADJ:
        curr = pos
        idx = 0
        while grid.get(curr) == XMAS[idx]:
            curr += a
            idx += 1
            if idx == len(XMAS):
                p1 += 1
                break

print(p1)


p2 = 0
CORNERS = [-1 + 1j, 1 + 1j, -1 - 1j, 1 - 1j]
for pos, val in grid.items():
    if val == 'A':
        corns = [grid.get(pos + c) for c in CORNERS]
        if corns.count('M') == 2 and corns.count('S') == 2:
            if not (grid.get(pos + CORNERS[0]) == grid.get(pos+CORNERS[3])):
                p2 += 1
print(p2)

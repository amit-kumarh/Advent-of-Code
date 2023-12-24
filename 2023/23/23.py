import sys

with open(sys.argv[1]) as f:
    contents = f.read().strip().splitlines()
    grid = {complex(i, j): char for i, line in enumerate(contents) for j, char in enumerate(line)}
    S = complex(0, 1)
    E = complex(len(contents)-1, len(contents[0])-2)

def gen_graph(p1):
    graph = {}
    for curr, char in grid.items():
        if char != '#':
            neighbors = set()
            if char in '<>^v' and p1:
                match char:
                    case '>': dir = 1j,
                    case '<': dir = -1j,
                    case '^': dir = -1,
                    case 'v': dir = 1,
                    case _: assert False
            else:
                dir = (-1, 1, 1j, -1j)

            for d in dir:
                next = curr + d
                if next in grid and grid[next] != '#':
                    neighbors.add((next, 1))
            graph[curr] = neighbors

    if not p1:
        while True:
            for curr, neighbors in graph.items():
                if len(neighbors) == 2:
                    a, b = neighbors
                    # remove curr from the edges of both its neighbors
                    graph[a[0]].remove((curr, a[1]))
                    graph[b[0]].remove((curr, b[1]))
                    # link the neighbors to each other
                    graph[a[0]].add((b[0], a[1] + b[1]))
                    graph[b[0]].add((a[0], a[1] + b[1]))
                    # remove curr from graph
                    del graph[curr]
                    break
            else:
                break

    return graph


def solve(p1):
    s = [(S, 0, set())]
    graph = gen_graph(p1)
    ans = None
    while s:
        curr, step, seen = s.pop()
        if curr == E:
            if ans is None or step > ans:
                ans = step

        for next, cost in graph[curr]:
            if next not in seen:
                s.append((next, step+cost, seen.union({next})))
    return ans

print(solve(True))
print(solve(False))

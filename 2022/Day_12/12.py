import re
from functools import reduce
from collections import Counter, defaultdict, deque
import numpy as np
import networkx as nx

def get_input():
    with open('input', 'r') as file:
        contents = [list(l.strip()) for l in file.readlines()]
    return contents

ADJ = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def solve(start):
    grid = get_input()
    end = (20, 146)
    grid[start[0]][start[1]] = 'a'
    grid[end[0]][end[1]] = 'z'
    visited = {}
    q = deque()
    q.append(start)
    done = False
    while q:
        curr = q.pop()
        val = grid[curr[0]][curr[1]]
        if curr == end:
            done = True
            break

        possible = []
        for x, y in ADJ:
            newx, newy = curr[0] + x, curr[1] + y
            if not (newx < 0 or newy < 0 or newx >= len(grid) or newy >= len(grid[0])):
                if ord(grid[newx][newy]) - ord(val) <= 1:
                    if (newx, newy) not in visited:
                        possible.append((newx, newy))

        for next in possible:
            q.appendleft(next)
            visited[next] = curr
        

    path = []
    while curr != start:
        path.append(curr := visited[curr])

    if done:
        return path

    return None



def p2():
    contents = get_input()
    ass = []
    for i, row in enumerate(contents):
        for j, cell in enumerate(row):
            if cell == 'a':
                ass.append((i, j))
    
    ans = 100000
    for a in ass:
        p = solve(a)
        if p:
            if len(p) < ans:
                ans = len(p)
    print(ans)



if __name__ == '__main__':
    print(solve((20, 0)))
    p2()

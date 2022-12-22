import re
from functools import reduce
from collections import Counter, defaultdict, deque
from treelib import Node, Tree
import numpy as np

def get_input():
    with open('input', 'r') as file:
        contents = file.read().strip().split('\n')
    return contents

def solve():
    contents = get_input()
    nodes = np.zeros((10, 2), int)
    visited = {(0, 0)}

    for line in contents:
        line = line.split()
        delta = {'D': (1, 0), 'U': (-1, 0), 'R': (0, 1), 'L': (0, -1)}[line[0]]
        for _ in range(int(line[1])):
            nodes[0] += delta
            for front, rear in zip(nodes[:-1], nodes[1:]):
                if abs(front-rear).max() > 1:
                    rear += np.sign(front - rear)
            visited.add(tuple(rear))

    print(len(visited))

if __name__ == '__main__':
    solve()

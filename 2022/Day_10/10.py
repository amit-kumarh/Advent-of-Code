import re
from functools import reduce
from collections import Counter, defaultdict, deque
import numpy as np

def get_input():
    with open('input', 'r') as file:
        contents = file.read().strip().split('\n')
    return contents

def solve():
    contents = get_input()
    X = 1
    cycles = 1
    tot = 0
    for line in contents:
        if line == 'noop':
            cycles += 1
            if (cycles -20) % 40 == 0:
                tot += X * cycles
        else:
            line = line.split(' ')
            cycles += 1
            if (cycles -20) % 40 == 0:
                tot += X * cycles
            cycles += 1
            X += int(line[1])
            if (cycles -20) % 40 == 0:
                tot += X * cycles

    print(tot)

def p2():
    contents = get_input()
    X = 1
    cycles = 0
    row = [' ' for x in range(40)]
    grid = [row[:] for x in range(6)]
    if cycles%40 in [X, X-1, X+1]:
        grid[cycles // 40][cycles % 40] = '#'
    for line in contents:
        if line == 'noop':
            cycles += 1
            if cycles%40 in [X, X-1, X+1]:
                grid[cycles // 40][cycles % 40] = '#'
        else:
            line = line.split(' ')
            cycles += 1
            if cycles % 40 in [X, X-1, X+1]:
                grid[cycles // 40][cycles % 40] = '#'
            cycles += 1
            X += int(line[1])
            if cycles % 40 in [X, X-1, X+1]:
                grid[cycles // 40][cycles % 40] = '#'

    for row in grid:
        print(' '.join(row))

if __name__ == '__main__':
    solve()
    p2()

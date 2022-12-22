import numpy as np
import functools
from collections import Counter, deque, defaultdict
import re

def get_input():
    with open('input', 'r') as file:
        lines = file.readlines()

    lowest = leftest = rightest = None
    grid = defaultdict(lambda: '.')
    for line in lines:
        pts = [complex(*map(int, cd.split(','))) for cd in line.split(' -> ')]
        for i in range(len(pts)):
            if lowest is None or pts[i].imag > lowest:
                lowest = int(pts[i].imag)
            if leftest is None or pts[i].real < leftest:
                leftest = int(pts[i].real)
            if rightest is None or pts[i].real > rightest:
                rightest = int(pts[i].real)

            if i == len(pts)-1:
                break

            diff = pts[i+1] - pts[i]
            dx, dy = map(int, [diff.real, diff.imag])
            if np.sign(dx):
                for step in range(0, dx + np.sign(dx), np.sign(dx)):
                    grid[pts[i]+step] = '#'
            if np.sign(dy):
                for step in range(0, dy + np.sign(dy), np.sign(dy)):
                    grid[pts[i]+step*1j] = '#'

    return grid, lowest, rightest, leftest
    
def abyss(pos, lowest, rightest, leftest):
    if pos.real > rightest or pos.real < leftest or pos.imag > lowest:
        return True
    return False

def solve(part):
    grid, lowest, rightest, leftest = get_input()
    sand = complex(500, 0)
    quantity = 0
    while not abyss(sand, lowest, rightest, leftest):
        if grid[sand + 1j] == '.':
            grid[sand] = '.'
            sand += 1j
            grid[sand] = 'o'
        elif grid[sand -1+1j] == '.':
            grid[sand] = '.'
            sand += -1+1j
            grid[sand] = 'o'
        elif grid[sand + 1+1j] == '.':
            grid[sand] = '.'
            sand += 1+1j
            grid[sand] = 'o'
        else:
            sand = complex(500, 0)
            quantity += 1

    print(quantity)

def p2():
    grid, lowest, rightest, leftest = get_input()
    for i in range(-10_000, 10_0001):
        grid[i+(lowest+2)*1j] = '#'

    print(grid[-1000+11j])
    sand = complex(500, 0)
    quantity = 0
    while True:
        if grid[sand + 1j] == '.':
            grid[sand] = '.'
            sand += 1j
            grid[sand] = 'o'
        elif grid[sand -1+1j] == '.':
            grid[sand] = '.'
            sand += -1+1j
            grid[sand] = 'o'
        elif grid[sand + 1+1j] == '.':
            grid[sand] = '.'
            sand += 1+1j
            grid[sand] = 'o'
        else:
            quantity += 1
            if sand == 500:
                break
            sand = complex(500, 0)
    print(quantity)


if __name__ == '__main__':
    solve(1)
    p2()

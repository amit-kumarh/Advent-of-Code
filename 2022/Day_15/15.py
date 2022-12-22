import numpy as np
import functools
from collections import Counter, deque
import re
from z3 import *

def get_input():
    with open('input', 'r') as file:
        contents = file.readlines()
    sensors = {}
    diffs = {}
    for line in contents:
        nums = list(map(int, re.findall(r'\d+', line)))
        sensors[(nums[0], nums[1])] = (nums[2], nums[3])
        diffs[(nums[0], nums[1])] = manhattan((nums[0], nums[1]), (nums[2], nums[3]))

    return sensors, diffs
    
def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def solve(part):
    sensors, diffs = get_input()
    ans = 0
    for x in range(-9019876, 9019876):
        if x % 100_000 == 0:
            print(x)
        tp = (x, 2000000)
        if tp in sensors.values():
            continue
        for s, d  in diffs.items():
            if manhattan(s, tp) <= d:
                ans += 1
                break
    print(ans)

def p2():
    sensors, _ = get_input()
    SEARCH_SIZE = 4_000_000
    x, y, solution = Int('x'), Int('y'), Int('solution')
    sol = Solver()
    sol.add(solution == 4_000_000 * x + y, x >= 0, y >= 0, x <= SEARCH_SIZE, y <= SEARCH_SIZE)
    for s, b in sensors.items():
        sx, sy = s[0], s[1]
        d = manhattan(s, b)
        sol.add(Abs(sx - x) + Abs(sy - y) > d)
    sol.check()
    print(sol)
    print(sol.model())

if __name__ == '__main__':
    #solve(1)
    p2()

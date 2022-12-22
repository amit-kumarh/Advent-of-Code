import re
from functools import reduce
from collections import Counter, defaultdict, deque
import numpy as np

def get_input():
    with open('input', 'r') as file:
        ms = map(lambda x: x.split('\n'), file.read().strip().split('\n\n'))

    monkeys = []
    MODS = []
    TRUE = []
    FALSE = []
    FUNCS = []
    def new_func(str):
        def the_func(old):
            return eval(str)
        return the_func
    for m in ms:
        monkeys.append([int(x) for x in re.findall(r'\d+', m[1])])
        MODS.append(int(re.findall(r'\d+', m[3])[0]))
        TRUE.append(int(re.findall(r'\d+', m[4])[0]))
        FALSE.append(int(re.findall(r'\d+', m[5])[0]))
        FUNCS.append(new_func(m[2][m[2].index('old'):]))

    return monkeys, MODS, TRUE, FALSE, FUNCS


def solve(part):
    inspections = [0] * 8
    monkeys, MODS, TRUE, FALSE, FUNCS = get_input()
    big_mod = reduce(lambda a, b: a*b, MODS)
    rounds = 20 if part == 1 else 10_000
    for _ in range(rounds):
        for i, m in enumerate(monkeys):
            while m:
                curr = m.pop(0)
                inspections[i] += 1
                curr = FUNCS[i](curr)
                if part == 1:
                    curr //= 3
                else:
                    curr %= big_mod

                if curr % MODS[i] == 0:
                    monkeys[TRUE[i]].append(curr)
                else:
                    monkeys[FALSE[i]].append(curr)

    print(monkeys)
    inspections.sort(reverse=True)
    print(inspections[0] * inspections[1])

if __name__ == '__main__':
    solve(1)
    solve(2)

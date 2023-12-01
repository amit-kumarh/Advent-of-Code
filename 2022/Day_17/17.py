import numpy as np
import functools
from collections import Counter, deque, defaultdict
import re
from itertools import cycle
from aocd import submit

def get_input():
    with open('input', 'r') as file:
        contents = list(file.read().strip())
    return contents

def minus(top):
    return [complex(2, top+4), complex(3, top+4), complex(4, top+4), complex(5, top+4)]

def stick(top):
    return [complex(2, top+4), complex(2, top+5), complex(2, top+6), complex(2, top+7)]

def plus(top):
    return [complex(2, top+5), complex(3, top+5), complex(4, top+5), complex(3, top+4), complex(3, top+6)]

def square(top):
    return [complex(2, top+4), complex(3, top+4), complex(2, top+5), complex(3, top+5)]

def L(top):
    return [complex(2, top+4), complex(3, top+4), complex(4, top+4), complex(4, top+5), complex(4, top+6)]

def moveRight(r, filled):
    for cell in r:
        if cell.real == 6 or cell + 1 in filled:
            return r

    for i, _ in enumerate(r):
        r[i] += 1

    return r
        
def moveLeft(r, filled):
    for cell in r:
        if cell.real == 0 or cell - 1 in filled:
            return r

    for i, _ in enumerate(r):
        r[i] -= 1
    return r

def main():
    air = get_input()
    rocks = [minus, plus, L, stick, square]
    la = len(air)
    ai = -1
    top = 0
    tower = set([0, 1, 2, 3, 4, 5, 6])

    for step in range(2022):
        # print(ai, step%5) 
        r = rocks[step % 5](top)

        falling = True
        while falling:
            ai += 1
            if ai == la:
                ai = 0
            a = air[ai]

            match a:
                case '>':
                    r = moveRight(r, tower)
                case '<':
                    r = moveLeft(r, tower)

            for cell in r:
                if cell - 1j in tower:
                    falling = False
                    tower.update(r)
                    top = max([c.imag for c in tower])
                    tower = set(filter(lambda x: x.imag > top - 100, tower))
                    break
            else:
                for i, _ in enumerate(r):
                    r[i] -= 1j

    print(top)
    # submit(int(top), part="a", day=17, year=2022)

def p2():
    air = get_input()
    rocks = [minus, plus, L, stick, square]
    jets = {'<': moveLeft, '>': moveRight}
    la = len(air)
    ai = -1
    top = 0
    tower = set([0, 1, 2, 3, 4, 5, 6])
    cache = {}

    for step in range(int(1e12)):
        ri = step % 5
        r = rocks[ri](top)

        falling = True
        key = ri, ai
        if key in cache and step > 1000:
            S, T = cache[key]
            d, m = divmod(1e12-step, step-S)
            print(S, T, d, m)
            if m == 0:
                print("cache", top + (top-T)*d)
                break
        else:
            cache[key] = step, top

        while falling:
            ai = (ai + 1) % la
            a = air[ai]
            r = jets[a](r, tower) # move sideways

            for cell in r:
                if cell - 1j in tower:
                    falling = False
                    for cell in r:
                        tower.add(cell)
                    top = max([c.imag for c in tower])
                    tower = set(filter(lambda x: x.imag > top - 75, tower))
                    cache[step] = tuple(tower)
                    break
            else:
                for i, _ in enumerate(r):
                    r[i] -= 1j

    print(top)


if __name__ == '__main__':
    # main()
    p2()

import sys
import re

with open(sys.argv[1], 'r') as f:
    contents = f.read()

map, inst = contents.split('\n\n')
grid = {complex(r, c): char for r, line in enumerate(map.split('\n')) for c, char in enumerate(line) if char != ' '}
S = len([x for x in grid if x.real == 0])
inst = re.findall(r"R|L|\d+", inst)

def wrap1(pos, dir):
    curr = pos
    while curr + -dir in grid:
        curr += -dir

    return curr

def wrap2(pos, dir):
    r, c = pos.real, pos.imag
    match dir, r//50, c//50:
        case  1j, 0, _: return complex(149-r, 99), -1j
        case  1j, 1, _: return complex(49, 50+r), -1
        case  1j, 2, _: return complex(149-r, 149), -1j
        case  1j, 3, _: return complex(149, r-100), -1
        case -1j, 0, _: return complex(149-r, 0),  1j
        case -1j, 1, _: return complex(100, r-50),  1
        case -1j, 2, _: return complex(149-r, 50),  1j
        case -1j, 3, _: return complex(0, r-100),  1
        case  1 , _, 0: return complex(0, c+100),  1
        case  1 , _, 1: return complex(c+100 , 49), -1j
        case  1 , _, 2: return complex(c-50, 99), -1j
        case -1 , _, 0: return complex(c+50, 50),  1j
        case -1 , _, 1: return complex(c+100, 0),  1j
        case -1 , _, 2: return complex(199, c-100), -1
        case _: assert False

def solve(part1):
    curr = min(c.imag for c in grid.keys() if c.real == 0) * 1j
    dir = 1j
    for move in inst:
        match move:
            case "R": dir *= -1j
            case "L": dir *= 1j
            case _:
                for _ in range(int(move)):
                    npos, ndir = curr + dir, dir
                    if npos not in grid:
                        if part1:
                            npos = wrap1(npos,dir)
                        else:
                            npos, ndir = wrap2(npos, dir)

                    if grid[npos] == ".":
                        curr, dir = npos, ndir


    print(round(sum([1000*(curr.real+1), 4*(curr.imag+1), [1j, -1, -1j, 1].index(dir)])))

solve(True)
solve(False)

import numpy as np
import sys

with open(sys.argv[1]) as f:
    contents = f.read().strip().splitlines()

def area(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

DIR = {'R': 1j, 'L': -1j, 'U': -1, 'D': 1}
DIR2 = [1j, 1, -1j, -1]
def solve(p2):
    curr = complex(0,0)
    perimeter = 0
    xs = []
    ys = []
    for line in contents:
        dir, num, rest = line.split()
        if not p2:
            num = int(num)
            dir = DIR[dir]
        else:
            dir = DIR2[int(rest[-2])]
            num = int(rest[2:-2], 16)

        curr = curr + dir*num
        perimeter += num
        xs.append(int(curr.real))
        ys.append(int(curr.imag))

    A = area(xs, ys)
    I = A + 1 - perimeter // 2
    print(int(I+perimeter))

solve(False)
solve(True)

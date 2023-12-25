import sys
import re
import itertools
from collections import namedtuple
import z3

Hailstone = namedtuple('Hailstone', ['x', 'y', 'z', 'dx', 'dy', 'dz', 'a', 'b', 'c'])

with open(sys.argv[1]) as f:
    contents = f.read().strip().splitlines()
    MIN = 200000000000000
    MAX = 400000000000000

ib = lambda x: MIN < x < MAX

def intersection(l1, l2):
    if l1.a == l2.a:
        if l1.c == l2.c:
            return MIN+1, MIN+1
        return 0,0

    return -(l1.b*l2.c - l2.b*l1.c)/(l1.a*l2.b - l2.a*l1.b), -(l1.c*l2.a - l2.c*l1.a)/(l1.a*l2.b - l2.a*l1.b)

lines = []
for line in contents:
    x, y, z, dx, dy, dz = list(map(int, re.findall(r"-?\d+", line)))
    slope = dy / dx
    lines.append(Hailstone(x, y, z, dx, dy, dz, -slope, 1, y - slope * x))

p1 = 0
for l1, l2 in itertools.combinations(lines, 2):
    ipoint = intersection(l1, l2)
    in_bounds = all([ib(c) for c in ipoint])
    in_future = (l1.x < ipoint[0]) == (l1.dx > 0) and (l2.x < ipoint[0]) == (l2.dx > 0)

    if in_bounds and in_future:
        p1 += 1
print(p1)


# P2 - slight cheating with z3
s = z3.Solver()
x, y, z = z3.Int('x'), z3.Int('y'), z3.Int('z')
dx, dy, dz = z3.Int('dx'), z3.Int('dy'), z3.Int('dz')

for i, l in enumerate(lines[:5]):
    t = z3.Int(f't_{i}')
    s.add(t >= 0)
    s.add(x + dx * t == l.x + l.dx * t)
    s.add(y + dy * t == l.y + l.dy * t)
    s.add(z + dz * t == l.z + l.dz * t)

s.check()
m = s.model()
xyz = m.eval(x).as_long(), m.eval(y).as_long(), m.eval(z).as_long()
print(sum(xyz))

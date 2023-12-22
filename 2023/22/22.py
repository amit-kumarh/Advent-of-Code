import sys
import re
from dataclasses import dataclass
import copy

with open(sys.argv[1]) as f:
    contents = f.read().strip().splitlines()

@dataclass()
class Point:
    x: int
    y: int
    z: int

@dataclass()
class Brick:
    start: Point
    end: Point
    id : int

    def lower(self):
        self.start.z -= 1
        self.end.z -= 1

    def zs(self):
        return sorted([self.start.z, self.end.z])

    def twod_overlap(self, other):
        first = max(self.start.x, other.start.x), min(self.end.x, other.end.x)
        second = max(self.start.y, other.start.y), min(self.end.y, other.end.y)
        return first[0] <= first[1] and second[0] <= second[1]

    def touching_above(self, other):
        return other.zs()[0] == self.zs()[1]+1 and self.twod_overlap(other)

    def touching_below(self, other):
        return other.zs()[1] == self.zs()[0]-1 and self.twod_overlap(other)

    def __hash__(self) -> int:
        return hash(id)

def get_bricks():
    bricks = []
    for i, line in enumerate(contents):
        x1, y1, z1, x2, y2, z2, = list(map(int, re.findall(r'\d+', line)))
        b = Brick(Point(x1, y1, z1), Point(x2, y2, z2), i)
        bricks.append(b)
    bricks.sort(key=lambda x: min(x.start.z, x.end.z))
    return bricks

def fall1(bricks):
    fallen = set()
    for b in bricks:
        if b.zs()[0] != 1:
            for below in bricks:
                if b.touching_below(below):
                    break
            else:
                b.lower()
                fallen.add(b)

    return fallen

bricks = get_bricks()
while len(fall1(bricks)) > 0: pass

p1 = p2 = 0
for i, b in enumerate(bricks):
    print(f"Progress: {(i / len(bricks)) * 100}%")
    minusb = [x for x in copy.deepcopy(bricks) if x != b]
    fallen = set()
    first = True
    while len(new := fall1(minusb)) > 0:
        fallen.update(new)
        first = False
    if first: p1 += 1
    p2 += len(fallen)

print(p1)
print(p2)

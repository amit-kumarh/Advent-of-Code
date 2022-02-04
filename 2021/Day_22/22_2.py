import re
from collections import defaultdict
import copy

class Cube:
    def __init__(self, X, Y, Z, state=1):
        self.X = X
        self.x0, self.x1 = self.X

        self.Y = Y
        self.y0, self.y1 = self.Y

        self.Z = Z
        self.z0, self.z1 = self.Z

        self.state = state
    
    def get_size(self):
        return (self.x1+1-self.x0) * (self.y1+1-self.y0) * (self.z1+1-self.z0) * self.state

def get_input():
    with open('input', 'r') as file:
        contents = file.read().split('\n')

        output = []
        inst = []
        for line in contents:
            inst += re.findall('(^o[nf]f?)', line)
            output.append([int(i) for i in re.findall('-?\d+', line)])

    
    return output, inst
        
def overlaps(cube, cubes):
    x0, x1, y0, y1, z0, z1 = cube
    for otherCube in cubes:
        if ((x0, x1) == otherCube.X and (y0, y1) == otherCube.Y and (z0, z1) == otherCube.Z):
            continue
        ix0, ix1, iy0, iy1, iz0, iz1 = 0,0,0,0,0,0
        rx0, rx1 = otherCube.X
        ry0, ry1 = otherCube.Y
        rz0, rz1 = otherCube.Z
        ix0 = max(x0, rx0)
        ix1 = min(x1, rx1)
        iy0 = max(y0, ry0)
        iy1 = min(y1, ry1)
        iz0 = max(z0, rz0)
        iz1 = min(z1, rz1)

        if ix0 <= ix1 and iy0 <= iy1 and iz0 <= iz1:
            yield Cube((ix0, ix1), (iy0, iy1), (iz0, iz1), -1 if otherCube.state == 1 else 1)

contents, inst = get_input()
regions = []

for i, line in enumerate(contents):
    x0, x1, y0, y1, z0, z1 = line
    if inst[i] == 'on':
        mode = 1
    elif inst[i] == 'off':
        mode = -1
    else:
        raise Exception('Unknown instruction')
    

    regions.append(Cube((x0, x1), (y0, y1), (z0, z1), mode))

update = []

for cube in regions:
    x0, x1 = cube.X
    y0, y1 = cube.Y
    z0, z1 = cube.Z

    for intersection in overlaps((x0, x1, y0, y1, z0, z1), update.copy()):
        update.append(intersection)
    
    if cube.state == 1: update.append(cube)


    
    

ans = 0
for cube in update:
    ans += cube.get_size()

print(ans)

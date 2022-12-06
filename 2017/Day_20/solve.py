import re
import numpy as np
from collections import defaultdict

with open('input', 'r') as f:
    contents = f.read().strip().split('\n')

particles = []
for line in contents:
    toadd = []
    for sec in re.findall(r'<([\d,-]+)>', line):
        toadd.append([int(i) for i in sec.split(',')])
    particles.append(toadd)

def pt1():
    minAccel = lambda x: sum(abs(i) for i in x[2])
    return particles.index(min(particles, key=minAccel))

def update(particle):
    for i in range(3):
        particle[1][i] += particle[2][i]
        particle[0][i] += particle[1][i]
    return particle
    
def pt2():
    for _ in range(100):
        cnt = defaultdict(int)
        toRemove = []
        for idx, p in enumerate(particles):
            particles[idx] = update(p)
            cnt[tuple(p[0])] += 1

        for p in particles:
            if cnt[tuple(p[0])] > 1:
                toRemove.append(p)

        for p in toRemove:
            particles.remove(p)

        print(len(particles))


print(pt1())
print(pt2())

import sys
import numpy as np

with open(sys.argv[1]) as f:
    c = f.read().strip().splitlines()

p1 = p2 = 0
for line in c:
    nums = list(map(int, line.split()))

    diffs = [nums]
    while set(diffs[-1]) != { 0 }:
        diffs.append(list(np.diff(diffs[-1])))

    diffs = list(reversed(diffs))
    for i, d in enumerate(diffs):
        if i == 0: continue
        d.append(d[-1] + diffs[i-1][-1])
        d.insert(0, d[0] - diffs[i-1][0])

    p1 += diffs[-1][-1]
    p2 += diffs[-1][0]

print(p1)
print(p2)

import sys
import math
import re
import itertools

with open(sys.argv[1], "r") as f:
    contents = f.read().splitlines()

qualities = []
for line in contents:
    qualities.append(tuple(int(x) for x in re.findall(r"-?\d+", line.split(": ")[1])))

def score(cookie):
    sums = [0, 0, 0, 0, 0]
    for i, ing in enumerate(cookie):
        for j in range(5):
            sums[j] += qualities[i][j] * ing

    return (math.prod(max(0, x) for x in sums[:-1]), sums[-1])

p1 = p2 = 0
for comb in itertools.combinations_with_replacement([1, 2, 3, 4], 100):
    cookie = (comb.count(1), comb.count(2), comb.count(3), comb.count(4))
    cookie_score, cals = score(cookie)
    p1 = max(p1, cookie_score)
    p2 = max(p2, cookie_score) if cals == 500 else p2
print(p1, p2, sep='\n')



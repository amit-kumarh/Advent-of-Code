import sys
import re
from math import prod

with open(sys.argv[1]) as f:
    c = f.read().strip()

p1 = p2 = 0
for line in c.split('\n'):
    id = re.findall(r"Game (\d+):", line)[0]
    p1 += int(id) if all([int(n) <= lim for col, lim in [("red", 12), ("green", 13), ("blue", 14)] for n in re.findall(rf"(\d+) {col}", line)]) else 0
    p2 += prod(max(int(match) for match in re.findall(rf"(\d+) {color}", line)) for color in ["red", "green", "blue"])
print(p1, p2)

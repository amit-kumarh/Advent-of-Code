import sys
import math
import collections

with open(sys.argv[1]) as f:
    c = [l.strip() for l in f.read().split("\n")]

DIR = [complex(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2)]
grid = {
    complex(row, col): char
    for row, line in enumerate(c)
    for col, char in enumerate(line)
}

p1 = 0
stars = collections.defaultdict(list)
for row in range(len(c)):
    num, part, adj_stars = 0, False, set()
    for col in range(len(c[row]) + 1):
        char = grid.get(coord := complex(row, col), ".")
        if char.isdigit():
            num = num * 10 + int(char)
            for d in DIR:
                char = grid.get(coord + d, ".")
                part |=  char not in "1234567890."
                if char == "*":
                    adj_stars.add(coord+d)
        else:
            if num and part:
                p1 += num
                for s in adj_stars:
                    stars[s].append(num)
            num, part, adj_stars = 0, False, set()

print(p1)
p2 = sum(math.prod(i for i in l) for l in stars.values() if len(l) == 2)
print(p2)


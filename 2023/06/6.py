import sys
import re

with open(sys.argv[1]) as f:
    c = f.read().strip().splitlines()

times = re.findall(r"\d+", c[0])
distances = re.findall(r"\d+", c[1])
times.append(''.join(times))
distances.append(''.join(distances))

p1, p2 = 1, 0
for i, (time, distance) in enumerate(zip(times, distances)):
    time, distance = int(time), int(distance)
    ways = 0
    for j in range(time):
        final = (time - j) * (time - (time - j))
        if final > distance:
            ways += 1

    if i != len(times) - 1:
        p1 *= ways
    else:
        p2 = ways

print(p1)
print(p2)

import sys
import re
from dataclasses import dataclass

with open(sys.argv[1], "r") as f:
    contents = f.read().splitlines()


@dataclass
class Deer:
    speed: int
    sprint: int
    rest: int
    cnt: int = 0
    running: bool = True
    distance: int = 0
    points: int = 0


deers = []
for line in contents:
    nums = [int(x) for x in re.findall(r"\d+", line)][:2]
    deers.append(Deer(nums[0], nums[1], nums[2]))
    deers[-1].cnt = nums[1]

for _ in range(2503):
    for deer in deers:
        if deer.running:
            deer.distance += deer.speed
            deer.cnt -= 1
        else:
            deer.cnt -= 1

        if deer.cnt == 0:
            deer.running = not deer.running
            deer.cnt = deer.sprint if deer.running else deer.rest

    max(deers, key=lambda x: x.distance).points += 1

print(max([deer.distance for deer in deers]))
print(max([deer.points for deer in deers]))

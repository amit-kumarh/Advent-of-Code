import sys
import re
import collections

with open(sys.argv[1], "r") as f:
    contents = f.read().splitlines()

grid = collections.defaultdict(int)
p1 = p2 = 0
for line in contents:
    nums = list(map(int, re.findall(r'\d+', line)))
    for i in range(nums[0], nums[2]+1):
        for j in range(nums[1], nums[3]+1):
            match re.findall(r'turn off|toggle|turn on', line)[0]:
                case 'turn off': grid[(i, j)] = max(0, grid[(i, j)] - 1)
                case 'turn on': grid[(i, j)] += 1
                case 'toggle': grid[(i, j)] += 2

print(sum(x>0 for x in grid.values()))
print(sum(grid.values()))


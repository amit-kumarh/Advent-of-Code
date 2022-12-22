import re
from collections import defaultdict
from itertools import accumulate

with open('input', 'r') as file:
    contents = file.read().strip().split('\n')

path = []
sizes = defaultdict(int)
for line in contents:
    if line.startswith('$ cd'):
        if (dir := line[5:]) == '..':
            path.pop()
        else:
            path.append(dir)
    elif (nums := re.findall(r'\d+', line)):
        for p in accumulate(path):
            sizes[p] += int(nums[0])

print(sum(i for i in sizes.values() if i < 100000))
print(min(i for i in sizes.values() if i > sizes['/'] - 40000000))

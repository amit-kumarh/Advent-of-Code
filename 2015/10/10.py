import sys
from itertools import groupby

with open(sys.argv[1], 'r') as f:
    start = f.read().strip()

curr = start
for i in range(50):
    curr = ''.join(f'{len(list(g))}{k}' for k, g in groupby(curr))
    if i == 39:
        print(len(curr))
print(len(curr))
    

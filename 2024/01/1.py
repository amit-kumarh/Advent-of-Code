import sys
from collections import Counter

with open(sys.argv[1]) as f:
    contents = f.read().strip().splitlines()

l1, l2 = zip(*[map(int, line.split()) for line in contents])
cnt = Counter(l2)
p1 = sum(abs(x-y) for x, y in zip(sorted(l1), sorted(l2)))
p2 = sum(x*cnt[x] for x in set(l1))
print(p1, p2, sep='\n')

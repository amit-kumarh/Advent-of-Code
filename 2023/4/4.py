import sys
import re
import collections

with open(sys.argv[1]) as f:
    c = f.read().strip().split('\n')

p1, cards = 0, collections.defaultdict(int)
for i, line in enumerate(c):
    cards[i] += 1
    elf, me = [set(m.split()) for m in re.findall(r"^.+: (.*) \| (.*)", line)[0]]
    if len(inter := elf.intersection(me)) > 0:
        p1 += 2 ** (len(inter)-1)

    for j in range(len(inter)):
        cards[i+j+1] += cards[i]

print(p1)
print(sum(cards.values()))

import sys
from itertools import cycle

with open(sys.argv[1], 'r') as f:
    contents = list(f.read())

curr = complex(0, 0)
robo = complex(0, 0)
seen = {curr}
c = cycle(["curr", "robo"])
for i in contents:
    r = next(c)
    match i:
        case '^': 
            locals()[r] -= 1
            seen.add(locals()[r])
        case 'v':
            locals()[r] += 1
            seen.add(locals()[r])
        case '>':
            locals()[r] += 1j
            seen.add(locals()[r])
        case '<':
            locals()[r] -= 1j
            seen.add(locals()[r])
print(len(seen))



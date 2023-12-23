import sys
import re

with open(sys.argv[1], 'r') as f:
    contents = f.read().splitlines()

p1 = p2 = 0
for line in contents:
    l, w, h = [int(x) for x in re.findall(r'\d+', line)]
    p1 +=  2*(s1 := l*w) + 2*(s2 := w*h) + 2*(s3 := h*l) + min([s1, s2, s3])
    p2 += l*w*h + min([2*(l+w), 2*(w+h), 2*(l+h)])

print(p1)
print(p2)

import sys
import re

with open(sys.argv[1]) as f:
    contents = f.read()

inst = re.finditer(r'mul\((\d\d?\d?),(\d\d?\d?)\)|do\(\)|don\'t\(\)', contents)
p1 = p2 = 0
on = True
for i in inst:
    if i[0].startswith( "mul"):
        p1 += int(i[1]) * int(i[2])
        p2 += int(i[1]) * int(i[2]) * on
    elif i[0].startswith("don't"):
        on = False
    elif i[0].startswith("do"):
        on = True

print(p1, p2, sep='\n')

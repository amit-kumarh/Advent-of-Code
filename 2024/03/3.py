import sys
import re

with open(sys.argv[1]) as f:
    contents = f.read()

inst = re.findall(r'mul\(\d\d?\d?,\d\d?\d?\)|do\(\)|don\'t\(\)', contents)
p1 = p2 = 0
on = True
for i in inst:
    if i.startswith( "mul"):
        nums = [int(x) for x in re.findall(r'\d+', i)]
        p1 += nums[0] * nums[1]
        p2 += nums[0] * nums[1] * on
    elif i.startswith("don't"):
        on = False
    elif i.startswith("do"):
        on = True

print(p1, p2, sep='\n')

import sys
import re

with open(sys.argv[1], "r") as f:
    contents = f.read().splitlines()

p1 = p2 = 0
for line in contents:
    if (
        len(re.findall(r"a|e|i|o|u", line)) >= 3
        and all(x not in line for x in ["ab", "cd", "pq", "xy"])
        and len(re.findall(r"(.)\1{1,}", line)) >= 1
    ):
        p1 += 1
    if (
        len(re.findall(r"([a-z]{2}).*\1", line)) >= 1
        and len(re.findall(r"([a-z]).\1", line)) >= 1
    ):
        p2 += 1

print(p1)
print(p2)

import sys
import re
import itertools

with open(sys.argv[1]) as f:
    contents = f.read().strip().splitlines()

def solve(p2):
    total = 0
    ops = ['+', '*', '||'] if p2 else ['+', '*']
    for line in contents:
        nums = list(map(int, re.findall(r'-?\d+', line)))
        res = nums[0]
        parts = nums[1:]

        for perm in itertools.product(ops, repeat=len(parts)-1):
            eq = parts[0]
            for i, part in enumerate(parts[1:]):
                match perm[i]:
                    case '+': eq += part
                    case '*': eq *= part
                    case '||': eq = int(str(eq) + str(part))

            if eq == res:
                total += res
                break

    return total

print(solve(False), solve(True), sep='\n')

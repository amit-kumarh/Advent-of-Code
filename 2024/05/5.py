import sys
import functools

with open(sys.argv[1]) as f:
    contents = f.read().strip()

rules_str, cases = contents.split('\n\n')
rules = set(tuple(int(x) for x in line.split('|')) for line in rules_str.split('\n'))

def cmp(a, b):
    if (a, b) in rules: return -1
    elif (b, a): return 1
    else: assert False

p1 = p2 = 0
for c in cases.splitlines():
    nums = [int(x) for x in c.split(',')]
    if (sorted_nums := sorted(nums, key=functools.cmp_to_key(cmp))) == nums:
        p1 += nums[len(nums) // 2]
    else:
        p2 += sorted_nums[len(sorted_nums) // 2]

print(p1, p2, sep='\n')

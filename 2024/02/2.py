import sys

with open(sys.argv[1]) as f:
    contents = [[int(x) for x in line.split()] for line in f.read().strip().splitlines()]

def safe(nums):
    if nums not in [sorted(nums), sorted(nums, reverse=True)]:
        return False

    for i, n in enumerate(nums):
        if i == 0:
            continue
        diff = abs(n - nums[i - 1])
        if diff < 1 or diff > 3:
            break
    else:
        return True

    return False

def solve(p2):
    ans = 0
    for nums in contents:
        if safe(nums):
            ans += 1
            continue

        if p2:
            for i in range(0, len(nums)):
                if safe(nums[:i] + nums[i + 1:]):
                    ans += 1
                    break
    return ans

print(solve(False))
print(solve(True))

import sys

with open(sys.argv[1]) as f:
    contents = f.read().strip().split('\n\n')
    patterns = [p.splitlines() for p in contents]

def find_reflection(pattern, part):
    CMP = 1 if part == 2 else 0
    for i, _ in enumerate(pattern):
        if i == 0: continue
        count = 0
        for a, b in zip(list(reversed(pattern[:i])), pattern[i:]):
            count += sum(ca != cb for ca, cb in zip(a, b))

        if count == CMP:
            return i
    return 0

def solve(part):
    ans = 0
    for pattern in patterns:
        ans += 100 * find_reflection(pattern, part)
        ans += find_reflection(list(zip(*pattern)), part)

    print(ans)

solve(1)
solve(2)

import sys

if len(sys.argv) < 2:
    path = "20.in"
else:
    path = sys.argv[1]
with open(path) as f:
    c = f.read().strip()

digits = [int(i) * 811589153 for i in c.split('\n')]
L = len(digits)
indices = list(range(L))

for _ in range(10):
    for i in range(L):
        indices.pop(pos := indices.index(i))
        indices.insert((pos + digits[i]) % len(indices), i)
        ans = [digits[i] for i in indices]

zero = indices.index(digits.index(0))
ans = sum(digits[indices[(zero+p)%L]] for p in [1000, 2000, 3000])
print(ans)





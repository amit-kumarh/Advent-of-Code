import sys
import itertools

with open(sys.argv[1]) as f:
    contents = f.read().strip().splitlines()

galaxies = set(
    complex(i, j)
    for i, line in enumerate(contents)
    for j, char in enumerate(line)
    if char == "#"
)
blank_rows = set(i for i, x in enumerate(contents) if '#' not in x)
blank_cols = set(i for i, x in enumerate(list(zip(*contents))) if '#' not in x)

p1 = p2 = 0
for a, b in itertools.combinations(galaxies, 2):
    step = 1 if a.real < b.real else -1
    for i in range(int(a.real), int(b.real), step):
        p1 += 2 if i in blank_rows else 1
        p2 += 1_000_000 if i in blank_rows else 1

    step = 1 if a.imag < b.imag else -1
    for i in range(int(a.imag), int(b.imag), step):
        p1 += 2 if i in blank_cols else 1
        p2 += 1_000_000 if i in blank_cols else 1

print(p1)
print(p2)

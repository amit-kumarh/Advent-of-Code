import sys
import itertools
from math import prod

with open(sys.argv[1]) as f:
    c = [l.strip() for l in f.read().strip().split('\n')]

DIR = list(itertools.permutations([-1, 0, 1], 2) ) + [(1, 1), (-1, -1)]
def check_char(x, y):
    for dx, dy in DIR:
        row = x + dx
        col = y + dy
        if not (0 <= row < len(c) and 0 <= col < len(c[0])):
            continue

        if c[row][col] != "." and not c[row][col].isdigit():
            return True

    return False

p1 = j = 0
for (i, _) in enumerate(c):
    j = 0
    while j < len(c[0]):
        num = ""
        good = False
        while j < len(c[0]) and c[i][j].isdigit():
            if check_char(i, j):
                good = True
            num += c[i][j]
            j += 1

        if num != "" and good:
            p1 += int(num)

        j += 1

print(p1)

p2 = j = 0
for (i, _) in enumerate(c):
    j = 0
    while j < len(c[0]):
        if c[i][j] == '*':
            nums = set()
            for dx, dy in DIR:
                row = i + dx
                col = j + dy
                if not (0 <= row < len(c) and 0 <= col < len(c[0])):
                    continue

                if c[row][col].isdigit():
                    numr = ""
                    while col < len(c[0]) and c[row][col].isdigit():
                        numr += c[row][col]
                        col += 1

                    numl = ""
                    row = i + dx
                    col = j + dy - 1
                    while col < len(c[0]) and c[row][col].isdigit():
                        numl += c[row][col]
                        col -= 1

                    num = ''.join(list(reversed(numl))) + numr
                    if num != "":
                        nums.add(int(num))

            if len(nums) == 2:
                p2 += prod(nums)

        j += 1

print(p2)


        

import sys
import re

with open(sys.argv[1], "r") as f:
    contents = f.read().splitlines()

ANS = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

for i, line in enumerate(contents):
    match = [(i, int(j)) for i, j in re.findall(r"(\w+): (\d+)", line)]
    for m in match:
        match m[0]:
            case "cats" | "trees": correct = m[1] > ANS[m[0]]
            case "pomeranians" | "goldfish": correct = m[1] < ANS[m[0]]
            case _: correct = m[1] == ANS[m[0]]
        if not correct:
            break
    else:
        print(i+1)
        


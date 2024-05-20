import sys

with open(sys.argv[1], "r") as f:
    contents = f.read().splitlines()

solve = lambda p1: abs(sum((len(eval(line)) if p1 else len(line) + line.count("\\") + line.count("\"") + 2) - len(line) for line in contents))
print(solve(True), solve(False), sep="\n")


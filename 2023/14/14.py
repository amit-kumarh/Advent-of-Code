import sys

with open(sys.argv[1]) as f:
    contents = list(list(x) for x in f.read().strip().splitlines())

def tilt(grid):
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == 'O':
                curr = i
                while curr >= 1 and grid[curr-1][j] == '.':
                    grid[curr][j], grid[curr-1][j] = '.', 'O'
                    curr -= 1
    return grid


rot90ccw = lambda x: list(list(x) for x in zip(*reversed(x)))
rot90cw = lambda x: list(list(x) for x in zip(*x))[::-1]
grid, seen, rep = rot90cw(contents), {}, 0
while rep < (REPS := 1000000000):
    if str(grid) in seen:
        cycle = rep - seen[str(grid)]
        rep += (REPS - rep) // cycle * cycle
    seen[str(grid)] = rep

    for _ in range(4): grid = tilt(rot90ccw(grid))
    rep += 1
grid = rot90ccw(grid)

p1 = sum(line.count('O') * (len(contents) - i) for i, line in enumerate(tilt(contents)))
p2 = sum(line.count('O') * (len(contents) - i) for i, line in enumerate(grid))
print(p1)
print(p2)

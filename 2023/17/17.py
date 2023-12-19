import sys
import heapq

# jerryrigging a state class bc heapq doesn't like complex numbers...
class State:
	def __init__(self, dist, loc, dir, cdir):
		self.dist = dist
		self.loc = loc
		self.dir = dir
		self.cdir = cdir
		self.key = (self.loc, self.dir, self.cdir)

	def __lt__(self, other):
		return (self.dist, self.cdir)<(other.dist, other.cdir)

with open(sys.argv[1]) as f:
    contents = f.read().strip().splitlines()
    grid = {
        complex(i, j): int(char)
        for i, line in enumerate(contents)
        for j, char in enumerate(line)
    }

def solve(p2):
    start = complex(0, 0)
    target = complex(len(contents)-1, len(contents[0])-1)
    # dist, curr, dir, cdir
    q = [State(grid[start], start, 0, 0)]
    seen = {}
    while q:
        state = heapq.heappop(q)
        dist, curr, dir, cdir = state.dist, state.loc, state.dir, state.cdir
        if curr == target and (cdir >= 4 or not p2):
            return dist

        if state.key in seen:
            continue
        seen[state.key] = dist

        for d in {1, -1, 1j, -1j} - {-dir}:
            new_cdir = 1 if d != dir else cdir+1
            dir_valid = new_cdir <= 10 and (d == dir or cdir >= 4 or cdir == 0)

            if (next := curr+d) in grid and (dir_valid if p2 else new_cdir <= 3):
                heapq.heappush(q, State(dist + grid[curr], next, d, new_cdir))

print(solve(False))
print(solve(True))

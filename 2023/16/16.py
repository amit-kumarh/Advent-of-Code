import collections
import sys

with open(sys.argv[1]) as f:
    contents = f.read().strip().splitlines()
    grid = {complex(i, j): char for i, line in enumerate(contents) for j, char in enumerate(line)}

def new_beams(pos, dir):
    newbeams = []
    match grid[pos]:
        case '.': 
            newbeams.append((pos + dir, dir))
        case '/':
            match dir:
                case 1j | -1j: newdir = -dir.imag
                case 1 | -1: newdir = -dir.real * 1j
                case _: assert False
            newbeams.append((pos + newdir, newdir))
        case '\\':
            match dir:
                case 1j | -1j: newdir = dir.imag
                case 1 | -1: newdir = dir.real * 1j
                case _: assert False
            newbeams.append((pos + newdir, newdir))
        case '-':
            match dir:
                case 1j | -1j: newbeams.append((pos+dir, dir))
                case 1 | -1: 
                    newbeams.append((pos + 1j, 1j))
                    newbeams.append((pos - 1j, -1j))
                case _: assert False
        case '|':
            match dir:
                case 1 | -1: newbeams.append((pos+dir, dir))
                case 1j | -1j: 
                    newbeams.append((pos + 1, 1))
                    newbeams.append((pos - 1, -1))
                case _: assert False
        case _:
            assert False
    return newbeams

def run(start, dir):
    beams = collections.deque()
    beams.append((start, dir))
    seen = collections.defaultdict(set)
    while beams:
        pos, dir = beams.popleft()
        seen[pos].add(dir)

        for pos, dir in new_beams(pos, dir):
            if pos in grid and dir not in seen[pos]:
                beams.append((pos, dir))
    return len(seen)

ans = 0
for i, _ in enumerate(contents):
    ans = max(ans, run(complex(i, 0), 1j))
    ans = max(ans, run(complex(i, len(contents[0])-1), -1j))
for j, _ in enumerate(contents[0]):
    ans = max(ans, run(complex(0, j), 1))
    ans = max(ans, run(complex(len(contents)-1, j), -1))

print(run(complex(0, 0), 1j))
print(ans)

import sys
import functools

with open(sys.argv[1]) as f:
    contents = f.read().strip().splitlines()

@functools.cache
def solve(s, g):
    s = s.lstrip('.') # advance to first "#"

    # if we're at the end of the row, no more remaining groups
    if s == '':
        return int(g == ())

    # if we're at the end of the groups, no more remaining '#'
    if g == ():
        return int(s.find('#') == -1)

    if s[0] == '#':
        # these aren't the group(s) you're looking for
        if len(s) < g[0] or '.' in s[:g[0]]: # not enough room for the next group
            return 0
        if len(s) == g[0]: # exactly enough room for the next group
            return  int(len(g) == 1)
        if s[g[0]] == '#': # group is too long
            return 0
        
        # move along
        return solve(s[g[0]+1:], g[1:])

    # at a '?', so we branch
    return solve('#'+s[1:], g) + solve('.'+s[1:], g)

lines = [line.split() for line in contents]
p1 = [(spring, tuple(map(int, groups.split(',')))) for spring, groups in lines]
p2 = [(((spring + '?') * 5)[:-1], groups * 5) for spring, groups in p1]
print(sum(map(lambda row: solve(*row), p1)))
print(sum(map(lambda row: solve(*row), p2)))

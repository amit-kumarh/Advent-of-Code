import sys
import re

with open(sys.argv[1]) as f:
    c = f.read().strip()

secs = c.split('\n\n')
init, rest = [int(i) for i in re.findall(r"\d+", secs[0])], secs[1:]
maps = []
for map in rest:
    r = []
    for line in map.split('\n')[1:]:
        r.append(tuple(int(i) for i in line.split()))
    maps.append(r)

## Part 1
res = []
for i in init:
    curr = i
    for m in maps:
        for d, s, l in m:
            if 0 <= curr-s < l:
                curr = d + (curr-s)
                break
    res.append(curr)
print(min(res))

# Part 2
res = []
for i in range(0, len(init), 2):
    ranges = [(init[i], init[i] + init[i+1])]
    for m in maps:
        new_ranges = []
        while ranges:
            start, end = ranges.pop()
            for dest, src, length in m:
                before = (start, min(end, src))
                inter = (max(start, src), min(end, src+length))
                after = (max(src+length, start), end)
                if inter [0] < inter [1]: 
                    new_ranges.append((inter[0] - src + dest, inter[1] - src + dest))
                    if before [0] < before [1]: ranges.append(before)
                    if after [0] < after [1]: ranges.append(after)
                    break
            else:
                new_ranges.append((start, end))

        new_ranges.extend(ranges)
        ranges = new_ranges

    res.append(min(x[0] for x in ranges))

print(min(res))

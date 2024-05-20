import sys

with open(sys.argv[1], "r") as f:
    contents = f.read().splitlines()


def solve(b=None):
    wires = dict()
    if b is not None:
        wires["b"] = b

    while 'a' not in wires:
        for line in contents:
            source, dest = line.split(' -> ')
            if dest in wires:
                continue
            source = source.split()
            try:
                if len(source) == 1:
                    wires[dest] = wires[v] if (v := source[0]) in wires else int(v)
                elif len(source) == 2:
                    val = wires[v] if (v := source[1]) in wires else int(v)
                    wires[dest] = ~val + (1 << 16)
                elif len(source) == 3:
                    left = wires[l] if (l := source[0]) in wires else int(l)
                    right = wires[r] if (r := source[2]) in wires else int(r)
                    match source[1]:
                        case 'AND': wires[dest] = left & right
                        case 'OR': wires[dest] = left | right
                        case 'LSHIFT': wires[dest] = left << right
                        case 'RSHIFT': wires[dest] = left >> right
                else:
                    assert False
            except ValueError:
                pass

    return wires["a"]

print(p1 := solve())
print(solve(p1))

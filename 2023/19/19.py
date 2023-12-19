import sys
import re
import collections

with open(sys.argv[1]) as f:
    contents = f.read().strip()
    workflows, parts = contents.split('\n\n')

def make_lambda(op, cmp):
    match op:
        case '<': return lambda x: x < cmp
        case '>': return  lambda x: x > cmp
        case _: assert False

rules = collections.defaultdict(list)
for line in workflows.splitlines():
    name, rest = line.split('{') #}
    inst = rest[:-1].split(',')
    for i in inst:
        if ':' not in i:
            xmas, func, goto = None, lambda: True, i
        else:
            xmas, op, cmp, goto = re.findall(r"([a-z]+)([<>])(-?\d+):(.*)", i)[0]
            func = make_lambda(op, int(cmp))
        rules[name].append((xmas, func, goto))

def solve_p1(state, rule):
    for xmas, func, goto in rules[rule]:
        if func(state[xmas]) if xmas else True:
            match goto:
                case 'A': return sum(state.values())
                case 'R': return 0
                case _: return solve_p1(state, goto)
def p2(state):
    ans = 0
    q = [state]
    while q:
        x, m, a, s, rule = q.pop()
        if rule == 'A':
            ans += len(x) * len(m) * len(a) * len(s)
            continue
        elif rule == 'R':
            continue

        for r in rules[rule]:
            xmas, func, goto = r
            match xmas:
                case 'x':
                    if new := tuple(filter(func, x)):
                        q.append((new, m, a, s, goto))
                    x = tuple(filter(lambda n: not func(n), x))
                case 'm':
                    if new := tuple(filter(func, m)):
                        q.append((x, new, a, s, goto))
                    m = tuple(filter(lambda n: not func(n), m))
                case 'a':
                    if new := tuple(filter(func, a)):
                        q.append((x, m, new, s, goto))
                    a = tuple(filter(lambda n: not func(n), a))
                case 's':
                    if new := tuple(filter(func, s)):
                        q.append((x, m, a, new, goto))
                    s = tuple(filter(lambda n: not func(n), s))
                case None:
                    q.append((x, m, a, s, goto))
    print(ans)

p1 = 0
for line in parts.splitlines():
    x, m, a, s = list(map(int, re.findall(r'-?\d+', line)))
    state = {'x': x, 'm': m, 'a': a, 's': s}
    p1 += solve_p1(state, 'in')
print(p1)

p2((range(1, 4001), range(1, 4001), range(1, 4001), range(1, 4001), 'in'))

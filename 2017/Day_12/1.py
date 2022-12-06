import re, collections
with open('input', 'r') as f:
    contents = f.read().strip().split('\n')

contents = [line.split(' <-> ') for line in contents]
prog = {item[0]: set(re.findall(r'\d+', item[1])) for item in contents}

def bfs():
    seen = set()
    queue = {'0'}

    while queue:
        i = queue.pop()
        seen.add(i)
        queue.update(prog[i] - seen)

    print(len(seen))

def pt2():
    rem = set(prog.keys())
    groups = 0

    while prog:
        queue = {next(iter(prog))}
        seen = set()

        while queue:
            i = queue.pop()
            seen.add(i)
            queue.update(prog[i] - seen)
        groups += 1
        for item in seen:
            del prog[item]
    return groups


bfs() 
print(pt2())

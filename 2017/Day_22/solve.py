with open('input', 'r') as f:
    contents = f.read().strip().split('\n')

init_infected = set()
for r, row in enumerate(contents):
    for c, cell in enumerate(row):
        if cell == '#':
            init_infected.add((c,r))

pos = {1: (0,-1), 2: (1,0), 3: (0,1), 4: (-1,0)}

def pt1():
    dir = 1
    infected = init_infected.copy()
    curr = (len(contents)//2, len(contents[0])//2)
    cnt = 0
    for _ in range(10000):
        if curr in infected:
            dir = 1 if dir == 4 else dir + 1
            infected.remove(curr)
            print('infected', dir, curr, pos[dir])
            curr = tuple(sum(x) for x in zip(curr, pos[dir]))
        else:
            cnt += 1
            dir = 4 if dir == 1 else dir - 1
            infected.add(curr)
            print('clean', dir, curr, pos[dir])
            curr = tuple(sum(x) for x in zip(curr, pos[dir]))
    return cnt

def pt2():
    pass

print(pt1())
print(pt2())

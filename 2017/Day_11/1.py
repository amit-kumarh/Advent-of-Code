with open('input', 'r') as f: contents = f.read().strip().split(',')

def run():
    locs = {'n': (0,1), 'ne': (.5, .5), 'nw': (-.5, .5),
            's': (0,-1), 'sw': (-.5, -.5), 'se': (.5, -.5)}
    x = y = ans = 0
    for inst in contents:
        x, y = x + locs[inst][0], y + locs[inst][1]
        ans = max(ans, abs(x)+abs(y))
    return abs(x) + abs(y), ans

print(run())

#start = perf_counter()
import collections
def get_contents():
    with open('input', 'r') as f:
        contents = f.read().strip().split('\t')
        contents = [int(i) for i in contents]
    return contents

contents = get_contents()
contents = [0, 2, 7, 0]
print(contents)
states = collections.defaultdict(int)
step = 0
def redistribute(contents, imax, val):
    pointer = (imax + 1) % len(contents)
    contents[imax] = 0
    while val:
        contents[pointer] += 1
        pointer = (pointer + 1)%len(contents)
        val -= 1

    return contents

while True:
    step += 1
    val, imax = max(contents), contents.index(max(contents))
    
    contents = redistribute(contents, imax, val)

    print(contents, step)
    if states[tuple(contents)] == 2: 
        print(step)
        break
    else:
        states[tuple(contents)] += 1

    if states[tuple(contents)] == 1:
        step = 0

    



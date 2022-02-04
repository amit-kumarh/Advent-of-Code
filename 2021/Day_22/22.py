import re
from collections import defaultdict

def get_input():
    with open('input', 'r') as file:
        contents = file.read().split('\n')

        output = []
        inst = []
        for line in contents:
            inst += re.findall('(^o[nf]f?)', line)
            output.append(re.findall('=(-?[0-9]+)\.\.(-?[-0-9]+)', line))

    
    return output, inst

contents, inst = get_input()
ans = defaultdict(int)

for i, line in enumerate(contents):
    X, Y, Z = line
    if inst[i] == 'on':
        mode = 1
    elif inst[i] == 'off':
        mode = 0
    else:
        raise Exception('Unknown instruction')
    for x in range(int(X[0]), int(X[1])+1):
        for y in range(int(Y[0]), int(Y[1])+1):
            for z in range(int(Z[0]), int(Z[1])+1):
                 ans[(x, y, z)] = mode
    
    print(i)

values = ans.values()
print(sum(values))

                

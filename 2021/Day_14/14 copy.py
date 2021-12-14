from collections import *
import copy

def get_input():
    with open('input', 'r') as file:
        start, inst = file.read().split('\n\n')
        start = str(start)

        inst = inst.strip().split('\n')
        inst = [line.split(' -> ') for line in inst]
    
    return start, inst

X, inst = get_input()


pd = defaultdict(int)
for i in range(len(X)-1):
    pd[(X[i]+X[i+1])] += 1

print(pd)

for step in range(40):
    npd = copy.deepcopy(pd)

    for line in inst:
        prev = (line[0][0] + line[1])
        nex = (line[1] +line[0][1])
        rep = (line[0][0] + line[0][1])
        rep_count = pd[rep]

        npd[prev] += rep_count
        npd[nex] += rep_count
        npd[rep] -= pd[rep]
        
    pd = npd

letters = defaultdict(int)
for i in pd:
    letters[i[0]] += pd[i]
    letters[i[1]] += pd[i]

letters[X[0]] += 1
letters[X[-1]] +=  1
for i in letters:
    letters[i] = letters[i]//2

listLetters = letters.values()    

solution = max(listLetters) - min(listLetters)
print(solution)
                







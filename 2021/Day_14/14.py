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
X = list(X)

for iter in range(10):
    next_x = []
    for i in range(len(X)-1):
        curr = X[i]
        next = X[i+1]
        next_x.append(curr)
        for line in inst:
            if curr + next == line[0]:
                next_x.append(line[1])
    next_x.append(X[-1])
    X = next_x
    print(len(X))



cnt = Counter(X).most_common()

solution = cnt[0][1] - cnt[-1][1]
print(solution)
                







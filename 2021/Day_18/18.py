from collections import *
import copy

def get_input():
    with open('input', 'r') as file:
        contents = file.read().strip().split('\n')

        contents = [list(line) for line in contents]
        for i, line in enumerate(contents):
            for j, char in enumerate(line):
                try:
                    contents[i][j] = int(char)
                except ValueError:
                    continue
        
        contents = [[char for char in line if char != ','] for line in contents]

        return contents

def toString(val):
        valcopy = copy.deepcopy(val)
        for i, line in enumerate(valcopy):
            valcopy[i] = str(line)
        return valcopy
    
contents = get_input()

def simplify(num):
    while True:
        flag = True
        stack = 0
        for i, char in enumerate(num):
            if char == '[':
                stack += 1
                continue
            elif char == ']':
                stack -= 1
                continue
            else:
                if stack > 4:
                    flag = False
                    num = explode(num, i)
                    #print(''.join(toString(num)))
                    #print()
                    break
        if not flag:
            continue

        for i, char in enumerate(num):
            if char == '[':
                stack += 1
                continue
            elif char == ']':
                stack -= 1
                continue
            elif char > 9:
                flag = False
                num = split_snail(num, i)
                #print(''.join(toString(num)))
                #print()
                break

        if flag:
            return num


def explode(num, i):
    pair = (num[i], num[i+1])

    pointer = i-1
    while True:
        if pointer < 0:
            break
        if isinstance(num[pointer], int):
            num[pointer] += pair[0]
            break
        pointer -= 1

    pointer = i+2
    while True:
        if pointer > len(num)-1:
            break
        if isinstance(num[pointer], int):
            num[pointer] += pair[1]
            break
        pointer += 1

    return num[:i-1] + [0] + num[i+3:]


def split_snail(num, i):
    pair = ['[', num[i]//2, num[i]-num[i]//2, ']']
    return num[:i] + pair + num[i+1:]
            
        


ans = contents[0]
for num in contents[1:]:
    newSum = ['['] + ans + num + [']']
    ans = simplify(list(newSum))


def magnitude(num):
    simplify_pair = lambda x, y: 3*x + 2* y

    while True:
        if len(num) == 1:
            return num 
        for i, char in enumerate(num):
            if isinstance(char, int) and isinstance(num[i+1], int):
                newNum = simplify_pair(char, num[i+1])
                num = num[:i-1] + [newNum] + num[i+3:]
                break

def pt2():
    solution = 0
    for a in contents:
        for b in contents:
            if a == b:
                continue
            newSum = ['['] + a + b + [']']
            mag = magnitude(simplify(list(newSum)))

            if mag[0] > solution:
                solution = mag[0]
    
    return solution

print(magnitude(ans))
print(pt2())




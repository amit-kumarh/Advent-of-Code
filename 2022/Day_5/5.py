import re
from collections import deque

def get_input():
    with open('input', 'r') as file:
        contents = file.read().strip().split('\n')
    return contents

l1 = ['J', 'H', 'P', 'M', 'S', 'F', 'N', 'V']
l2 = ['S', 'R', 'L', 'M', 'J', 'D', 'Q']
l3 = ['N', 'Q', 'D', 'H', 'C', 'S', 'W', 'B']
l4 = ['R', 'S', 'C', 'L']
l5 = ['M', 'V', 'T', 'P', 'F', 'B']
l6 = ['T', 'R', 'Q', 'N', 'C']
l7 = ['G', 'V', 'R']
l8 = ['C', 'Z', 'S', 'P', 'D', 'L', 'R']
l9 = ['D', 'S', 'J', 'V', 'G', 'P', 'B', 'F']

def main():
    contents = get_input()
    for line in contents[10:]:
        nums = [int(x) for x in re.findall(r'\d+', line)]
        cnt = nums[0]
        t = f'l{nums[2]}'
        f = f'l{nums[1]}'

    for i in range(cnt):
        globals()[t].append(globals()[f].pop())


    for i in range(1, 10):
        print(globals()[f'l{i}'][-1], end='')

l1 = ['J', 'H', 'P', 'M', 'S', 'F', 'N', 'V']
l2 = ['S', 'R', 'L', 'M', 'J', 'D', 'Q']
l3 = ['N', 'Q', 'D', 'H', 'C', 'S', 'W', 'B']
l4 = ['R', 'S', 'C', 'L']
l5 = ['M', 'V', 'T', 'P', 'F', 'B']
l6 = ['T', 'R', 'Q', 'N', 'C']
l7 = ['G', 'V', 'R']
l8 = ['C', 'Z', 'S', 'P', 'D', 'L', 'R']
l9 = ['D', 'S', 'J', 'V', 'G', 'P', 'B', 'F']

def p2():
    contents = get_input()
    for line in contents[10:]:
        nums = [int(x) for x in re.findall(r'\d+', line)]
        cnt = nums[0]
        t = f'l{nums[2]}'
        f = f'l{nums[1]}'

        globals()[t] += globals()[f][-cnt:]
        globals()[f] = globals()[f][:-cnt]

    print()
    for i in range(1, 10):
        print(globals()[f'l{i}'][-1], end='')

if __name__ == '__main__':
    main()
    p2()

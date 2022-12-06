from collections import defaultdict

with open('input', 'r') as f:
    contents = f.read().strip().split('\n')
    contents = [line.split(' ') for line in contents]

def pt1():
    regs = defaultdict(int)
    step = 0
    pointer = 0
    while pointer < len(contents):
        line = contents[pointer]
        inst = line[0]
        if inst == 'set':
            regs[line[1]] = int(line[2]) if line[2].isnumeric() or line[2][0] == '-' else regs[line[2]]
        elif inst == 'sub':
            regs[line[1]] -= int(line[2]) if line[2].isnumeric() or line[2][0] == '-' else regs[line[2]]
        elif inst == 'mul':
            step += 1
            regs[line[1]] *= int(line[2]) if line[2].isnumeric() or line[2][0] == '-' else regs[line[2]]
        elif inst == 'jnz' and (line[1] == '1' or regs[line[1]] != 0):
            pointer += int(line[2])
            continue
        pointer += 1
    return step

def pt2():
    pass

print(pt1())
print(pt2())

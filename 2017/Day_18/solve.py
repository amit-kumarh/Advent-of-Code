from collections import defaultdict
with open('input', 'r') as f:
    contents = f.read().strip().split('\n')
    contents = [line.split(' ') for line in contents]

def pt1():
    pointer = 0
    regs = defaultdict(int)
    snd = 0
    while True:
        line = contents[pointer]
        inst = line[0]
        if inst == 'snd':
           snd = regs[line[1]]
        elif inst == 'set':
            regs[line[1]] = int(line[2]) if line[2].isnumeric() or line[2][0] == '-' else regs[line[2]]
        elif inst == 'add':
            regs[line[1]] += int(line[2]) if line[2].isnumeric() or line[2][0] == '-' else regs[line[2]]
        elif inst == 'mul':
            regs[line[1]] *= int(line[2]) if line[2].isnumeric() or line[2][0] == '-' else regs[line[2]]
        elif inst == 'mod':
            regs[line[1]] %= int(line[2]) if line[2].isnumeric() or line[2][0] == '-' else regs[line[2]]
        elif inst == 'rcv' and regs[line[1]] != 0:
            return snd
        elif inst == 'jgz' and regs[line[1]] > 0:
            pointer += int(line[2])
            continue
        pointer += 1
        

def pt2():
    pass

print(pt1())

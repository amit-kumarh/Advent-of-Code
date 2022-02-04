
def get_input():
    with open('dig1', 'r') as file:
        contents = file.read().strip().split('\n')

        contents = [line.split(' ') for line in contents]
    return contents

inst = get_input()

def monad(num, inst, param1, param2):
    num = list(str(num))
    iter_nums = iter(num)
    assert len(num) == 1

    vals = {'x': 0, 'y': 0, 'z': 0, 'w': 0, 'param1':param1, 'param2':param2}

    for line in inst:
        print(vals)
        oper = line[0]

        if oper == 'inp':
            vals['w'] = int(num[0])
        else:
            oper1 = vals[line[1]]
            oper2 = vals[line[2]] if line[2] in vals else int(line[2])
            if oper == 'add':
                vals[line[1]] = oper1 + oper2
            elif oper == 'mul':
                vals[line[1]] = oper1 * oper2
            elif oper == 'div':
                vals[line[1]] = oper1 // oper2
            elif oper == 'mod':
                vals[line[1]] = oper1 % oper2
            elif oper == 'eql':
                vals[line[1]] = 1 if oper1 == oper2 else 0
            else:
                raise Exception('Unknown instruction')
    
    return vals

print(monad(monad(9, inst, 10, 2), 10, 4))
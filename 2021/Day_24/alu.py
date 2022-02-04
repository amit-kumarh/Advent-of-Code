import collections, itertools, re, copy


def get_input():
    with open('input', 'r') as file:
        contents = file.read().strip().split('\n')

        contents = [line.split(' ') for line in contents]
    return contents

inst = get_input()

def monad(num, inst):
    num = list(str(num))
    iter_nums = iter(num)
    assert len(num) == 14

    vals = {'x': 0, 'y': 0, 'z': 0, 'w': 0}

    for line in inst:
        oper = line[0]

        if oper == 'inp':
            vals['w'] = int(next(iter_nums))
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

        print(line)
        print(vals)

    return vals['z']


monad(99999999999999, inst)

#step = 0
#states = {}
#for i in range(99999932596000, 11111111111111, -1):
#    if '0' in str(i): continue
#    step += 1
#    if step % 100000 == 0: print(i) 
 #   if monad(i, inst, states) == 0:
 #       with open(solution, 'a') as file:
 #           print(i)
 #       break


                



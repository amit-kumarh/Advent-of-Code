with open('input', 'r') as istr:
    with open('output.py', 'w') as ostr:
        print('from collections import defaultdict\nregs=defaultdict(int)\nans=0', file=ostr)
        for i, line in enumerate(istr):
            line = line.split()
            line[0] = f"regs['{line[0]}']"
            line[4] = f"regs['{line[4]}']"
            line[1] = '+=' if line[1] == 'inc' else '-='
            print(' '.join(line) + f' else 0\nans = max(ans, {line[0]})', file=ostr)
        print('print(max(regs.values()))\nprint(ans)', file=ostr)
exec(open("output.py").read())
__import__('os').remove('output.py')

    

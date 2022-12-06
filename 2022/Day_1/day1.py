with open('in', 'r') as f: print(*[all := sorted([sum(map(int, (line.strip() for line in [line.strip() for line in elf.strip().split('\n')]))) for elf in f.read().split('\n\n')]), sum(all[-1:]), sum(all[-3:])][1:], sep='\n')


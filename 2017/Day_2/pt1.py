with open('input', 'r') as file:
    contents = file.readlines()
    contents = [line.strip().split('\t') for line in contents]

for i, line in enumerate(contents):
    contents[i] = [int(j) for j in line]

def pt1(contents):
    ans = 0
    for line in contents:
        ans += max(line) - min(line)
    print(ans)

def pt2(contents):
    ans = 0
    for line in contents:
        sline = sorted(line)
        for idx, i in enumerate(line):
            for i2, j in enumerate(line):
                print(i, j)
                if idx == i2:
                    continue
                if i % j == 0:
                    ans += i // j

    print(ans)

pt2(contents)

    



    

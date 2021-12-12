import copy

def get_input():
    with open('input', 'r') as file:
        contents = file.read().split('\n')
        contents = [split_string(line) for line in contents]
        contents = [[int(i) for i in line] for line in contents]
    
    return contents

def split_string(word):
    return [char for char in word]

flashes = 0
contents = get_input()


def flash(x, y):
    print(x, y)
    flashes = 0
    flashed[x][y] = True
    contents[x][y] = 0

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if (-1 < x+i and x+i < len(contents)) and (-1 < y+j and y+j < len(contents[x])):
                if not flashed[x+i][y+j]:
                    contents[x+i][y+j] += 1
                    if contents[x+i][y+j] > 9:
                        flashes += 1
                        flashes += flash(x+i,y+j)
    
    return flashes
    
step = 0           
while True:
    step += 1
    flashed = [[copy.deepcopy(False) for j in range(len(contents[0]))] for i in range(len(contents))]
    for i, line in enumerate(contents):
        for j, octo in enumerate(line):
            contents[i][j] += 1
            
    for i, line in enumerate(contents):
        for j, octo in enumerate(line):
            if contents[i][j] == 10:
                flashes += 1
                flashes += flash(i,j)
    
    flag = True
    for i in flashed:
        for j in i:
            if not j:
                flag = False
    
    if flag:
        print(step)
        break

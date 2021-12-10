import numpy as np

def get_input():
    with open('input', 'r') as file:
        contents = file.read().split('\n')
        contents = [split_string(line) for line in contents][:-1]

        for line in contents:
            line.append(9)
            line.insert(0, 9)

        contents.insert(0, list([9]*len(contents[1])))
        contents.append(list([9]*len(contents[1])))
    
        return contents

def split_string(word):
    return [char for char in word]

def get_lows():
    contents = get_input()

    cnt = []
    for i in range(1, len(contents)-1):
        contents[i] = [int(idx) for idx in contents[i]]

    for i in range(1, len(contents)-1):
        for j in range(1, len(contents[1])-1):
                if contents[i][j+1] > contents[i][j]: 
                    if contents[i][j-1] > contents[i][j]:
                        if contents[i+1][j] > contents[i][j]:
                             if contents[i-1][j] > contents[i][j]:
                                cnt.append((i, j))
    
    return cnt

def pt2(loc, basin):
    contents = get_input()
    adj = [(0,1), (1,0), (0, -1), (-1, 0)]
    for i in range(1, len(contents)-1):
        contents[i] = [int(idx) for idx in contents[i]]

    for row, col in adj:
        cell = contents[loc[0]+row][loc[1]+col]
        idx = (loc[0]+row,loc[1]+col)
        if not cell == 9 and idx not in basin:
            basin.append(idx)
            pt2(idx, basin)

    return len(basin)

    
def main():
    low_points = get_lows()
    sizes = []
    for point in low_points:
        sizes.append(pt2(point, [point]))

    sizes.sort(reverse=True)

    print(sizes)
    
if __name__ == '__main__':
    main()

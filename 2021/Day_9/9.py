import numpy as np

def get_input():
    with open('input', 'r') as file:
        contents = file.read().split('\n')
        contents = [split_string(line) for line in contents][:-1]

        for line in contents:
            line.append(10)
            line.insert(0, 10)

        contents.insert(0, list([10]*len(contents[1])))
        contents.append(list([10]*len(contents[1])))
    
        return contents

def split_string(word):
    return [char for char in word]

def main():
    contents = get_input()

    cnt = 0
    for i in range(1, len(contents)-1):
        contents[i] = [int(idx) for idx in contents[i]]

    for i in range(1, len(contents)-1):
        for j in range(1, len(contents[1])-1):
                if contents[i][j+1] > contents[i][j]: 
                    if contents[i][j-1] > contents[i][j]:
                        if contents[i+1][j] > contents[i][j]:
                             if contents[i-1][j] > contents[i][j]:
                                cnt += int(contents[i][j]) + 1
    
    print(cnt)


if __name__ == '__main__':
    main()

import re
from functools import reduce
from collections import Counter, defaultdict, deque
from treelib import Node, Tree

def get_input():
    with open('input', 'r') as file:
        contents = [list(map(int, list(x.strip()))) for x in file.readlines()]
    return contents

def main():
    grid = get_input()
    ans = 0
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[i])-1):
            col = [grid[x][j] for x in range(0, len(grid))]
            if len(list(filter(lambda x: x >= grid[i][j], grid[i][:j]))) == 0:
                ans += 1
                continue
            if len(list(filter(lambda x: x >= grid[i][j], grid[i][j+1:]))) == 0:
                ans += 1
                continue
            if len(list(filter(lambda x: x >= grid[i][j], col[:i]))) == 0:
                ans += 1
                continue
            if len(list(filter(lambda x: x >= grid[i][j], col[i+1:]))) == 0:
                ans += 1
                continue

    ans += len(grid) * 4 - 4
    print(ans)


def p2():
    grid = get_input()
    ans = 0
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[i])-1):
            col = [grid[x][j] for x in range(0, len(grid))]
            val = grid[i][j]
            distances = []

            curr_col = j+1
            distance = 0
            while curr_col < len(grid[0]) and grid[i][curr_col] < val:
                distance += 1
                curr_col += 1
            if not curr_col == len(grid[0]):
                distance += 1
            distances.append(distance)


            curr_col = j-1
            distance = 0
            while curr_col >= 0 and grid[i][curr_col] < val:
                distance += 1
                curr_col -= 1
            if not curr_col == -1:
                distance += 1
            distances.append(distance)

            curr_row = i+1 
            distance = 0
            while curr_row < len(col) and grid[curr_row][j] < val:
                distance += 1
                curr_row += 1
            if not curr_row == len(col):
                distance += 1
            distances.append(distance)
                       
            curr_row = i-1 
            distance = 0
            while curr_row >= 0 and grid[curr_row][j] < val:
                distance += 1
                curr_row -= 1
            if not curr_row == -1:
                distance += 1
            distances.append(distance)

            tot = reduce(lambda a, b: a*b, distances)
            if tot > ans:
                ans = tot

    print(ans)

if __name__ == '__main__':
    p2()

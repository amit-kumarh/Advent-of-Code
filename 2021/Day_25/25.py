import networkx as nx
import matplotlib.pyplot as plt
import copy

def get_input():
    with open('input', 'r') as file:
        contents = file.read().strip().split('\n')
        contents  = [[char for char in line] for line in contents]
    return contents


grid = get_input()

step = 0
flag = True
while flag:
    step += 1
    flag = False
    cgrid = copy.deepcopy(grid)
    #check east
    for i, line in enumerate(grid):
        for j, cell in enumerate(line):
            if cell == '>':
                if grid[i][(j+1) % len(line)] == '.':
                   cgrid[i][(j+1) % len(line)] = '>'
                   cgrid[i][j] = '.' 
                   flag = True
    
    grid = cgrid
    cgrid = copy.deepcopy(grid)
    for i, line in enumerate(grid):
        for j, cell in enumerate(line):
            if cell == 'v':
                if grid[(i+1) % len(grid)][j] == '.':
                   cgrid[(i+1) % len(grid)][j] = 'v'
                   cgrid[i][j] = '.' 
                   flag = True
    
    grid = cgrid
     
print(step)





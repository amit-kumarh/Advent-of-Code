import networkx as nx
import copy
import numpy as np

def get_input():
    with open('input', 'r') as file:
        contents = file.read().strip().split('\n')
        contents = [split_string(line) for line in contents]
    
    return contents


def split_string(word):
    return [int(char) for char in word]

contents = get_input()

def increaseRow(i,j, k):
    kcopy = copy.deepcopy(k)
    for idx, cell in enumerate(k):
        if cell+i+j < 10:
            kcopy[idx] += i+j
        else:
            kcopy[idx] -= 9-(i+j)
    return kcopy


fullmaze = []
for i in range(5):
    for k in contents:
        line = []
        for j in range(5):
            line += increaseRow(i, j, k)
        fullmaze.append(line)



rows = len(fullmaze)-1
cols = len(fullmaze[0])-1
G = nx.DiGraph()
adj = [(0,1), (1,0), (0,-1), (-1, 0)]

for i, row in enumerate(fullmaze):
    for j ,cell in enumerate(row):
        for x,y in adj:
            if i+x >= 0 and i+x < len(fullmaze):
                if j+y >= 0 and j+y < len(row):
                    G.add_edge((i,j), (i+x, j+y), weight=fullmaze[i+x][j+y])

path = nx.dijkstra_path_length(G, source=(0,0),target=(rows,cols), weight='weight')
print(path)






import networkx as nx

def get_input():
    with open('input', 'r') as file:
        contents = file.read().strip().split('\n')
        contents = [split_string(line) for line in contents]
    
    return contents


def split_string(word):
    return [int(char) for char in word]

contents = get_input()
rows = len(contents)-1
cols = len(contents[0])-1

G = nx.DiGraph()
adj = [(0,1), (1,0), (0,-1), (-1, 0)]

for i, row in enumerate(contents):
    for j ,cell in enumerate(row):
        for x,y in adj:
            if i+x >= 0 and i+x < len(contents):
                if j+y >= 0 and j+y < len(row):
                    G.add_edge((i,j), (i+x, j+y), weight=contents[i+x][j+y])

path = nx.dijkstra_path_length(G, source=(0,0),target=(rows,cols), weight='weight')
print(path)






from collections import defaultdict

def get_input():
    with open('input', 'r') as file:
        contents = file.read().strip().split('\n')
        contents = [line.strip().split('-') for line in contents]
    
    neighbors = defaultdict(list)

    for line in contents:
        x, y = line
        if y != 'start':
            neighbors[x].append(y)
        if x != 'start':
            neighbors[y].append(x)

    
    return neighbors

neighbors = get_input()


def traverse(current_loc, visited, path):
    global paths
    if current_loc == 'end':
        paths += 1
        print(path)
        return 
    
    visited[current_loc] += 1
    path.append(current_loc)

    double_lower = True
    for key in visited:
        if key.islower():
            if visited[key] == 2:
                double_lower = False
                break
        
    for loc in neighbors[current_loc]:
        if loc.islower() and loc != 'end':
           if loc not in visited or visited[loc] == 0:
               traverse(loc, visited, path)
           elif visited[loc] < 2 and double_lower:
               traverse(loc, visited, path)
        else:
            traverse(loc, visited, path)
    
    path.pop()
    visited[current_loc] -= 1

        

paths = 0
test = traverse('start', defaultdict(int), [])
print(paths)

#    start
#    /   \
#c--A-----b--d
#    \   /
#     end





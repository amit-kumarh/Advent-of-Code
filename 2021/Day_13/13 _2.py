from collections import defaultdict, Counter

def get_input():
    with open('input', 'r') as file:
        contents = file.read().split('\n')

        points = [line.split(',') for line in contents]
        points_int = []
        for line in points:
            p1 = int(line[0])
            p2 = int(line[1])
            points_int.append([p1, p2]) 

    return points_int

def get_inst():
    with open('instructions', 'r') as file:
        contents = file.read().strip().split('\n')
        inst = []
        for line in contents:
            idx = line.index('=')
            axis = line[idx-1]
            num = int(line[idx+1:])
            inst.append([axis, num])
    
        return inst




points = get_input()
instructions = get_inst()
#instructions = [['y', 7], ['x', 5]]
print(instructions)

for axis, num in instructions:
    if axis == 'x':
        for i, point in enumerate(points):
            x = point[0]
            y = point[1]
            if x > num:
                point[0] = num - abs(point[0]-num)
    if axis == 'y':
        for i, point in enumerate(points):
            x = point[0]
            y = point[1]
            if y > num:
                point[1] = num - abs(point[1]-num)

board = []
for i in range(6):
    board.append([])
    for j in range(39):
        board[i].append('.')

for point in points:
    board[point[1]][point[0]] = '#'

for line in board:
    print(line)






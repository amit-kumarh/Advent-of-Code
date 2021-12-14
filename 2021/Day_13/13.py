from collections import Counter

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

points = get_input()
instructions = [['x',655]]

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

tuple_points = [(line[0], line[1]) for line in points]

count = Counter(tuple_points)

print(count.most_common(10))
print(len(count))
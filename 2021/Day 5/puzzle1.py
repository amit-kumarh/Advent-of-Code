def get_input():
    with open('input', 'r') as file:
        contents = file.read().split('\n')
        coordinates = [((pair1.split(',')), (pair2.split(','))) for pair1, pair2 in [line.strip().split(' -> ') for line in contents]]
    
    return coordinates

def get_coords_dict(coords):
    coords_dict = {}
    for line in coords:
        points = get_points(line)
        for point in points:
            if point not in coords_dict:
                coords_dict[point] = 0
            coords_dict[point] += 1

    return coords_dict

def get_points(line):
    #unpacking
    x1 = int(line[0][0])
    y1 = int(line[0][1])
    x2 = int(line[1][0])
    y2 = int(line[1][1])

    points = []    
    if y1 == y2:
        for i in range(x1, x2+1) if x2 > x1 else range(x2, x1+1):
            points.append((str(i), str(y1)))
    elif x1 == x2:
        for i in range(y1, y2+1) if y2 > y1 else range(y2, y1+1):
            points.append((str(x1), str(i)))
    else:
        if (y2-y1)/(x2-x1) > 0:
            #positive slope
            if x1 > x2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            for xdelta, ydelta in zip(range(x1, x2+1), range(y1, y2+1)):
                points.append((str(xdelta), str(ydelta)))
        else:
            #negative slope
            if x1 > x2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            for xdelta, ydelta in zip(range(x1, x2+1), range(y1, y2-1, -1)):
                points.append((str(xdelta), str(ydelta)))

        

    return points
    



def main():
    coords = get_input()
    coords_dict =  get_coords_dict(coords)
    solution = len([point for point in coords_dict if coords_dict[point] >= 2])
    print(solution)


if __name__ == '__main__':
    main()
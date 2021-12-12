with open('movements', 'r') as file:
    lines = file.readlines()
    lines = [line.strip().split() for line in lines]
    x = 0
    y = 0
    aim = 0
    for line in lines:
        line[1] = int(line[1])
        if line[0] == 'forward':
            x += line[1]
            y += aim*line[1]
        elif line[0] == 'up':
            aim -= line[1]
        elif line[0] == 'down':
            aim += line[1]
    
    print(x*y)
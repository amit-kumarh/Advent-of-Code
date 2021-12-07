with open('depths', 'r') as file:
    lines = file.readlines()
    lines = [int(line.strip()) for line in lines]
    increasing_count = 0
    for count in range(0, len(lines)-3):
        if sum(lines[count+1:count+4]) > sum(lines[count:count+3]):
            increasing_count += 1

print(increasing_count)



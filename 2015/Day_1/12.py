with open('2015/Day_1/input', 'r') as file:
    contents = file.read().strip()



floor = 0
for i, char in enumerate(contents):
    if floor == -1:
        print(i)
    if char == '(':
        floor += 1
    elif char == ')':
        floor -= 1

print(floor)

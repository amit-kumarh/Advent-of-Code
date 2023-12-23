with open('input', 'r') as file:
    contents = file.read().strip()

floor = 0
for char in contents:
    if char == '(':
        floor += 1
    if char == ')':
        floor -= 1

print(floor)

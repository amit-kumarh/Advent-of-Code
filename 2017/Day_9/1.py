from collections import Counter, defaultdict, deque

def get_contents():
    with open('input', 'r') as f:
        contents = f.read().strip()
    return contents

contents = get_contents()
contents = [char for char in contents]

new = []
ignore = False
garb = False
for idx, char in enumerate(contents):
    prev = contents[idx-1]
    if ignore:
        ignore = False
        continue
    if char  == '!':
        ignore = True
    if char == '<':
        garb = True
    elif char == '>' and garb:
        garb = False
    elif not garb:
        new.append(char)
print(''.join(new))

stack, score = 0, 0
for char in new:
    if char == '{':
        stack += 1
    elif char == '}':
        score += stack
        stack -= 1 

print(score)

def get_contents():
    with open('input', 'r') as f:
        contents = f.read().strip()
    return contents

contents = get_contents()
contents = [char for char in contents]

ignore = False
garb = False
cnt = 0
for idx, char in enumerate(contents):
    if ignore:
        ignore = False
        continue
    if char  == '!':
        ignore = True
    elif char == '<' and not garb:
        garb = True
    elif char == '>' and garb:
        garb = False
    elif garb:
        cnt += 1

print(cnt)

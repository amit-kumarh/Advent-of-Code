from collections import defaultdict
import copy

def get_input():
    with open('input', 'r') as file:
        inst, contents = file.read().strip().split('\n\n')

        photo = [[char for char in line] for line in contents.split('\n')]

    return inst, photo

inst, photo = get_input()

def pad(photo):
    for step in range(150):
        for row in photo:
            row.append('.')
            row.insert(0, '.')
        
        photo.insert(0, ['.'] * len(photo[0]))
        photo.append(['.'] * len(photo[0]))

    return photo

def get_string(idx, photo):
    x, y = idx
    res = ''
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if photo[x+i][y+j] == '#':
                res += '1'
            else:
                res += '0'
    
    return int(res, 2)

photo = pad(photo)

for step in range(50):
    if step % 2 == 0:
        #reset edge to .
        for row in photo:
            row[-1] = '.'
            row[0] = '.'
        
        photo[0] = ['.'] * len(photo[0])
        photo[-1] = ['.'] * len(photo[0])
    else:
        #reset edge to #
        for row in photo:
            row[-1] = '#'
            row[0] = '#'
        
        photo[0] = ['#'] * len(photo[0])
        photo[-1] = ['#'] * len(photo[0])

    output = [[copy.deepcopy(None) for j in range(len(photo[0]))] for i in range(len(photo))]
    for ri, row in enumerate(photo[1:-1]):
        ri += 1
        for ci, cell in enumerate(row[1:-1]):
            ci += 1
            inst_idx = get_string((ri, ci), photo)
            new_pixel = inst[inst_idx] 
            output[ri][ci] = new_pixel
    
    photo = output

ans = 0
for row in photo[5:-5]:
    print(row)
    for cell in row[5:-5]:
        if cell == '#':
            ans += 1

print(ans)




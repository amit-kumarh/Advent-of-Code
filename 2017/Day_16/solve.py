with open('input', 'r') as f:
    contents = tuple(f.read().strip().split(','))

def spin(arr, num):
    return arr[-num:] + arr[:-num]

def ex(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return arr

def partner(arr, a, b):
    ia = arr.index(a)
    ib = arr.index(b)
    arr[ia], arr[ib] = arr[ib], arr[ia]
    return arr

progs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

def pt1(contents, progs):
    for i in contents:
        if i[0] == 's':
            progs = spin(progs, int(i[1:]))
        else:
            inst1, inst2 = i[1:].split('/')
            if i[0] == 'x':
                progs = ex(progs, int(inst1), int(inst2))
            else:
                progs = partner(progs, inst1, inst2)
    return ''.join(progs)

def pt2():
    progs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    progs = pt1(contents, progs)
    step = 1
    while start != progs:
        progs = pt1(contents, progs)
        step += 1

    for _ in range(1000000000 % step):
        progs = pt1(contents, progs)

    return ''.join(progs)

print(pt1(contents, progs))
print(pt2())

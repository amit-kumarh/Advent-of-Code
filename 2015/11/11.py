import sys

with open(sys.argv[1], 'r') as f:
    start = f.read().strip()

def increment(pw):
    pw = list(pw)
    pw[ptr] = chr(ord(pw[ptr := len(pw)-1]) + 1)
    while ord(pw[ptr]) == 123:
        pw[ptr] = 'a'
        ptr -= 1
        pw[ptr] = chr(ord(pw[ptr]) + 1)

    return ''.join(pw)

def is_valid(pw):
    if 'i' in pw or 'o' in pw or 'l' in pw:
        return False
    
    for i in range(len(pw) - 2):
        if ord(pw[i]) == ord(pw[i+1]) - 1 and ord(pw[i]) == ord(pw[i+2]) - 2:
            break
    else:
        return False

    pairs = i = 0
    while i < len(pw) - 1:
        if pw[i] == pw[i+1]:
            pairs += 1
            i += 1
        i += 1
    if pairs < 2:
        return False
    
    return True

def solve(curr):
    while True:
        curr = increment(curr)
        if is_valid(curr):
            return curr

print(p1 := solve(start))
print(solve(p1))

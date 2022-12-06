def get_contents():
    with open('input', 'r') as f:
        return  [ord(char) for char in f.read().strip()] + [17,31,73,47,23]

def rev(arr, low, hi):
    rot_arr = arr[low:] + arr [:low]
    rev_arr = list(reversed(rot_arr[:hi])) + rot_arr[hi:]
    return rev_arr[-low:] + rev_arr[:-low]

lengths = get_contents()
string = list(range(256))
skip = pointer = 0
for _ in range(64):
    for l in lengths:
        string = rev(string, pointer, l)
        pointer = (pointer + skip + l) % len(string)
        skip += 1

ans = ''
for i in range(16):
    num = 0
    for j in range(16):
        num = num ^ string[i * 16 + j] 
    ans += hex(num)[2:] if len(hex(num)[2:]) == 2 else '0' + hex(num)[2:]
print(ans)

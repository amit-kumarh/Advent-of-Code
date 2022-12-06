def get_contents():
    with open('flo', 'r') as f:
        contents = [int(i) for i in f.read().strip().split(',')]
    return contents

def rev(arr, low, hi):
    rot_arr = arr[low:] + arr [:low]
    rev_arr = list(reversed(rot_arr[:hi])) + rot_arr[hi:]
    return rev_arr[-low:] + rev_arr[:-low]

lengths = get_contents()
string = list(range(256))
skip = pointer = 0
for l in lengths:
    string = rev(string, pointer, l)
    pointer = (pointer + skip + l) % len(string)
    skip += 1

print(string[0] * string[1])

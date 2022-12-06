import collections
with open('input', 'r') as f:
    contents = f.read().strip()
contents = 'hfdlxzhv'

def rev(arr, low, hi):
    rot_arr = arr[low:] + arr [:low]
    rev_arr = list(reversed(rot_arr[:hi])) + rot_arr[hi:]
    return rev_arr[-low:] + rev_arr[:-low]

def pt1(contents):
    solution = 0
    for k in range(128):
        lengths = [ord(char) for char in contents + '-' + str(k)] + [17,31,73,47,23]
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

        assert len(ans) == 32

        binary = ''
        for char in ans:
            toadd = bin(int(char, base=16))[2:]
            while len(toadd) < 4: toadd = '0' + toadd
            binary += toadd

        assert len(binary) == 128

        solution += sum([int(a) for a in binary])

    return solution

def grid():
    grid = []
    for k in range(128):
        lengths = [ord(char) for char in contents + '-' + str(k)] + [17,31,73,47,23]
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

        assert len(ans) == 32

        binary = ''
        for char in ans:
            toadd = bin(int(char, base=16))[2:]
            while len(toadd) < 4: toadd = '0' + toadd
            binary += toadd

        assert len(binary) == 128

        grid.append(list(binary))
    return grid
    
def pt2(grid):
    ans = 0
    ones = []
    for i in range(128):
        for j in range(128):
            if grid[i][j] == '1':
                ones.append((i,j))
    adj = [(1,0), (-1,0), (0,1), (0,-1)]
    while ones:
        ans += 1
        queue = collections.deque()
        queue.append(ones[0])
        ones.remove(ones[0])
        while queue:
            x, y = queue.popleft()

            for locx, locy in adj:
                if (next := (x+locx, y+locy)) in ones:
                    queue.append(next)
                    ones.remove(next)
    return ans

print(pt1(contents))
print(pt2(grid()))

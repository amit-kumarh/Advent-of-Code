size = 366

def pt1():
    buffer = [0]
    pointer = 0
    for i in range(1, 2018):
        buffer.insert((pointer := (pointer + size) % len(buffer)+1), i)
    return buffer[pointer + 1]

def pt2():
    ans = pointer = 0
    for i in range(1, 50000001):
        if (pointer := (pointer + size) % i+1) == 1: ans = i
    return ans

print(pt1())
print(pt2())

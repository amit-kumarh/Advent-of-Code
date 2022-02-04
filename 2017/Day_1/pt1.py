with open('input', 'r') as foo:
    cap = foo.read().strip()
    cap = list(cap)
    cap = [int(i) for i in cap]

def pt1(cap):
    ans = 0
    for i in range(len(cap)-1):
        if cap[i] == cap[i + 1]:
            ans += int(cap[i])

    if cap[-1] == cap[0]:
        ans += int(cap[-1])

    print(ans)

def pt2(cap):
    ans = 0
    half = len(cap) //2    
    for i in range(len(cap)-1):
        if cap[i] == cap[(i + half) % len(cap)]:
            ans += int(cap[i])

    print(ans)

pt1(cap)
pt2(cap)

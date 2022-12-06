a=512
b=191
A=16807
B=48271
divisor=2147483647
def pt1(a, b):
    ans = 0
    for _ in range(40000000):
        a = ((a*A) & (divisor)) + (a*A >> 31)
        b = ((b*B) & (divisor)) + (b*B >> 31)
        if a & 0xFFFF == b & 0xFFFF:
            ans += 1
    return ans

def pt2(a, b):
    ans = 0
    for _ in range(5000000):
        a = ((a*A) & (divisor)) + ((a*A) >> 31)
        while not a % 4 == 0:
            a = ((a*A) & (divisor)) + ((a*A) >> 31)
        b = ((b*B) & (divisor)) + ((b*B) >> 31)
        while not b % 8 == 0:
            b = ((b*B) & (divisor)) + ((b*B) >> 31)
        if a & 0xFFFF == b & 0xFFFF:
            ans += 1
    return ans

print(pt1(a, b))
print(pt2(a, b))

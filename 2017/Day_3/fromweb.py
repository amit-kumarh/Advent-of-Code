inp = 368078

from math import sqrt, ceil
circle = ceil(sqrt(inp)) // 2
print(circle)
circle_zero = pow(circle * 2 - 1, 2)
print(circle_zero)
centers = [ circle_zero + x * circle for x in [1, 3, 5, 7] ]
print(centers)
distance = circle + min([ abs(inp - x) for x in centers ])
print(distance)

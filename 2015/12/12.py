import sys

with open(sys.argv[1], 'r') as f:
    contents = f.read().strip()

def solve(obj, p2):
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, list):
        return sum(solve(x, p2) for x in obj)
    elif isinstance(obj, dict):
        if p2 and 'red' in obj.values():
            return 0
        return sum(solve(x, p2) for x in obj.values())

    return 0

print(solve(eval(contents), False)) 
print(solve(eval(contents), True))

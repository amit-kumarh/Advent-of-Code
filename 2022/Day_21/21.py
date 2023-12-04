import sys

if len(sys.argv) < 2:
    path = "21.in"
else:
    path = sys.argv[1]
with open(path) as f:
    c = f.read().strip()

humn = 3221245824363
while "root" not in locals():
    for line in c.splitlines():
        name, inst = line.split(':')
        if name == 'humn':
            continue
        try:
            locals()[name] = eval(inst)
        except:
            pass
diff = prrg - jntz

ans = locals()['root']
print(ans)
print(round(diff))

# brute-forced p2 one digit at a time...

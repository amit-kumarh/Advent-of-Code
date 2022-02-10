#start = perf_counter()
def get_contents():
    with open('input', 'r') as f:
        contents = f.read().strip().split('\n')
        contents = [int(i) for i in contents]
    return contents

contents = get_contents()
pointer = 0
step = 0
while pointer < len(contents):
    step += 1
    inst = contents[pointer]
    contents[pointer] = inst + 1 if inst < 3 else inst - 1
    pointer += inst

print(step)
#end = perf_counter()
#print(end-start)

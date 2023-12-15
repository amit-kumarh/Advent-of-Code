import sys
import functools

with open(sys.argv[1]) as f:
    contents = f.read().strip().split(",")

def hash(s):
    return functools.reduce(lambda x, y: (x + ord(y)) * 17 % 256, s, 0)

boxes = [dict() for _ in range(256)]
for inst in contents:
    match inst.split("="):
        case [label, power]:
            boxes[hash(label)][label] = int(power)
        case [inst]:
            boxes[hash(label := inst[:-1])].pop(label, "nothing")

print(sum(hash(inst) for inst in contents))
print(
    sum(
        (i + 1) * (j + 1) * power
        for i, box in enumerate(boxes)
        for j, power in enumerate(box.values())
    )
)

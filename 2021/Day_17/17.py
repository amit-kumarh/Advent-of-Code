import copy
from collections import defaultdict, Counter

def get_input():
    with open('ex', 'r') as file:
        contents = file.read().split('\n')
    
    return contents

xRange = lambda x: x <= 94 and x >= 60
yRange = lambda y: y <= -136 and y >= -171
xOver = lambda x: x > 94
yOver = lambda y: y < -171
tri = lambda x: x*(x+1)/2

#xRange = lambda x: x <= 30 and x >= 20
#yRange = lambda y: y <= -5 and y >= -10
#xOver = lambda x: x > 30
#yOver = lambda y: y < -10
#tri = lambda x: x*(x+1)/2

def findXranges():
    global xRange, yRange, xOver, yOver

    step_dict = defaultdict(list)
    for xv in range(0, 100):
        xpos = 0
        xv_copy = copy.deepcopy(xv)
        step = 0
        while not xOver(xpos):
            step += 1
            xpos += xv_copy
            xv_copy -= 1
            if xv_copy == -1:
                xv_copy = 0
            if xRange(xpos):
                step_dict[step].append(xv)
            if step > 350:
                break
    
    return step_dict

def findYranges():
    global yRange, xRange, xOver, yOver

    step_dict = defaultdict(list)
    for yv in range(-171, 1000):
        ypos = 0
        yv_copy = copy.deepcopy(yv)
        step = 0
        while not yOver(ypos):
            step += 1
            ypos += yv_copy
            yv_copy -= 1
            if yRange(ypos):
                step_dict[step].append(yv)

    return step_dict


x_ranges = findXranges() 
print(x_ranges)
y_ranges = findYranges()
#print(y_ranges)

cnt = 0
steps = []
for step in x_ranges:
    if step in y_ranges:
        for xval in x_ranges[step]:
            for yval in y_ranges[step]:
                steps.append((xval, yval))

print(len(Counter(steps)))

with open('input', 'r') as f:
    contents = {line.split(': ')[0]: line.split(': ')[1] for line in f.read().strip().split('\n')}

def sim(delay, pt2):
    severity = 0
    for packet in contents.keys():
        ran = int(contents[packet])
        if (int(packet)+delay) % (2*(ran-1)) == 0:
            severity += int(packet) * ran
            if pt2:
                return None
    return severity 
    
def pt2():
    delay = 0
    while True:
        if sim(delay, True) is not None:
            return delay
        delay += 1 

print(sim(0, False))
print(pt2())

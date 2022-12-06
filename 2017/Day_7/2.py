#start = perf_counter()
import numpy as np
from collections import Counter
import re

def get_contents():
    with open('ex', 'r') as f:
        contents = f.read().strip()
        parents = re.findall(r'([a-z]+) \((\d+)\)', contents)
        children = [re.findall(r'-> (.*)$', line) for line in contents.split('\n')]
        for line in children:
            if line:
                line[0] = line[0].split(', ')
    return parents, children

parents, children = get_contents()
print(parents)
print()
print(children)

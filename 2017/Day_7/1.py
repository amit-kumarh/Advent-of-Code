#start = perf_counter()
import numpy as np
from collections import Counter
import re

def get_contents():
    with open('input', 'r') as f:
        contents = f.read().strip()
        children = re.findall(r'[a-z]+', contents)
    return children

children = get_contents()

seen  = Counter(children)
print(seen.most_common()[-1])

with open('input', 'r') as f: print(Counter(re.findall(r'[a-z]+', f.read().strip())).most_common()[-1][0])

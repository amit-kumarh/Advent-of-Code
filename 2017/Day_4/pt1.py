with open('input', 'r') as f:
    contents = f.read().strip().split('\n')

pt1, pt2 = 0,0
for line in contents:
    sorted_words = set([''.join(sorted(word)) for word in line.split(' ')])
    words = set(line.split(' '))
    if len(words) == len(line.split(' ')):
        pt1 += 1
    if len(sorted_words) == len(line.split(' ')):
        pt2 += 1
    
print(pt1, pt2)

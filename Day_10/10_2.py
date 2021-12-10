import numpy as np

def get_input():
    with open('input', 'r') as file:
        contents = file.read().split('\n')
        contents = [split_string(line) for line in contents]
    
    return contents

def split_string(word):
    return [char for char in word]

def main():
    contents = get_input()

    starts = []
    corrupted = []
    

    for i, line in enumerate(contents):
        for char in line:
            if char in '([{<':
                starts.append(char)
            elif char in ')]}>':
                if char == ')':
                    if starts[-1] == '(':
                        del starts[-1]
                    else:
                        corrupted.append(line)
                        break
                elif char == ']':
                    if starts[-1] == '[':
                        del starts[-1]
                    else:
                        corrupted.append(line)
                        break
                elif char == '}':
                    if starts[-1] == '{':
                        del starts[-1]
                    else:
                        corrupted.append(line)
                        break
                elif char == '>':
                    if starts[-1] == '<':
                        del starts[-1]
                    else:
                        corrupted.append(line)
                        break
    
    for i in corrupted:
        contents.remove(i)

    scores = []

    for i, line in enumerate(contents):
        starts = []
        for char in line:
            if char in '([{<':
                starts.append(char)
            elif char in ')]}>':
                if char == ')':
                    if starts[-1] == '(':
                        del starts[-1]
                elif char == ']':
                    if starts[-1] == '[':
                        del starts[-1]
                elif char == '}':
                    if starts[-1] == '{':
                        del starts[-1]
                elif char == '>':
                    if starts[-1] == '<':
                        del starts[-1]

        finish = []
        print(finish)
        for char in starts:
            if char == '(':
                finish.append(')')
            if char == '[':
                finish.append(']')
            if char == '{':
                finish.append('}')    
            if char == '<':
                finish.append('>')
        finish.reverse()

        scores.append(get_score(finish))

    scores.sort()
    print(scores[len(scores)//2])

    

def get_score(finish):
    score = 0
    for i in finish:
        score *= 5
        if i == ')':
            score += 1
        if i == ']':
            score += 2
        if i == '}':
            score += 3
        if i == '>':
            score += 4
    return score
        


if __name__ == '__main__':
    main()

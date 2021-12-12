def get_input():
    with open('ex', 'r') as file:
        contents = file.read().split('\n')
        contents = [split_string(line) for line in contents]
    
    return contents

def split_string(word):
    return [char for char in word]

def main():
    contents = get_input()

    starts = []
    score = 0
    

    for line in contents:
        for char in line:
            if char in '([{<':
                starts.append(char)
            elif char in ')]}>':
                if char == ')':
                    if starts[-1] == '(':
                        del starts[-1]
                    else:
                        score += 3
                        break
                elif char == ']':
                    if starts[-1] == '[':
                        del starts[-1]
                    else:
                        score += 57
                        break
                elif char == '}':
                    if starts[-1] == '{':
                        del starts[-1]
                    else:
                        score += 1197
                        break
                elif char == '>':
                    if starts[-1] == '<':
                        del starts[-1]
                    else:
                        score += 25137
                        break

    print(score)

if __name__ == '__main__':
    main()

def get_input():
    with open('input', 'r') as file:
        contents = file.readlines()

        output = [i.strip().split('|')[1].split(' ') for i in contents]
        input_data = [i.strip().split('|')[0].split(' ') for i in contents]
        output = [i[1:] for i in output]
        input_data = [i[:-1] for i in input_data]

    
    return input_data, output

def main():
    input_data, output_data = get_input()
    solution = 0
    
    
    for idx, line_unsorted in enumerate(input_data):
        answers = {1: 0,2: 0,3: 0,4: 0,5: 0,6: 0,7: 0,8: 0,9: 0}
        line = line_unsorted
        line.sort(key = len)
        for j, combo in enumerate(line):
            sorted_characters  = sorted(combo)
            line[j] = ''.join(sorted_characters)

        for i in line:
            if len(i) == 2:
                answers[1] = i
                continue
            if len(i) == 3:
                answers[7] = i
                continue
            if len(i) == 4:
                answers[4] = i
                continue
            if len(i) == 7:
                answers[8] = i
                continue
            if len(i) == 5:
                if answers[1][0] in i and answers[1][1] in i:
                    answers[3] = i
                    continue
                else:
                    cnt = 0
                    for char in answers[4]:
                        if char in i:
                            cnt += 1
                    if cnt >= 3:
                        answers[5] = i
                        continue
                    else:
                        answers[2] = i 
                        continue               
            if len(i) == 6:
                cnt = 0
                for char in answers[4]:
                    if char in i:
                        cnt += 1
                if cnt == 4:
                    answers[9] = i
                    continue
                else:
                    cnt = 0
                    for char in answers[5]:
                        if char in i:
                            cnt += 1
                    if cnt == 5:
                         answers[6] = i
                         continue
                    else:
                         answers[0] = i
                         continue

        lookup_dict = inv_map = {v: k for k, v in answers.items()}

        for j, combo in enumerate(output_data[idx]):
            sorted_characters  = sorted(combo)
            output_data[idx][j] = ''.join(sorted_characters)

        

        output_num = ''
        for output in output_data[idx]:
            output_num += str(lookup_dict[output])
        
        solution += int(output_num)

    print(solution)
        

if __name__ == '__main__':
    main()

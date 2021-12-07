with open('diag', 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    remaining_lines = lines
    for i in range(len(lines[0])+1):
        if len(remaining_lines) == 1:
            oxygen = int(remaining_lines[0], base=2)
            break

        count = 0
        for line in remaining_lines:
            count += int(line[i])
        avg = count / len(remaining_lines)
        if avg >= .5:
            common_bit = '1'
        elif avg < .5:
            common_bit = '0'

        rem = []
        for line in remaining_lines:
            if not line[i] != common_bit:
                rem.append(line)
        remaining_lines = rem
                
    
    remaining_lines = lines
    for i in range(len(lines[0])):
        if len(remaining_lines) == 1:
            carbondioxide = int(remaining_lines[0], base=2)
            break

        count = 0
        for line in remaining_lines:
            count += int(line[i])
        avg = count / len(remaining_lines)
        if avg >= .5:
            common_bit = '0'
        elif avg < .5:
            common_bit = '1'

        rem = []
        for line in remaining_lines:
            if not line[i] != common_bit:
                rem.append(line)

        remaining_lines = rem


print(oxygen * carbondioxide)







            

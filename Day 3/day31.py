with open('diag', 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    gamma = ''
    epsilon = ''

    for i in range(len(lines[0])):
        count = 0
        for line in lines:
            count += int(line[i])
        avg = count / len(lines)
        if avg > .5:
            gamma = gamma + '1'
            epsilon = epsilon + '0'
        else:
            gamma = gamma + '0'
            epsilon = epsilon + '1'

    gamma = int(gamma, base=2)
    epsilon = int(epsilon, base=2)

    print(gamma*epsilon)


        

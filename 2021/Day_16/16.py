bits = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111'
}


def get_input():
    global bits
    files = ['ex', 'lit', 'input']
    with open(files[2], 'r') as file:
        contents = file.read().strip()
        print(contents)
        bin_contents = ''
        for char in contents:
            bin_contents += bits[char]
        
    
    return bin_contents

msg = get_input()
version_sum = 0

def parse(msg):
    global version_sum
    V = int(msg[:3],2)
    print('packet' + str(V))
    T = int(msg[3:6],2)

    data = msg[6:]

    version_sum += V

    if T == 4: # literal - WORKING
        rem = True
        literal = ''
        while rem:
            if data[0] == '0':
                rem = False
            literal += data[1:5]
            data = data[5:]
        return int(literal, 2), data
    else:
        literals = []
        ltid = data[0]
        if ltid == '0': # bit length
            num_bits = int(data[1:16], 2)
            data = data[16:]
            sub = data[:num_bits]
            rest = data[num_bits:]
            while sub:
                ans, sub = parse(sub)
                literals.append(ans)
            sub = rest

        elif ltid == '1': # packet length
            num_packets = int(data[1:12], 2)
            data = data[12:]
            sub = data
            for i in range(num_packets):
                ans, sub = parse(sub)
                literals.append(ans)

        if T == 0: # sum
            return sum(literals), sub
        
        elif T == 1: # product
            product = 1
            for i in literals:
                product *= i
            return product, sub
        
        elif T == 2: #min
            return min(literals), sub
        
        elif T == 3: #max
            return max(literals), sub
        
        elif T == 5: #greater than
            if literals[0] > literals[1]:
                return 1, sub
            else:
                return 0, sub
        
        elif T == 6: #less than
            if literals[0] < literals[1]:
                return 1, sub
            else:
                return 0, sub
        
        elif T == 7: #equals
            if literals[0] == literals[1]:
                return 1, sub
            else:
                return 0, sub
        
        
print(version_sum)
ans, rem = parse(msg)
print(ans)





    






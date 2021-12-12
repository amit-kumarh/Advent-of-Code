def get_input():
    with open('input', 'r') as file:
        contents = file.read().split(',')
    
    return contents

def main():
    input_list = get_input()
    input_list = [int(i) for i in input_list]
    max_crabs = max(input_list)
    min_crabs = min(input_list)

    min_fuel = 0

    for i in range(min_crabs, max_crabs+1):
        fuel_cost = 0
        for crab in input_list:
            n = abs(crab - i)
            fuel_cost += n*(n+1)/2
        
        if fuel_cost < min_fuel or min_fuel == 0:
            min_fuel = fuel_cost

    print(min_fuel)

if __name__ == '__main__':
    main()
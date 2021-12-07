def get_input():
    with open('ex', 'r') as file:
        contents = file.read().split(',')
    
    return contents

def main():
    input_list = get_input()
    input_list = [int(i) for i in input_list]
    max_crabs = max(input_list)
    min_crabs = min(input_list)

    fuel_costs = [] 

    for i in range(min_crabs, max_crabs+1):
        distances = []
        nums = []
        for j, crab in enumerate(input_list):
            distances.append(abs(crab - i))
            nums.append(j)
        final_cost = sum([cost*nums[k] for k, cost in enumerate(distances)])
        
        fuel_costs.append(final_cost)

    print(min(fuel_costs))




def find_solution(input_list, pos):
    
    under = pos - 1
    over = pos + 1

    for crab in input_list:
        fuel += abs(crab-pos)

    






if __name__ == '__main__':
    main()
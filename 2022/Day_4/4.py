import re
def get_input():
    with open('input', 'r') as file:
        contents = file.read().strip().split('\n')
    return contents

def main():
    tot = 0
    contents = get_input()
    for line in contents:
        nums = [int(x) for x in re.findall(r'\d+', line)]
        if nums[0] in range(nums[2], nums[3]+1) or nums[1] in range(nums[2], nums[3]+1):
            print(nums)
            tot += 1
        elif nums[2] in range(nums[0], nums[1]+1) or nums[3] in range(nums[0], nums[1]+1):
            print(nums)
            tot += 1
        
    print(tot)


if __name__ == '__main__':
    main()

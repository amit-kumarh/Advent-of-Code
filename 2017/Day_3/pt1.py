def get_input():
    with open('input', 'r') as file:
        contents = file.strip().read().split('\n')

    return contents

def main():
    contents = get_input()

if __name__ == '__main__':
    main()

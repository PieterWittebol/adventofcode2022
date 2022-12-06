input_file = 'input_data.txt'


def read_input():
    read_input_file = open(input_file, 'r')
    read_input_file_data = read_input_file.read()
    input_values = read_input_file_data.split("\n")
    return input_values

def puzzle_1(input_data):
    pass

def puzzle_2(input_data):
    pass

def main():
    read_input_data = read_input()
    puzzle_1(read_input_data)
    puzzle_2(read_input_data)

if __name__ == "__main__":
    main()

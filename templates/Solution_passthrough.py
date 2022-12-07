import setup

day = 0
passthrough = True

def read_input():
    aoc_data = setup.main(passthrough, day)
    input_data = aoc_data.read().split('\n')
    return input_data

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

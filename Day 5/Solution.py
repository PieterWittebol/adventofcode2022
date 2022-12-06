input_file = 'input_data.txt'

def set_stacks_value():
    stacks = [['F', 'H', 'M', 'T', 'V', 'L', 'D'],
            ['P', 'N', 'T', 'C', 'J', 'G', 'Q', 'H'],
            ['H', 'P', 'M', 'D', 'S', 'R'],
            ['F', 'V', 'B', 'L'],
            ['Q', 'L', 'G', 'H', 'N'],
            ['P', 'M', 'R', 'G', 'D', 'B', 'W'],
            ['Q', 'L', 'H', 'C', 'R', 'N', 'M', 'G'],
            ['W', 'L', 'C'],
            ['T', 'M', 'Z', 'J', 'Q', 'L', 'D', 'R']]
    return stacks

def read_input():
    read_input_file = open(input_file, 'r')
    input_values = read_input_file.readlines()[10:]
    return input_values

def puzzle_1(input_data):
    stacks = set_stacks_value()
    for instruction in input_data:
        instruction = instruction.strip()
        amount_crate_to_move = int(instruction.split(' ')[2 - 1])
        from_stack = int(instruction.split(' ')[4 - 1]) - 1
        to_stack = int(instruction.split(' ')[6 - 1]) - 1
        for crate_to_move in range(0, amount_crate_to_move):
            # print(f'Moving crate number {crate_to_move} from {from_stack} to {to_stack}')
            stacks[to_stack].insert(0, stacks[from_stack].pop(0))
    top_crates = "".join([crate[0] for crate in stacks])
    print(f'Puzzle 1\nThe top crates are: {top_crates}')

def puzzle_2(input_data):
    stacks = set_stacks_value()
    for instruction in input_data:
        instruction = instruction.strip()
        amount_crate_to_move = int(instruction.split(' ')[2 - 1])
        from_stack = int(instruction.split(' ')[4 - 1]) - 1
        to_stack = int(instruction.split(' ')[6 - 1]) - 1
        for crate_to_move in range(0, amount_crate_to_move, 1):
            crate_index = amount_crate_to_move - crate_to_move - 1
            # print(f'Moving crate number {crate_to_move} from index {crate_index} from stack {from_stack} to stack {to_stack}')
            stacks[to_stack].insert(0, stacks[from_stack].pop(crate_index))
    top_crates = "".join([crate[0] for crate in stacks])
    print(f'Puzzle 2\nThe top crates are: {top_crates}')

def main():
    read_input_data = read_input()
    puzzle_1(read_input_data)
    puzzle_2(read_input_data)

if __name__ == "__main__":
    main()

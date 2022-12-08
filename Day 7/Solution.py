import setup

day = 7
passthrough = True

def read_input():
    aoc_data = setup.main(passthrough, day)
    input_data = aoc_data.read().strip().splitlines()
    return input_data

def instruction_parser(input_data):
    for line in input_data:
        match_output = []
        match line[0]:
            case '$':
                ls = line[2:4]
                if line[2:4] == 'cd':
                    file_size_count = 0
                    cd = line[2:].split()
                # match_output = ("Command", command)
            case 'd':
                directory = line[4:]
                # match_output = ("Directory", directory)
            case _:
                file = line.split()
                file_size_count += file[1]
                # match_output = ("File", file)
        # instruction_list.append(match_output)
    # return instruction_list

def puzzle_1(input_data):
    instruction_data = instruction_parser(input_data)
    print(f"{instruction_data}")

def puzzle_2(input_data):
    pass

def main():
    read_input_data = read_input()
    puzzle_1(read_input_data)
    puzzle_2(read_input_data)


if __name__ == "__main__":
    main()

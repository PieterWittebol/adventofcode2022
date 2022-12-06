input_file = 'input_data.txt'


def read_input():
    read_input_file = open(input_file, 'r')
    read_input_file_data = read_input_file.read()
    input_values = read_input_file_data.split("\n")
    return input_values

def find_overlap(assignments):
    assignment_overlap_contain_count = 0
    assignment_overlap_count = 0
    for assignment in assignments:
        elf_1_assignment, elf_2_assignment = assignment.split(',')
        elf_1_assignment_start, elf_1_assignment_end = elf_1_assignment.split('-')
        elf_2_assignment_start, elf_2_assignment_end = elf_2_assignment.split('-')
        elf_1_assignment_set = set(range(int(elf_1_assignment_start), int(elf_1_assignment_end) + 1))
        elf_2_assignment_set = set(range(int(elf_2_assignment_start), int(elf_2_assignment_end) + 1))
        assignment_intersection = elf_1_assignment_set & elf_2_assignment_set
        assignment_subset = elf_1_assignment_set <= elf_2_assignment_set
        assignment_superset = elf_1_assignment_set >= elf_2_assignment_set
        if assignment_intersection:
            assignment_overlap_count += 1
            # print(f"Assignments overlap for sections: {assignment_intersection}")
            if assignment_subset:
                # print("Assignments elf 1 done by elf 2")
                assignment_overlap_contain_count += 1
            if assignment_superset and not assignment_subset:
                # print("Assignments elf 2 done by elf 1")
                assignment_overlap_contain_count += 1
    return assignment_overlap_contain_count, assignment_overlap_count

def puzzle_1(input_data):
    assignment_overlap_contain_count, assignment_overlap_count = find_overlap(input_data)
    print(f"Puzzle 1\nAssignments fully contain the other's {assignment_overlap_contain_count} times")

def puzzle_2(input_data):
    assignment_overlap_contain_count, assignment_overlap_count = find_overlap(input_data)
    print(f"Puzzle 2\nAssignments overlap {assignment_overlap_count} times")

def main():
    read_input_data = read_input()
    puzzle_1(read_input_data)
    puzzle_2(read_input_data)

if __name__ == "__main__":
    main()

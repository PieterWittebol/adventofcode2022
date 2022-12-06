import os


input_file = 'input_data.txt'
input_file_to_list = []
rugsack_comp_list = []
compartment_items = []
duplicate_items = []
priority_list = []
badge_groups = []
common_items_per_badge_group = []

def read_input():
    read_input_file = open(input_file, 'r')
    read_input_file_data = read_input_file.read()
    input_values = read_input_file_data.split("\n")
    return input_values

def define_badge_groups(input_values):
    badge_group = ()
    for line in input_values:
        badge_group = badge_group + (line, )
        if len(badge_group) == 3:
            badge_groups.append(badge_group)
            badge_group = ()
    return badge_groups

def split_compartments(input_values):
    for line in input_values:
        length_rugsack_string = len(line)
        if length_rugsack_string % 2 == 0:
            rugsack_comp_1_slice = slice(0, length_rugsack_string // 2)
            rugsack_comp_2_slice = slice(length_rugsack_string // 2, length_rugsack_string)
            rugsack_comp_1 = line[rugsack_comp_1_slice]
            rugsack_comp_2 = line[rugsack_comp_2_slice]
            rugsack_comps_split = (rugsack_comp_1, rugsack_comp_2)
            rugsack_comp_list.append(rugsack_comps_split)
    return rugsack_comp_list

def items_compartments(rugsack_compartments):
    for compartment in rugsack_compartments:
        compartment_1_items = [*compartment[0]]
        compartment_2_items = [*compartment[1]]
        compartments_split_items = (compartment_1_items, compartment_2_items)
        compartment_items.append(compartments_split_items)
    return compartment_items

def compare_compartments(compartment_item_lists):
    for rugsack in compartment_item_lists:
        compartment_1_items, compartment_2_items = rugsack
        common_items = set(compartment_1_items) & set(compartment_2_items)
        duplicate_items.append(common_items)
    return duplicate_items

def priority_definer(duplicate_items):
    sum_item_priorities = 0
    priority_list = []
    for duplicate_item in duplicate_items:
        for character in duplicate_item:
            if character.isupper():
                priority_list.append(ord(character) - 38)
            elif character.islower():
                priority_list.append(ord(character) - 96)
    for priority_items in range(0, len(priority_list)):
        sum_item_priorities = sum_item_priorities + priority_list[priority_items]
    return sum_item_priorities

def common_between_elves(badge_groups):
    for badge_group in badge_groups:
        elf_1, elf_2, elf_3 = badge_group
        common_items_per_badge_group.append(set(elf_1) & set(elf_2) & set(elf_3))
    return common_items_per_badge_group

def puzzle_1(read_input_data):
    all_rugsack_contents = split_compartments(read_input_data)
    all_rugsack_compartments_items = items_compartments(all_rugsack_contents)
    compartment_duplicate_items = compare_compartments(all_rugsack_compartments_items)
    puzzle_1_priority_sum = priority_definer(compartment_duplicate_items)
    print(f"Puzzle 1\nThe total sum of priority item types: {puzzle_1_priority_sum}\n")

def puzzle_2(read_input_data):
    elf_groups = define_badge_groups(read_input_data)
    common_items = common_between_elves(elf_groups)
    puzzle_2_priority_sum = priority_definer(common_items)
    print(f"Puzzle 2\nThe total sum of priority items per badge group: {puzzle_2_priority_sum}")

def main():
    read_input_data = read_input()
    puzzle_1(read_input_data)
    puzzle_2(read_input_data)

if __name__ == "__main__":
    main()

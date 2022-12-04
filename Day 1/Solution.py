fileLocation = 'input_data.txt'
calories_list = []
elf_list = []
count = 0
total_calories = 0

with open(fileLocation, 'r') as input_values:
    for line in input_values:
        try:
            meal_calories = int(line)
            total_calories += meal_calories
        except ValueError:
            calories_list.append(total_calories)
            elf_list.append(count)
            count = count + 1
            total_calories = 0

strongest_elf_load = max(calories_list)
strongest_elf_number = calories_list.index(strongest_elf_load)

sorted_elf_tuple = zip(calories_list, elf_list)
top_three_elves = sorted(sorted_elf_tuple, reverse=True)[:3]
top_three_elves_numbers = [i[1] for i in top_three_elves]
combined_top_three_elves_load = sum([i[0] for i in top_three_elves])

print(f"Elf number {strongest_elf_number} is carrying the highest calorie load ({strongest_elf_load}).")
print(f"The top three elves are:{top_three_elves_numbers} and they are carrying {combined_top_three_elves_load} calories combined.")

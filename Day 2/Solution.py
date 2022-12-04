# Lose = 0
# Draw = 3
# Win = 6
# Puzzle 1
# Rock = A = X = 1
# Paper = B = Y = 2
# Scissors = C = Z = 3
# A: loses against Y, draws against X, beats Z
# B: loses against Z, draws against Y, beats X
# C: loses against X, draws against Z, beats Y
# Puzzle 2
# Rock = A = 1
# Paper = B = 2
# Scissors = C = 3
# X = you lose
# Y = draw
# Z = you win
# A: loses (Z) against Paper (Y), draws (Y) against Rock (X), beats (X) Scissors (Z)
# B: loses (Z) against Scissors (Z), draws (Y) against Paper (Y), beats (X) Rock (X)
# C: loses (Z) against Rock (X), draws (Y) against Scissors (Z), beats (X) Paper (Y)
input_file = 'input_data.txt'
round_values_list_1 = []
round_values_list_2 = []
puzzle_2_lookup_dictionary = {'A': {'X': 'Z', 'Y': 'X', 'Z': 'Y'},
                              'B': {'X': 'X', 'Y': 'Y', 'Z': 'Z'},
                              'C': {'X': 'Y', 'Y': 'Z', 'Z': 'X'}}


def puzzle_1(rps_game_input_values_adversary, rps_game_input_values_you):
    print("Puzzle 1")
    rps_game_round_results = list(map(rps_game, rps_game_input_values_adversary, rps_game_input_values_you))
    return rps_game_round_results


def puzzle_2(rps_game_input_values_adversary, rps_game_round_outcomes):
    print("Puzzle 2")
    rps_game_round_values_you = []
    for rps_game_input_value_adversary, rps_game_round_outcome in zip(rps_game_input_values_adversary, rps_game_round_outcomes):
        rps_game_round_value_you = puzzle_2_lookup_dictionary[rps_game_input_value_adversary][rps_game_round_outcome]
        rps_game_round_values_you.append(rps_game_round_value_you)
    rps_game_round_results = list(map(rps_game, rps_game_input_values_adversary, rps_game_round_values_you))

    return rps_game_round_results


def rps_game(adversary_round_value, you_round_value):
    round_score_adversary = 0
    round_score_you = 0
    if adversary_round_value == 'A':
        round_score_adversary = round_score_adversary + 1
    if adversary_round_value == 'B':
        round_score_adversary = round_score_adversary + 2
    if adversary_round_value == 'C':
        round_score_adversary = round_score_adversary + 3
    if you_round_value == 'X':
        round_score_you = round_score_you + 1
    if you_round_value == 'Y':
        round_score_you = round_score_you + 2
    if you_round_value == 'Z':
        round_score_you = round_score_you + 3

    rps_game_round_values = adversary_round_value + you_round_value
    match rps_game_round_values:
        case 'AY' | 'BZ' | 'CX':  # You win
            round_score_you = round_score_you + 6
            round_score_adversary = round_score_adversary + 0
            return round_score_adversary, round_score_you
        case 'AX' | 'BY' | 'CZ':  # Draw
            round_score_you = round_score_you + 3
            round_score_adversary = round_score_adversary + 3
            return round_score_adversary, round_score_you
        case 'AZ' | 'BX' | 'CY':  # You lose
            round_score_you = round_score_you + 0
            round_score_adversary = round_score_adversary + 6
            return round_score_adversary, round_score_you


def calculate_rps_total_game_score(rps_game_round_results):
    total_score_adversary = 0
    total_score_you = 0
    for round_result in rps_game_round_results:
        total_score_adversary += round_result[0]
        total_score_you += round_result[1]

    print(f"total_score_adversary: {total_score_adversary}")
    print(f"total_score_you: {total_score_you}")


def read_input():
    with open(input_file, 'r') as input_values:
        for line in input_values:
            round_values = line.split()
            round_values_list_1.append(round_values[0])
            round_values_list_2.append(round_values[1])
        return round_values_list_1, round_values_list_2


def main():
    rps_game_input_values_1, rps_game_input_values_2 = read_input()
    calculate_rps_total_game_score(puzzle_1(rps_game_input_values_1, rps_game_input_values_2))
    print('\n')
    calculate_rps_total_game_score(puzzle_2(rps_game_input_values_1, rps_game_input_values_2))


if __name__ == "__main__":
    main()

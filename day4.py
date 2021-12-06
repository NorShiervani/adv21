import numpy as np

def day_4():
    bingo_numbers = []
    user_numbers_array = []

    with open('advent/input4.txt') as f:
        user_numbers = []
        for i, line in enumerate(f.readlines()):
            line = " ".join(line.split())
            if i == 0:
                bingo_numbers = line.split(',')
            elif i > 1:
                if line:
                    user_numbers.append(line.split(' '))
                if (not line or len(user_numbers) == 5) and user_numbers:
                    user_numbers_array.append(user_numbers)
                    user_numbers = []

    winning_number, unmarked_sum = get_last_winner(bingo_numbers, user_numbers_array, None)
    if winning_number and unmarked_sum:
        score = winning_number * unmarked_sum
        print(score)
    else:
        print('no winner lol')

# Part 1
def get_winner(bingo_numbers, user_numbers_data):
    for i, bingo_number in enumerate(bingo_numbers):
        for user_numbers in user_numbers_data:
            winning_numbers_row = get_winning_numbers(i, bingo_numbers, user_numbers, True)
            if winning_numbers_row:
                return winning_numbers_row
            winning_numbers_column = get_winning_numbers(i, bingo_numbers, user_numbers, False)
            if winning_numbers_column:
                return winning_numbers_column
    
    return None

# Part 2
def get_last_winner(bingo_numbers, user_numbers_data, last_winner):
    for i, bingo_number in enumerate(bingo_numbers):
        for user_numbers in user_numbers_data:
            last_winner_row = get_winning_numbers(i, bingo_numbers, user_numbers, True)
            if (last_winner_row):
                user_numbers_data.remove(user_numbers)
                return get_last_winner(bingo_numbers, user_numbers_data, last_winner_row)
            last_winner_column = get_winning_numbers(i, bingo_numbers, user_numbers, False)
            if (last_winner_column):
                user_numbers_data.remove(user_numbers)
                return get_last_winner(bingo_numbers, user_numbers_data, last_winner_column)

    return last_winner


def get_winning_numbers(bingo_index, bingo_numbers, user_numbers, check_rows):
    for numbers in user_numbers if check_rows else np.array(user_numbers).T:  # Check rows or columns
        if all(number in bingo_numbers[:bingo_index+1] for number in numbers): # Check if its the winning numbers
            return int(bingo_numbers[bingo_index]), get_unmarked_numbers_sum(bingo_numbers[:bingo_index+1], user_numbers)


def get_unmarked_numbers_sum(bingo_numbers, user_numbers):
    sum = 0
    for numbers_row in user_numbers:
        for number in numbers_row:
            if number not in bingo_numbers:
                sum += int(number)

    return sum

day_4()
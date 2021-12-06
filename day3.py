from typing import Counter
import numpy as np

def day_3_part1():
    arr = []
    while True:
        input_ = input()
        if not input_:
            break
        arr.append(list(input_))

    gamma_rate = ''
    epsilon_rate = ''
    for np_arr in np.array(arr).T:
        most_common = Counter(np_arr).most_common(1)[0][0]
        gamma_rate += most_common
        epsilon_rate += str(1 - int(most_common))

    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    print(power_consumption)


def day_3_part2():
    arr = []
    while True:
        input_ = input()
        if not input_:
            break
        arr.append(list(input_))

    oxygen_generator_rating = get_rating(arr.copy(), 0, '1')
    co2_scrubber_rating = get_rating(arr.copy(), 0, '0')

    life_support_rating = int(''.join(oxygen_generator_rating[0]), 2) * int(''.join(co2_scrubber_rating[0]), 2)
    print(life_support_rating)


def get_rating(arr, count, target_bit):
    if len(arr) <= 1:
        return arr
    bit_sequence = np.array(arr).T[count]
    equal_common = (bit_sequence == '1').sum() == (bit_sequence == '0').sum()
    most_common = Counter(bit_sequence).most_common(1)[0][0] if target_bit == '1' else Counter(bit_sequence).most_common()[-1][0]
    most_common = target_bit if equal_common else most_common
    for e in arr[:]:
        if e[count] != most_common:
            arr.remove(e)
    count += 1
    return get_rating(arr, count, target_bit)

day_3_part2()
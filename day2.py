def day_2_part1():
    dict = {'forward': 0, 'up': 0, 'down': 0}
    while True:
        input_ = input()
        if not input_:
            break
        values = input_.split(' ')
        dict[values[0]] += int(values[1])

    res = dict['forward'] * (dict['down'] - dict['up'])
    print(res)


def day_2_part2():
    dict = {'forward': 0, 'depth': 0, 'down': 0, 'up': 0}
    while True:
        input_ = input()
        if not input_:
            break
        values = input_.split(' ')
        if values[0] == 'forward':
            dict['forward'] += int(values[1])
            dict['depth'] += int(values[1]) * (dict['down'] - dict['up'])
        else:
            dict[values[0]] += int(values[1])

    res = dict['forward'] * dict['depth']

    print(res)

day_2_part2()
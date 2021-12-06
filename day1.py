def day_1_part1():
    prev_depth = -1
    count = 0
    while True:
        input_ = input()
        if not input_:
            break
        new_depth = int(input_)
        if prev_depth < new_depth and prev_depth != -1:
            count += 1
        prev_depth = new_depth
    print(count)


def day_1_part2():
    arr = []
    while True:
        input_ = input()
        if not input_:
            break
        arr.append(int(input_))

    leftovers = len(arr) % 3
    filtered_arr = arr[:-leftovers] if leftovers else arr
    prev_sum = -1
    count = 0

    for i, num in enumerate(filtered_arr):
        if i+2 > len(arr)-1:
            continue
        new_sum = sum([arr[i], arr[i+1], arr[i+2]])
        if prev_sum < new_sum and prev_sum != -1:
            count += 1
        prev_sum = new_sum

    print(count)

day_1_part2()
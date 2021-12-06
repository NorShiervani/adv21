def day6():
    timers = list(map(int, input().split(',')))

    for x in range(80):
        for i, timer in enumerate(timers[:]):
            if timers[i] == 0:
                timers[i] = 6
                timers.append(8)
            else:
                timers[i] = timers[i] - 1

    print(len(timers))

day6()
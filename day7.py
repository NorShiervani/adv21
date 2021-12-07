def day7_part1():
    positions = list(map(int, input().split(',')))
    least_fuel = -1

    for new_position in range(min(positions), max(positions)):
        fuel = 0
        for position in positions:
            fuel += abs(position-new_position)
        
        if fuel < least_fuel or least_fuel == -1:
            least_fuel = fuel
            
    print(least_fuel)

def day7_part2():
    positions = list(map(int, input().split(',')))
    least_fuel = -1

    for new_position in range(min(positions), max(positions)):
        fuel = 0
        for position in positions:
            distance = abs(position-new_position)
            fuel += int((distance*(distance+1))/2)
        
        if fuel < least_fuel or least_fuel == -1:
            least_fuel = fuel
            
    print(least_fuel)

day7_part2()
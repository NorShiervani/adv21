import collections as coll

def day_5(allow_diagonal_lines):
    marked_points = []
    with open('advent/input5.txt') as f:
        for i, line in enumerate(f.readlines()):
            input_ = line
            if not input_:
                break

            points = [int(s)for s in input_.replace(' -> ', ',').split(',')]
            if (points[0] == points[2] or points[1] == points[3]) or allow_diagonal_lines:
                points = list(map(int, points))
                marked_points += get_points(points[0], points[1], points[2], points[3])

    print(len([item for item, count in coll.Counter(marked_points).items() if count > 1]))

# Bresenham's line algorithm
def get_points(x1, y1, x2, y2):
    points_in_line = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1
    is_horizontal = dx > dy

    if is_horizontal:
        err = dx / 2.0
        while x != x2: # Append points while start x hasnt reached end x
            points_in_line.append((x, y))
            err -= dy
            if err < 0: # Adjust when diagonal line
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y2:
            points_in_line.append((x, y))
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    points_in_line.append((x, y))
    return points_in_line


day_5(True)
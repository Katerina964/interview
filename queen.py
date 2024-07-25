weidht = 8
height = 8

desk = [["."] * weidht for i in range(height)]

def queen_steps(queen_position):
    queen_row = queen_position[0]
    queen_point = queen_position[1]
    offset = queen_row - queen_point
    
    a, b = queen_row, queen_point
    c, d = queen_row, queen_point

    for row in range(0, height):
        for point in range(0, weidht):
            if (
                point == queen_point
                or row == queen_row
                or row == (point + offset)
            ):
                desk[row][point] = "*"

            if c + 1 == row and d - 1 == point:
                desk[row][point] = "*"
                c, d = c + 1, d - 1

    for row in reversed(range(0, height)):
        for point in range(0, weidht):
            if a - 1 == row and b + 1 == point:
                desk[row][point] = "*"
                a, b = a - 1, b + 1

    desk[queen_row][queen_point] = "Q"
    return desk


result = queen_steps((5, 4))
for each in result:
    print(*each)

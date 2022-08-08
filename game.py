import numpy as np


def print_grid():
    print()
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] is None:
                print("-", end=" ")
            else:
                print(grid[row][col], end=" ")
        print()


def reset_grid():
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] is not None:
                grid[row][col] = None


def put(item):
    count = 0
    reset_grid()
    for row in range(len(grid)):
        for col in range(len(grid)):
            index_ = row + col
            if row == 1:
                index_ += 3
            elif row == 2:
                index_ += 6
            elif row == 3:
                index_ += 9
            if item[count] == index_:
                grid[row][col] = 0
                count += 1
                if count > 3:
                    count = 0
                    break
    print_grid()


def rotate(items):
    for item in items:
        put(item)


grid = np.array([[None, None, None, None],
                 [None, None, None, None],
                 [None, None, None, None],
                 [None, None, None, None]])
o_piece = [[5, 6, 9, 10]]
i_piece = [[1, 5, 9, 13], [4, 5, 6, 7]]
s_piece = [[5, 6, 8, 9], [5, 9, 10, 14]]  #
z_piece = [[4, 5, 9, 10], [2, 5, 6, 9]]
l_piece = [[1, 5, 9, 10], [2, 4, 5, 6], [1, 2, 6, 10], [4, 5, 6, 8]]
j_piece = [[2, 6, 9, 10], [4, 5, 6, 10], [1, 2, 5, 9], [0, 4, 5, 6]]
t_piece = [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]]
piece = input()  # I J L O S T Z
print_grid()
"""
00 01 02 03
10 11 12 13
20 21 22 23
30 31 32 33
"""

if piece == 'I':
    rotate(i_piece)
    put(i_piece[0])
elif piece == 'J':
    rotate(j_piece)
    put(j_piece[0])
elif piece == 'L':
    rotate(l_piece)
    put(l_piece[0])
elif piece == 'O':
    put(o_piece[0])
    rotate(o_piece)
    rotate(o_piece)
    rotate(o_piece)
    rotate(o_piece)
elif piece == 'S':
    rotate(s_piece)
    rotate(s_piece)
    put(s_piece[0])
elif piece == 'T':
    rotate(t_piece)
    put(t_piece[0])
elif piece == 'Z':
    rotate(z_piece)
    rotate(z_piece)
    put(z_piece[0])
else:
    print("Unknown piece!")

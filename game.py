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
            index = col + 4 * row
            # if row == 1:
            #     index += 3
            # elif row == 2:
            #     index += 6
            # elif row == 3:
            #     index += 9
            if item[count] == index:
                grid[row][col] = 0
                count += 1
                if count > 3:
                    count = 0
                    break
    print_grid()


def put2(item, num_of_time):
    for _ in range(num_of_time):
        put(item)


def rotate(items, num_of_times):
    index = 1
    count = 0
    while count < num_of_times:
        item = items[index]
        put(item)
        index += 1
        if index == len(items):
            index = 0
        count += 1


grid = np.full((4, 4), None)


def main():
    o_piece = [[5, 6, 9, 10]]
    i_piece = [[1, 5, 9, 13], [4, 5, 6, 7]]
    s_piece = [[5, 6, 8, 9], [5, 9, 10, 14]]  #
    z_piece = [[4, 5, 9, 10], [2, 5, 6, 9]]
    l_piece = [[1, 5, 9, 10], [2, 4, 5, 6], [1, 2, 6, 10], [4, 5, 6, 8]]
    j_piece = [[2, 6, 9, 10], [4, 5, 6, 10], [1, 2, 5, 9], [0, 4, 5, 6]]
    t_piece = [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]]
    piece = input().upper()  # I J L O S T Z
    print_grid()

    if piece == 'I':
        put(i_piece[0])
        rotate(i_piece, 4)
    elif piece == 'J':
        put(j_piece[0])
        rotate(j_piece, 4)
    elif piece == 'L':
        put(l_piece[0])
        rotate(l_piece, 4)
    elif piece == 'O':
        put2(o_piece[0], 5)
    elif piece == 'S':
        put(s_piece[0])
        rotate(s_piece, 4)
    elif piece == 'T':
        put(t_piece[0])
        rotate(t_piece, 4)
    elif piece == 'Z':
        put(z_piece[0])
        rotate(z_piece, 4)
    else:
        print("Unknown piece!")


if __name__ == '__main__':
    main()

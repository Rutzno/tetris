import numpy as np
"""
__author__ = "Mack_TB"
__since__ = "11/8/2021"
__version__ = "1.0.3"
"""


class Board:
    n = 0  # number of instances of this class
    symbols = {
        'O': [[4, 5, 14, 15]],
        'I': [[4, 14, 24, 34], [3, 4, 5, 6]],
        'S': [[4, 5, 13, 14], [4, 14, 15, 25]],
        'Z': [[4, 5, 15, 16], [5, 14, 15, 24]],
        'L': [[4, 14, 24, 25], [5, 13, 14, 15], [4, 5, 15, 25], [4, 5, 6, 14]],
        'J': [[5, 15, 24, 25], [3, 4, 5, 15], [4, 5, 14, 24], [4, 14, 15, 16]],
        'T': [[4, 14, 15, 24], [4, 13, 14, 15], [5, 14, 15, 25], [4, 5, 6, 15]]
    }

    def __new__(cls, *args, **kwargs):
        if cls.n == 0:
            cls.n += 1
            return object.__new__(cls)

    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.grid = np.full((height, width), None)
        self.current_piece = []  # like 'I': [[4, 14, 24, 34], [3, 4, 5, 6]]
        self.current_piece_index = 0

    def rotate(self):
        if self.is_piece_onfloor():
            self.print_grid()
        else:
            self.current_piece_index += 1
            if self.current_piece_index == len(self.current_piece):
                self.current_piece_index = 0  # reset: go back to the first index
            item = self.current_piece[self.current_piece_index]
            self.put(item, display=False)
            self.go_down()

    def go_down(self):
        self.move(10)

    def to_left(self):
        if any(self.check_left_border()):
            self.go_down()
        else:
            self.move(9)

    def to_right(self):
        if any(self.check_right_border()):
            # print("border_right")
            self.go_down()
        else:
            self.move(11)

    # shift all the element of a piece i.e. the unique piece and its rotated pieces
    def move(self, step):
        if self.is_piece_onfloor():
            # print("floor")
            self.print_grid()
        else:
            for i in range(len(self.current_piece)):
                for j in range(len(self.current_piece[i])):
                    self.current_piece[i][j] += step
            self.put(self.current_piece[self.current_piece_index])

    def put(self, item, display=True):
        index = 0
        self.reset_grid()
        for row in range(self.height):
            for col in range(self.width):
                value = int(f"{row}{col}")
                if item[index] == value:
                    self.grid[row][col] = 0
                    index += 1
                    if index > 3:
                        index = 0
                        break
        if display:
            self.print_grid()

    def print_grid(self):
        print()
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] is None:
                    print("-", end="") if col == self.width-1 else print("-", end=" ")
                else:
                    print(self.grid[row][col], end="") if col == self.width-1 else print(self.grid[row][col], end=" ")
                    # print(self.grid[row][col], end=" ")
            print()

    def reset_grid(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] is not None:
                    self.grid[row][col] = None

    def check_left_border(self):
        return [True if n % 10 == 0 else False
                for n in self.current_piece[self.current_piece_index]]

    def check_right_border(self):
        return [True if n % 10 == 9 else False
                for n in self.current_piece[self.current_piece_index]]

    def is_piece_onfloor(self):
        return any(True if n // 10 == self.height-1 else False
                   for n in self.current_piece[self.current_piece_index])


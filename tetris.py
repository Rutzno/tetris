import numpy as np
import sys
"""
__author__ = "Mack_TB"
__since__ = "11/8/2021"
__version__ = "1.0.4"
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
        self.preview_piece_item = list()
        # self.last_piece = list()
        self.static_blocks = list()  #

    def rotate(self):
        if self.is_piece_on_floor() or self.is_piece_touch_another():
            self.print_grid()
            if self.is_game_over():
                print("Game Over!")
                sys.exit()
        else:
            self.current_piece_index += 1
            if self.current_piece_index == len(self.current_piece):
                self.current_piece_index = 0  # reset: go back to the first index
            item = self.current_piece[self.current_piece_index]
            self.put(item, display=False)
            self.go_down()

    def go_down(self):
        self.move(10)

    def go_left(self):
        if self.is_piece_on_left_border():
            self.go_down()
        else:
            self.move(9)

    def go_right(self):
        if self.is_piece_on_right_border():
            self.go_down()
        else:
            self.move(11)

    # shift all the element of a piece i.e. the unique piece and its rotated pieces
    def move(self, step):
        if self.is_piece_on_floor() or self.is_piece_touch_another():
            self.print_grid()
            if self.is_game_over():
                print("Game Over!")
                sys.exit()
        else:
            for i in range(len(self.current_piece)):
                for j in range(len(self.current_piece[i])):
                    self.current_piece[i][j] += step
            self.put(self.current_piece[self.current_piece_index])

    def put(self, item, display=True):
        index = 0
        if len(self.preview_piece_item):
            self.remove_preview()
        for row in range(self.height):
            for col in range(self.width):
                value = int(f"{row}{col}")
                if len(item) > 0 and item[index] == value:
                    self.grid[row][col] = 0
                    index += 1
                    if index >= len(item):
                        break
            if index >= len(item):
                break
        if display:
            self.print_grid()
        self.preview_piece_item.clear()
        self.preview_piece_item.extend(item)
        if self.is_piece_on_floor() or self.is_piece_touch_another():
            self.static_blocks.extend(item)

    def print_grid(self):
        # print()
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] is None:
                    print("-", end="") if col == self.width-1 else print("-", end=" ")
                else:
                    print(self.grid[row][col], end="") \
                        if col == self.width-1 else print(self.grid[row][col], end=" ")
            print()
        print()

    def reset_grid(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] is not None:
                    self.grid[row][col] = None

    def remove_preview(self):
        index = 0
        for row in range(self.height):
            for col in range(self.width):
                value = int(f"{row}{col}")
                if self.preview_piece_item[index] == value:
                    self.grid[row][col] = None
                    index += 1
                    if index > 3:
                        index = 0
                        break

    def is_piece_on_left_border(self):
        return any(True if n % 10 == 0 else False
                   for n in self.current_piece[self.current_piece_index])

    def is_piece_on_right_border(self):
        return any(True if n % 10 == 9 else False
                   for n in self.current_piece[self.current_piece_index])

    def is_piece_on_floor(self):
        return any(True if n // 10 == self.height-1 else False
                   for n in self.current_piece[self.current_piece_index])

    def is_row_filled(self):
        count = 0
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] != 0:
                    break
                count += 1
            if count == self.width:
                return [row, True]
            count = 0
        return False

    def break_(self):
        is_ok = self.is_row_filled()
        if is_ok:
            filled_row = is_ok[0]
            value = (self.height - filled_row) * 10
            # disappear blocks
            rows = [i for i in range(filled_row, self.height)]
            i = 0
            while i < len(self.static_blocks):
                if rows.__contains__(self.static_blocks[i] // 10):
                    self.static_blocks.remove(self.static_blocks[i])
                    i -= 1
                i += 1

            self.static_blocks = [i + value for i in self.static_blocks]
            self.reset_grid()
            self.static_blocks.sort()
            self.put(self.static_blocks)
        else:
            print("No rows to break!")

    def is_piece_touch_another(self):
        result = []
        for i in range(len(self.static_blocks)-1, -1, -1):
            for cp in self.current_piece[self.current_piece_index]:
                if abs(self.static_blocks[i] - cp) == 10:
                    result.append(True)
                    break
                else:
                    result.append(False)
        return any(result)

    def is_game_over(self):
        count = 0
        for col in range(self.width):
            for row in range(self.height):
                if self.grid[row][col] != 0:
                    break
                count += 1
            if count == self.height:
                return True
            count = 0
        return False

    def set(self, items):
        self.current_piece.clear()
        self.current_piece.extend(items)
        self.current_piece_index = 0
        self.preview_piece_item = list()
        # print("current_p:", self.current_piece[self.current_piece_index])
        self.put(self.current_piece[self.current_piece_index])


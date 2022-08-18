from tetris import Board
"""
__author__ = "Mack_TB"
__since__ = "8/8/2021"
__version__ = "1.0.4"
"""


def get_piece(symbol):
    result = []
    item = []
    for i in range(len(symbol)):
        for j in range(len(symbol[i])):
            item.append(symbol[i][j])
        result.append(item)
        item = []
    return result


def main():
    width, height = input().split(" ")
    tetris = Board(int(width), int(height))
    tetris.print_grid()
    # piece = input()  # I J L O S T Z
    # tetris.current_piece.extend(Board.symbols[piece])
    # tetris.put(Board.symbols[piece][0])
    while True:
        command = input()
        if command == "piece":
            # there is a moving piece
            piece = input()  # I J L O S T Z
            # if len(tetris.current_piece):
            #     tetris.static_blocks.extend(tetris.current_piece[tetris.current_piece_index])
            # print("static:", tetris.static_blocks)
            items = get_piece(tetris.symbols[piece])
            tetris.set(items)
            # tetris.current_piece.clear()
            # tetris.current_piece.extend(items)
            # tetris.current_piece_index = 0
            # tetris.preview_piece_item = list()
            # print("current_p:", tetris.current_piece[tetris.current_piece_index])
            # tetris.put(tetris.current_piece[tetris.current_piece_index])

        elif command == "exit":
            break
        elif command == "down":
            tetris.go_down()
        elif command == "left":
            tetris.go_left()
        elif command == "right":
            tetris.go_right()
        elif command == "rotate":
            tetris.rotate()
        elif command == "break":
            tetris.break_()
        else:
            print("Unknown command!")
        # if tetris.is_game_over():
        #     break


if __name__ == '__main__':
    main()

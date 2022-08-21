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
    width, height = input("> ").split(" ")
    tetris = Board(int(width), int(height))
    tetris.print_grid()
    while True:
        command = input("> ")
        if command == "piece":
            #   TODO: there is a moving piece
            piece = input("> ")  # I J L O S T Z
            items = get_piece(tetris.symbols[piece])
            tetris.set(items)
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

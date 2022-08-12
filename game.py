from tetris import Board
"""
__author__ = "Mack_TB"
__since__ = "8/8/2021"
__version__ = "1.0.2"
"""


def main():
    piece = input()  # I J L O S T Z
    width, height = input().split(" ")

    tetris = Board(int(width), int(height))
    tetris.print_grid()
    tetris.current_piece.extend(Board.symbols[piece])
    tetris.put(Board.symbols[piece][0])

    while True:
        command = input("\n")
        if command == "exit":
            break
        elif command == "down":
            tetris.go_down()
        elif command == "left":
            tetris.to_left()
        elif command == "right":
            tetris.to_right()
        elif command == "rotate":
            tetris.rotate()
        else:
            print("Unknown command!")


if __name__ == '__main__':
    main()

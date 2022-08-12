from tetris import Board


def main():
    piece = input()  # I J L O S T Z
    dimensions = input().split(" ")

    tetris = Board(int(dimensions[0]), int(dimensions[1]))
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

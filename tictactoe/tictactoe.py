def print_grid(board):
    display = board.replace("_", " ")
    print("---------")
    print("|", " ".join(display[0:3]), "|")
    print("|", " ".join(display[3:6]), "|")
    print("|", " ".join(display[6:9]), "|")
    print("---------")


def check_winner(board):
    wins = [
        board[0:3], board[3:6], board[6:9],
        board[0::3], board[1::3], board[2::3],
        board[0::4], board[2:7:2]
    ]
    if "XXX" in wins:
        return "X wins"
    if "OOO" in wins:
        return "O wins"
    if "_" not in board:
        return "Draw"
    return None


cells = "_________"
current_player = "X"
print_grid(cells)

while True:
    coords = input("Enter the coordinates: ").split()
    try:
        if len(coords) != 2:
            raise ValueError
        row_str, col_str = coords
        row, col = int(row_str), int(col_str)
    except ValueError:
        print("You should enter numbers!")
        continue

    if not (1 <= row <= 3 and 1 <= col <= 3):
        print("Coordinates should be from 1 to 3!")
        continue

    index = (row - 1) * 3 + (col - 1)
    if cells[index] != "_":
        print("This cell is occupied! Choose another one!")
        continue

    cells = cells[:index] + current_player + cells[index + 1:]
    print_grid(cells)

    result = check_winner(cells)
    if result:
        print(result)
        break

    current_player = "O" if current_player == "X" else "X"

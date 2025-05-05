#!/usr/bin/python3

def print_board(board):
    """
    Display the current game board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """
    Check for a winner in the current game board.

    Returns:
        str: "X" or "O" if a player has won, or None otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def is_full(board):
    """
    Check if the board is full (tie condition).

    Returns:
        bool: True if all cells are filled, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    """
    Main game loop for Tic Tac Toe.
    """
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        # Get and validate input
        try:
            row = int(input(f"Enter row (0, 1, 2) for player {current_player}: "))
            col = int(input(f"Enter column (0, 1, 2) for player {current_player}: "))
        except ValueError:
            print("Please enter valid numbers (0, 1, or 2).")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Invalid position. Choose 0, 1, or 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Make move
        board[row][col] = current_player

        # Check for winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # Check for tie
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()

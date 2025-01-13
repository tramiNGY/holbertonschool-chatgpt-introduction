def print_board(board):
    """Print the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Check if there is a winner."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """Run the Tic-Tac-Toe game."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while not check_winner(board):
        print_board(board)
        
        # Input validation for row and column
        valid_input = False
        while not valid_input:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

                # Check if the input is within bounds
                if row not in range(3) or col not in range(3):
                    print("Invalid row or column. Please enter a value between 0 and 2.")
                elif board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                else:
                    valid_input = True  # Input is valid, break out of the loop

            except ValueError:
                print("Invalid input. Please enter numbers for row and column.")

        # Place the player's mark on the board
        board[row][col] = player

        # Switch player after a valid move
        player = "O" if player == "X" else "X"

    print_board(board)
    print(f"Player {player} wins!")

# Run the game
tic_tac_toe()

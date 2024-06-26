def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

def check_winner(board):
    
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return row[0]
    
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    
    return None

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    turns = 0

    while turns < 9:
        print_board(board)
        print(f"Player {player}'s turn.")
        
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        
        if board[row][col] == ' ':
            board[row][col] = player
            turns += 1
        else:
            print("That spot is already taken! Try again.")
            continue
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            return
        
        player = 'O' if player == 'X' else 'X'
    
    print_board(board)
    print("It's a tie!")

tic_tac_toe()

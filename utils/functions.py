def update_current_board(player_coords, current_board):
    # update the current board with the player's move
    row, col = player_coords
    if current_board[row][col] == " ":
        current_board[row][col] = "X"
        return current_board
    return current_board

def check_winner(current_board):
    # check rows
    for row in current_board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return f"{row[0]} wins!"
        
    # check columns
    for col in range(3):
        if current_board[0][col] == current_board[1][col] == current_board[2][col] and current_board[0][col] != " ":
            return f"{current_board[0][col]} wins!"
        
    # check diagonals
    if current_board[0][0] == current_board[1][1] == current_board[2][2] and current_board[0][0] != " ":
        return f"{current_board[0][0]} wins!"
    if current_board[0][2] == current_board[1][1] == current_board[2][0] and current_board[0][2] != " ":
        return f"{current_board[0][2]} wins!"
    
    # check draw
    if all([cell != " " for row in current_board for cell in row]):
        return "Draw!"
    
    return "No winner yet"
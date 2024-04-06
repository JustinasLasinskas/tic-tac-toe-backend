import random
def action(player_move: list, current_board: list):
    AI_placed_o = False
    while AI_placed_o == False:
        random_row = random.randint(0, 2)
        random_col = random.randint(0, 2)
        if current_board[random_row][random_col] == " ":
            current_board[random_row][random_col] = "O"
            AI_placed_o = True
    return current_board
from fastapi import FastAPI
from typing import List

from ai_model import ai
from utils.functions import update_current_board, check_winner

app = FastAPI()

current_board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
        ]

# root page
@app.get("/")
async def root():
    return {"message": "front page of the API"}

# accept player moves
@app.post("/action")
async def player_move(player_coords: List[int], current_board: List[List[str]]):
    row, col = player_coords

    current_board = update_current_board(player_coords, current_board)

    winner = check_winner(current_board)

    if winner == "No winner yet":
        current_board = ai.action(player_coords, current_board)
        winner = check_winner(current_board)

    return {"message": f"Player placed X on row {row}, column {col}", "winner": f"{winner}"}

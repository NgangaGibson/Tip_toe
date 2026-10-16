
import tkinter as tk

window = tk.Tk()
window.title("Unbeatable AI Tic-Tac-Toe")
window.geometry("400x500")
window.resizable(False, False)

board = [" "] * 9
buttons = []
game_over = False

title = tk.Label(
    window,
    text="TIC-TAC-TOE AI",
    font=("Arial", 22, "bold")
)
title.pack(pady=15)

status = tk.Label(
    window,
    text="Your turn: X",
    font=("Arial", 13)
)
status.pack(pady=10)

board_frame = tk.Frame(window)
board_frame.pack()

def check_winner():
    winning_lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_lines:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    return None

def player_move(index):
    global game_over

    if board[index] != " " or game_over:
        return

    board[index] = "X"
    buttons[index].config(text="X", state="disabled")

    winner = check_winner()

    if winner:
        status.config(text="You win!")
        game_over = True
    elif " " not in board:
        status.config(text="It's a draw!")
        game_over = True
    else:
        status.config(text="Computer's turn: O")

def reset_game():
    global board, game_over

    board = [" "] * 9
    game_over = False

    for button in buttons:
        button.config(text=" ", state="normal")

    status.config(text="Your turn: X")

for i in range(9):
    button = tk.Button(
        board_frame,
        text=" ",
        font=("Arial", 24, "bold"),
        width=5,
        height=2,
        command=lambda i=i: player_move(i)
    )
    button.grid(row=i // 3, column=i % 3, padx=3, pady=3)
    buttons.append(button)

restart_button = tk.Button(
    window,
    text="Restart Game",
    font=("Arial", 12),
    command=reset_game
)
restart_button.pack(pady=20)

window.mainloop()

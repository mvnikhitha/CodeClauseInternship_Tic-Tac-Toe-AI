import tkinter as tk
from tkinter import messagebox
import random
board = [[" " for _ in range(3)] for _ in range(3)]

def check_winner(b, player):
    win_states = [
        [b[0][0], b[0][1], b[0][2]],
        [b[1][0], b[1][1], b[1][2]],
        [b[2][0], b[2][1], b[2][2]],
        [b[0][0], b[1][0], b[2][0]],
        [b[0][1], b[1][1], b[2][1]],
        [b[0][2], b[1][2], b[2][2]],
        [b[0][0], b[1][1], b[2][2]],
        [b[0][2], b[1][1], b[2][0]],
    ]
    return [player, player, player] in win_states

# Get empty cells
def get_available_moves():
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

# AI move logic
def ai_move():
    for player in ["O", "X"]:
        for (i, j) in get_available_moves():
            copy = [row[:] for row in board]
            copy[i][j] = player
            if check_winner(copy, player):
                return i, j
    if board[1][1] == " ":
        return 1, 1
    for (i, j) in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if board[i][j] == " ":
            return i, j
    return random.choice(get_available_moves())

# When a button is clicked
def on_click(i, j):
    if board[i][j] == " ":
        board[i][j] = "X"
        buttons[i][j].config(text="X", state="disabled")
        if check_winner(board, "X"):
            messagebox.showinfo("Game Over", "You win!")
            window.quit()
            return
        if not get_available_moves():
            messagebox.showinfo("Game Over", "It's a draw!")
            window.quit()
            return

        ai_i, ai_j = ai_move()
        board[ai_i][ai_j] = "O"
        buttons[ai_i][ai_j].config(text="O", state="disabled")
        if check_winner(board, "O"):
            messagebox.showinfo("Game Over", "AI wins!")
            window.quit()
        elif not get_available_moves():
            messagebox.showinfo("Game Over", "It's a draw!")
            window.quit()

# Create GUI window
window = tk.Tk()
window.title("Tic-Tac-Toe")

buttons = [[None for _ in range(3)] for _ in range(3)]

# Create 3x3 grid of buttons
for i in range(3):
    for j in range(3):
        btn = tk.Button(window, text=" ", width=6, height=3,
                        font=("Arial", 24), command=lambda i=i, j=j: on_click(i, j))
        btn.grid(row=i, column=j)
        buttons[i][j] = btn

window.mainloop()

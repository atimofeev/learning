"""Tic-Tac-Toe game.

№5: 18 Python Projects for your Resume
"""
import random
import tkinter as tk

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
won = False


def button_press(button_id):
    """Handle user button press."""
    if not won:
        if buttons[button_id].cget("text") not in ["X", "O"]:
            buttons[button_id].config(text="X")
            combo_check()
            opponent_move()


def read_buttons():
    """Read button labels into matrix."""
    button_matrix = matrix
    button = 1
    for row in range(3):
        for column in range(3):
            # fill button_matrix with X/O or with digits
            button_matrix[row][column] = (
                button if buttons[button].cget("text") not in ["X", "O"]
                else buttons[button].cget("text")
            )
            button += 1
    return button_matrix


def opponent_move():
    """Move opponent via random button selection."""
    button_matrix = read_buttons()
    available_moves = []
    for row in range(3):
        for column in range(3):
            if button_matrix[row][column] not in ["X", "O"]:
                available_moves.append((row, column))
    if available_moves:
        move_row, move_column = random.choice(available_moves)
        button_id = matrix[move_row][move_column]
        buttons[button_id].config(text="O")
    else:
        result_label.config(text="Game over!")
    combo_check()


def combo_check():
    """Divide button matrix into rows, columns and diagonal lines."""
    button_matrix = read_buttons()
    # Rows and columns
    for i in range(3):
        row = button_matrix[i]
        column = [button_matrix[j][i] for j in range(3)]
        check_win(row)
        check_win(column)
    # Diagonals
    diag1 = [button_matrix[i][i] for i in range(3)]
    diag2 = [button_matrix[i][2-i] for i in range(3)]
    check_win(diag1)
    check_win(diag2)


def check_win(combo):
    """Check if win conditions were met on requested row,column or diagonal."""
    global won
    if all(x == combo[0] for x in combo):
        won = True
        if combo[0] == "X":
            result_label.config(text="You won!")
        elif combo[0] == "O":
            result_label.config(text="You lose!")


def reset_buttons():
    """Reset game state."""
    global won
    won = False
    result_label.config(text="")
    for i in range(1, 10):
        buttons[i].config(text="   ")


root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("150x150")

button_frame = tk.Frame(root)
button_frame.pack()

buttons = {
    1: tk.Button(button_frame, text="   ", command=lambda: button_press(1)),
    2: tk.Button(button_frame, text="   ", command=lambda: button_press(2)),
    3: tk.Button(button_frame, text="   ", command=lambda: button_press(3)),
    4: tk.Button(button_frame, text="   ", command=lambda: button_press(4)),
    5: tk.Button(button_frame, text="   ", command=lambda: button_press(5)),
    6: tk.Button(button_frame, text="   ", command=lambda: button_press(6)),
    7: tk.Button(button_frame, text="   ", command=lambda: button_press(7)),
    8: tk.Button(button_frame, text="   ", command=lambda: button_press(8)),
    9: tk.Button(button_frame, text="   ", command=lambda: button_press(9))
}

buttons[1].grid(row=0, column=0)
buttons[2].grid(row=0, column=1)
buttons[3].grid(row=0, column=2)
buttons[4].grid(row=1, column=0)
buttons[5].grid(row=1, column=1)
buttons[6].grid(row=1, column=2)
buttons[7].grid(row=2, column=0)
buttons[8].grid(row=2, column=1)
buttons[9].grid(row=2, column=2)

bottom_frame = tk.Frame(root)
bottom_frame.pack()

result_label = tk.Label(bottom_frame, text="")
result_label.pack()

reset_button = tk.Button(bottom_frame, text="Reset", command=reset_buttons)
reset_button.pack()

root.mainloop()

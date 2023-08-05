# 18 Python Projects for your Resume
# №4: Rock Paper Scissors

import random, tkinter as tk

def game(user_move):
    moves = [
        "rock",
        "paper",
        "scissors"
    ]
    win_combos = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    opponent_move = random.choice(moves)
    if user_move == opponent_move:
        result = "Stalemate"
        color = "White"
    elif win_combos[user_move] == opponent_move:
        result = "Win!"
        color = "Green"
    else:
        result = "Loss!"
        color = "Red"
    opponent_label.config(text=f"Opponent: {opponent_move}")
    result_label.config(text=result, bg=color)

# Create window with buttons and labels
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("190x125")

frame = tk.Frame(root)
frame.pack()

rock_button = tk.Button(frame, text="Rock", command=lambda: game("rock"))
rock_button.pack(side=tk.LEFT)

paper_button = tk.Button(frame, text="Paper", command=lambda: game("paper"))
paper_button.pack(side=tk.LEFT)

scissors_button = tk.Button(frame, text="Scissors", command=lambda: game("scissors"))
scissors_button.pack(side=tk.LEFT)

vertical_frame = tk.Frame(root)
vertical_frame.pack()

exit_button  = tk.Button(vertical_frame, text="Exit", command=root.quit)
exit_button.pack()

opponent_label = tk.Label(vertical_frame, text="Opponent: ")
opponent_label.pack()

result_label = tk.Label(vertical_frame, text="")
result_label.pack()

# Start main event loop
root.mainloop()
# 18 Python Projects for your Resume
# №8 Dice Roll

import random, tkinter as tk

def roll():
    result = random.randint(1,6)
    result_label.config(text=result)

frame = tk.Frame()
frame.pack()

result_label = tk.Label(frame, text="")
result_label.pack()

roll_button = tk.Button(frame, text="Roll", command=roll)
roll_button.pack()

frame.mainloop()
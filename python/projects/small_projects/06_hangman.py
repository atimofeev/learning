"""Hangman game.

№6: 18 Python Projects for your Resume
"""
import random
import tkinter as tk

WORD_LIST = ["elephant", "guitar", "computer", "umbrella", "kangaroo",
             "bicycle", "mountain", "pineapple", "waterfall", "chocolate"]


def draw_hangman(attempts):
    """Draw hanged man in stages."""
    stages = [
        """
           -----
           |
           |
           |
           |
           |
        """,
        """
           -----
           |   |
           |
           |
           |
           |
        """,
        """
           -----
           |   |
           |   O
           |
           |
           |
        """,
        """
           -----
           |   |
           |   O
           |   |
           |
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           |
        """
    ]
    return stages[attempts]


def guess(letter):
    """Game logic."""
    global attempts
    letter_entry.delete(0, 'end')
    current_word_label = word_label.cget("text")
    if (
        not letter
        or letter.isdigit()
        or letter in current_word_label
        or "_" not in current_word_label
        or len(letter) > 1
        or attempts >= 7
    ):
        return

    if letter in word:
        word_label_tmp = ''
        for i in range(len(word)):
            if word[i] == letter:
                word_label_tmp += letter
            elif current_word_label[i] != '_':
                word_label_tmp += current_word_label[i]
            else:
                word_label_tmp += '_'
        word_label.config(text=word_label_tmp)

        if "_" not in word_label_tmp:
            hangman_text.delete('1.0', tk.END)
            hangman_text.insert(tk.END, "Congratulations! You've won.")
    else:
        attempts += 1
        hangman_text.delete('1.0', tk.END)
        hangman_text.insert(tk.END, draw_hangman(attempts))

        if attempts >= 7:
            hangman_text.delete('1.0', tk.END)
            hangman_text.insert(tk.END, f"Game over!\nThe word was: {word}")


window = tk.Tk()
attempts = 0

# Text area for hangman drawing
hangman_text = tk.Text(window, width=30, height=10)
hangman_text.insert(tk.END, draw_hangman(attempts))
hangman_text.pack()

# Label for word to guess
word = random.choice(WORD_LIST)
word_label = tk.Label(window, text="_" * len(word))
word_label.pack()

# Entry for letter input
letter_entry = tk.Entry(window)
letter_entry.pack()

# Button for guessing
guess_button = tk.Button(window, text="Guess",
                         command=lambda: guess(letter_entry.get()))
guess_button.pack()

window.mainloop()

"""Search window.

Search for samples.
Showcases Iterator OOP design pattern.
"""
from tkinter import Toplevel, Entry, Listbox, Label
import behavioral.iterator as iterator


class Extra(Toplevel):
    """Implement Search window."""

    def __init__(self):
        """Initialize window."""
        super().__init__()
        self.title("Search")
        Label(self, text="Facade design pattern").pack()
        Label(self, text="Unified interface to a set of interfaces").pack()
        self.samples = iterator.Samples(['hat', 'kick', '808'])

        self.entry = Entry(self)
        self.entry.pack()
        self.entry.bind('<KeyRelease>', self.parse)

        self.listbox = Listbox(self)
        self.listbox.pack()

        for index, item in enumerate(self.samples):
            self.listbox.itemcget
            self.listbox.insert(index, item)

    def parse(self, e):
        """Parse key presses."""
        # self.listbox.delete(0, 'end')

        char = e.widget.get()
        data = []

        if not char.strip():
            data = list(self.samples)
        else:
            for item in self.samples:
                if char in item:
                    data.append(item)

        self.listbox.delete(0, 'end')
        for item in data:
            self.listbox.insert(0, item)

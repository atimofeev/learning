"""Footer window to place plugins.

Simplified version designed to simulate drag-and-drop behavior.
Showcases Factory Method OOP design pattern.
"""
from tkinter import Toplevel, Button, Entry, StringVar, Label
import creational.factorymethod as fm


class Extra(Toplevel):
    """Implement Footer window."""

    def __init__(self):
        """Initialize window."""
        super().__init__()
        self.title("Footer")
        Label(self, text="Factory Method").pack()
        Label(self, text="Create variants of one object").pack()
        Label(self, text="Available plugins: Effect, Synth").pack()
        self.entry = Entry(self, width=15, textvariable=StringVar())
        self.entry.pack()
        Button(self, text='Drag plugin here', command=self.show_plugins).pack()
        self.output_label = Label(self)
        self.output_label.pack()

    def show_plugins(self):
        """Simulate plugin drag-and-drop into footer."""
        drop = self.entry.get()
        effect = fm.Creator().Factory(drop)

        if effect:
            self.output_label.config(text='You dropped {}'.format(effect.type))

"""Render window.

Render tracks into files.
Showcases Facade OOP design pattern.
"""
from tkinter import Toplevel, Button, Label
from tkinter.messagebox import askquestion
import structural.facade as facade


class Extra(Toplevel):
    """Implement Render window."""

    def __init__(self):
        """Initialize window."""
        super().__init__()
        self.title("Render")
        Label(self, text="Facade design pattern").pack()
        Label(self, text="Unified interface to a set of interfaces").pack()
        Button(self, text='Start render', command=self.start_rendering).pack()
        self.out_label = Label(self)
        self.out_label.pack()

    def start_rendering(self):
        """Render tracks to files."""
        response = askquestion("...", message="Start rendering?")
        if response == "yes":
            self.out_label.config(text=facade.Render().startRendering())

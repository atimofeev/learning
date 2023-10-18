"""EQ window.

Lists available EQs.
Showcases Abstract Factory OOP design pattern.
"""
from tkinter import Toplevel, Button, Label
import creational.abstractfactory as af


class Extra(Toplevel):
    """Implement EQs window."""

    def __init__(self):
        """Initialize window."""
        super().__init__()
        self.title("EQs")
        Label(self, text="Abstract Factory").pack()
        Label(self, text="Create family of diferent object types").pack()
        Button(self, text='Show EQs', command=self.show_EQs).pack()

    def show_EQs(self):
        """Show EQs list."""
        # Remove "Show EQs" button
        for widget in self.winfo_children():
            if isinstance(widget, Button):
                widget.destroy()

        # Draw individual EQ buttons (non-functional)
        for eq in af.EQsFactory().eqs:
            Button(self, text=f'{eq.name}').pack()

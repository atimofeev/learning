"""Group window.

Apply settings to group of tracks.
Showcases Observer OOP design pattern.
"""
from tkinter import Toplevel, Label, Scale, StringVar
import behavioral.observer as obs


class Extra(Toplevel):
    """Implement Group window."""

    def __init__(self):
        """Initialize window."""
        super().__init__()
        self.title("Group")
        Label(self, text="Observer design pattern").pack()
        Label(self, text="One object checks for update in other object").pack()
        self.compressor = obs.Compressor("Compressor")
        self.label_var = StringVar()
        self.label_var.set('Initial gain')
        self.kick = obs.Kick(self.label_var)
        Label(self, text='Change Gain of the %s' % self.kick.name).pack()
        Scale(self, command=lambda value: self.change_gain(int(value)),
              from_=0, to=100).pack()
        Label(self, textvariable=self.label_var).pack()

    def change_gain(self, gain=0):
        """Gain changing slider.

        Subscribe self.kick for self.compressor updates.
        """
        self.compressor.attach(self.kick)
        self.compressor.setGain = gain

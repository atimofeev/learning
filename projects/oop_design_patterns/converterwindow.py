"""Converter window.

Convert Audio to MIDI.
Implements Adapter OOP design pattern.
"""
from tkinter import Toplevel, Button, Label
import structural.adapter as adapter


class Extra(Toplevel):
    """Implement Converter window."""

    def __init__(self):
        """Initialize window."""
        super().__init__()
        self.title("Converter")
        Label(self, text="Adapter design pattern").pack()
        Label(self, text="Make incompatible interfaces work together").pack()
        Button(self, text='Audio Record', command=self.audio).pack()
        Button(self, text='Midi', command=self.midi).pack()
        self.out_label = Label(self)
        self.out_label.pack()

    def audio(self):
        """Play Audio."""
        self.out_label.config(text=adapter.AudioTrack().audioRecord())

    def midi(self):
        """Convert Audio to Midi and play."""
        self.out_label.config(text=adapter.AudioToMidiAdapter().audioRecord())

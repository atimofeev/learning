"""PlaySynth window.

Plays sounds of different synths.
Showcases Strategy OOP design pattern.
"""
from tkinter import Toplevel, Label, Button
import behavioral.strategy as strat
from functools import partial


class Extra(Toplevel):
    """Implement PlaySynth window."""

    def __init__(self):
        """Initialize window."""
        super().__init__()
        self.title("PlaySynth")
        Label(self, text="Strategy design pattern").pack()
        Label(self, text="Separate behavior from object").pack()
        self.cleanSound = strat.CleanSound()
        self.keyScape = strat.KeyScape(self.cleanSound)
        self.vintageSound = strat.VintageSound()
        self.mellotron = strat.Mellotron(self.vintageSound)
        Label(self, text='KeyScape').pack()
        Button(self, text='Play Clean Sound',
               command=self.play_keyscape).pack()
        Label(self, text='Mellotron').pack()
        Button(self, text='Play Vintage Sound',
               command=self.play_mellotron).pack()
        Button(self, text='Play Clean Sound', command=partial(
                self.play_mellotron_clean,
                self.mellotron,
                self.cleanSound)).pack()
        self.out_label = Label(self)
        self.out_label.pack()

    def play_keyscape(self):
        """Play Keyscape sound (clean)."""
        self.out_label.config(text=self.keyScape.playSound())

    def play_mellotron(self):
        """Play Mellotron sound (vintage)."""
        self.out_label.config(text=self.mellotron.playSound())

    def play_mellotron_clean(self, mellotron, cleanSound):
        """Play Mellotron with Keyscape clean sound."""
        original_sound = mellotron.soundSystem
        mellotron.soundSystem = cleanSound
        self.out_label.config(text=mellotron.playSound())
        mellotron.soundSystem = original_sound

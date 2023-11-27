"""Effects window.

Places effects on top of dry sound.
Showcases Decorator OOP design pattern.
"""
from tkinter import Toplevel, Label, Checkbutton, IntVar
import structural.decorator as decorator


class Extra(Toplevel):
    """Implement Effects window."""

    def __init__(self):
        """Initialize window."""
        super().__init__()
        self.title("Effects")
        Label(self, text="Decorator design pattern").pack()
        lbl = "Add new functionality to object without altering its structure"
        Label(self, text=lbl).pack()
        self.dry = decorator.SoundEntity("sound")
        label = Label(self, bg='white', width=30, text=self.dry.play())
        label.pack()

        comp = IntVar(value=0)
        eq = IntVar(value=0)

        def result():
            """Place effect on sound."""
            if (comp.get()) and (not eq.get()):
                wet = decorator.Compressor(self.dry)
                label.config(text=wet.play())
            elif (not comp.get()) and (eq.get()):
                wet = decorator.EQ(self.dry)
                label.config(text=wet.play())
            elif (comp.get()) and (eq.get()):
                wet = decorator.EQ(decorator.Compressor(self.dry))
                label.config(text=wet.play())
            else:
                label.config(text=self.dry.play())

        Checkbutton(self, text='Compressor', variable=comp,
                    command=result).pack()
        Checkbutton(self, text='EQ', variable=eq, command=result).pack()

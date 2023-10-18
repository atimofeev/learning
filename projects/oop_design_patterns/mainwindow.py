"""Implementation of a Window class that inherits from Tk and Singleton.

The Window class is designed to create a Tkinter GUI window while ensuring that
only one instance of the window exists at any given time, following the
Singleton design pattern.
"""

from tkinter import Tk, Button, Label
from creational.singleton import Singleton
import eqswindow
import footerwindow
import converterwindow
import effectswindow
import renderwindow
import searchwindow
import trackeffectswindow
import playsynthwindow


class Window(Tk, Singleton):
    """A Tkinter GUI window following the Singleton design pattern.

    This class extends the Tk class from the tkinter library and also
    implements the Singleton design pattern. It ensures that only one window
    will exist at any given time.

    Methods:
        init: Initialize the singleton instance of the Window class.
    """

    def init(self):
        """Initialize the singleton instance of the Window class.

        This method is called when the singleton instance is created for the
        first time. It initializes the Tkinter window by calling the superclass
        constructor.
        """
        print('calling from init')
        super().__init__()

        Label(self,
              text="This window implements Singleton design pattern.").pack()
        Label(self, text="It can be launched only in one instance.").pack()

        # Dictionary mapping button texts and corresponding window types
        self.windows_dict = {
            'EQs': eqswindow.Extra,
            'Footer': footerwindow.Extra,
            'Converter': converterwindow.Extra,
            'Effects': effectswindow.Extra,
            'Renderer': renderwindow.Extra,
            'Search': searchwindow.Extra,
            'Track Effects': trackeffectswindow.Extra,
            'Play Synth': playsynthwindow.Extra,
        }

        for btn_text, window_type in self.windows_dict.items():
            Button(self, text=btn_text,
                   command=lambda win_type=window_type:
                   self.create_window(win_type)).pack()

    def create_window(self, window_class):
        """Create extra windows."""
        global extraWindow
        extraWindow = window_class()

    def __init__(self):
        """Initialize the Window class object.

        Note: This method will be called every time the class is instantiated,
        but due to the Singleton pattern, only 1 instance will actually exist.
        """
        print('calling from __init__')

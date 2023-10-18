#!/usr/bin/env python3
"""Learn OOP design patterns on a oversimplified DAW-like project.

Each pattern is well documented in it's implementation's docstrings.
"""

from mainwindow import Window

if __name__ == "__main__":

    handle = Window()
    handle.title('Daw')
    handle.mainloop()

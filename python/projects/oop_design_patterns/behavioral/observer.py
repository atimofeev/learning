"""Observer design pattern.

This module provides a basic implementation of the observer design pattern. In
this module, a Compressor object, which extends the Observable class, produces
some data (gain). And a Kick object, which serves as an observer, reacts
whenever data is altered in the Compressor (observable).

Classes:
    Observable: Class representing the subject in the observer design pattern.
    Compressor: Class representing a concrete implementation of an observable
subject.
    Kick: Class representing the observer in the observer design pattern.
"""


class Observable:
    """Base class representing a 'subject' in the observer design pattern."""

    def __init__(self):
        """Initialize an Observable instance with empty list of observers."""
        self.observers = []

    def notify(self):
        """Notify all attached observers, triggering their update methods."""
        for observer in self.observers:
            observer.update(self)

    def attach(self, observer):
        """Attach an observer to the observable.

        Args:
            observer: Observer instance to be attached.
        """
        if observer not in self.observers:
            self.observers.append(observer)


class Compressor(Observable):
    """An observable 'subject' in the context of audio processing module."""

    def __init__(self, name):
        """Initialize the Compressor instance with a name and default gain."""
        super().__init__()
        self.name = name
        self._gain = 0

    @property
    def gain(self):
        """Get the gain of the Compressor."""
        return self._gain

    @gain.setter
    def setGain(self, value):
        """Set the gain of the Compressor and notify observers of the change.

        Args:
            value: New gain value to be set.
        """
        self._gain = value
        self.notify()


class Kick:
    """Observer in observer design pattern; listens for Compressor events."""

    def __init__(self, label_var):
        """Initialize the Kick instance with a default name and label_var."""
        self._name = "Kick"
        self.label_var = label_var  # StringVar for Tkinter label

    def update(self, subject):
        """Update label_var instead of printing to console."""
        self.label_var.set(
            f'Kick: Subject {subject.name} has data: gain {subject.setGain}')

    @property
    def name(self):
        """Return name, which is 'Kick' by default."""
        return self._name

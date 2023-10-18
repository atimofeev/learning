"""This module contains classes implementing the Strategy design pattern.

This design pattern is applicable when there's a need to manage
algorithms, relationships, and responsibilities between objects
efficiently. The module allows a client to choose an algorithm from
a family of algorithms at runtime, and independently of the clients
that use it. Here it applies to different sound systems played by
different synthesizers.

Classes:
- Sound
- CleanSound
- VintageSound
- Synth
- KeyScape
- Mellotron
"""
from abc import ABCMeta, abstractmethod


class Sound(metaclass=ABCMeta):
    """Represent a sound system behavior."""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by each sound type."""
        pass


class CleanSound(Sound):
    """Clean sound system."""

    def sound(self):
        """Print clean sound."""
        return "Clean sound"


class VintageSound(Sound):
    """Vintage sound system."""

    def sound(self):
        """Print vintage sound."""
        return "Vintage sound"


class Synth(metaclass=ABCMeta):
    """Abstract class for synthesizers, using a sound system."""

    def __init__(self, soundSystem):
        """Initialize synth with a sound system."""
        self._soundSystem = soundSystem

    def playSound(self):
        """Plays the sound of the sound system."""
        return self._soundSystem.sound()

    @property
    def soundSystem(self):
        """Getter for sound system."""
        return self._soundSystem

    @soundSystem.setter
    def soundSystem(self, soundSystem):
        """Setter for the audio system."""
        self._soundSystem = soundSystem


class KeyScape(Synth):
    """KeyScape synth, defaults to a clean sound."""

    def __init__(self, cleanSound):
        """Initialize KeyScape with a clean sound system."""
        self.cleanSound = cleanSound
        super().__init__(cleanSound)


class Mellotron(Synth):
    """Mellotron synth, defaults to a vintage sound."""

    def __init__(self, vintageSound):
        """Initialize Mellotron with a vintage sound system."""
        self.vintageSound = vintageSound
        super().__init__(vintageSound)

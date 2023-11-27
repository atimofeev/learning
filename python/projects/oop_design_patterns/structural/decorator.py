"""Decorator design pattern for enhancing audio functionality.

The Decorator pattern allows us to add new functionality to an object without
altering its structure. This is achieved by wrapping the original object and
providing additional features.

In this example, the `SoundEntity` class serves as the base component providing
basic sound functionality. Decorator classes `EQ` and `Compressor` enhance the
functionality by adding EQ and Compression, respectively.

Classes:
- SoundEntity: Represents the basic sound entity that can play sound.
- EQ: Decorator that adds EQ (Equalization) to the sound.
- Compressor: Decorator that adds compression to the sound.

Methods:
- SoundEntity.play: Play the sound.
- EQ.play: Play the sound with EQ applied.
- Compressor.play: Play the sound with compression applied.
"""


class SoundEntity:
    """Base class representing a sound."""

    def __init__(self, sound):
        """Initialize the sound entity with the given sound."""
        self.sound = sound

    def play(self):
        """Play sound."""
        return self.sound


class EQ(SoundEntity):
    """Decorator class to add EQ to a sound."""

    def __init__(self, eqed):
        """Initialize with an Entity object to which EQ will be applied."""
        self.eqed = eqed

    def play(self):
        """Play the sound after applying EQ."""
        return "EQ[{}]".format(self.eqed.play())


class Compressor(SoundEntity):
    """Decorator class to add compression to a sound."""

    def __init__(self, compressed):
        """Initialize with an Entity object to which comp will be applied."""
        self.compressed = compressed

    def play(self):
        """Play the sound after applying compression."""
        return "Compressor[{}]".format(self.compressed.play())

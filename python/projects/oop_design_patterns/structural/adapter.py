"""Adapter design pattern, which allows incompatible interfaces work together.

The Adapter pattern is useful for allowing systems with incompatible interfaces
to work together. It serves as a wrapper around an existing class and provides
a standard interface expected by the system.

In this example, we have two abstract base classes `Audio` and `Midi` which
represent different kinds of audio interfaces. Concrete implementations of
these classes are `AudioTrack` and `MidiTrack`.

The `AudioToMidiAdapter` class serves as an adapter to make a `Midi` object
conform to an `Audio` interface.

Classes:
- Audio (ABC): An abstract base class representing an audio interface.
- Midi (ABC): An abstract base class representing a MIDI interface.
- AudioTrack: A concrete class implementing the Audio interface.
- MidiTrack: A concrete class implementing the Midi interface.
- AudioToMidiAdapter: An adapter class allowing a Midi object to be used where
an Audio object is expected.

Methods:
- Audio.audioRecord: Abstract method that should be implemented by all
subclasses to record audio.
- Midi.midiTrack: Abstract method that should be implemented by all subclasses
to play MIDI tracks.
"""
from abc import ABC, abstractmethod


class Audio(ABC):
    """Abstract base class (ABC) for audio interfaces."""

    @abstractmethod
    def audioRecord():
        """Record audio. Should be implemented by concrete subclasses."""
        pass


class Midi(ABC):
    """Abstract base class for MIDI interfaces."""

    @abstractmethod
    def midiTrack():
        """Play MIDI track. Should be implemented by concrete subclasses."""
        pass


class AudioTrack(Audio):
    """Concrete class for audio recording."""

    def audioRecord(self):
        """Implement audio recording functionality."""
        return "Audio is playing..."


class MidiTrack(Midi):
    """Concrete class for playing MIDI tracks."""

    def midiTrack(self):
        """Implement MIDI playing functionality."""
        return "Midi is playing..."


class AudioToMidiAdapter(Audio):
    """Adapter class to make Midi objects conform to Audio interface."""

    def __init__(self):
        """Initialize adapter with a MidiTrack object."""
        self.midi = MidiTrack()

    def audioRecord(self):
        """Adapt midiTrack method to conform to audioRecord interface."""
        return self.midi.midiTrack()

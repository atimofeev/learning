"""Facade design pattern: simplify access to a complex subsystem.

The Facade pattern provides a unified interface to a set of interfaces in a
subsystem, making the subsystem easier to use. In this example, the `Render`
class serves as the facade that unifies the interface for rendering MP3, WAV,
and Data.

Classes:
- MP3: Represents the MP3 rendering subsystem.
- WAV: Represents the WAV rendering subsystem.
- Data: Represents the Data rendering subsystem.
- Render: The facade class that aggregates all rendering types into a unified
interface.

Methods:
- MP3.process: Perform MP3 rendering.
- WAV.process: Perform WAV rendering.
- Data.process: Perform Data rendering.
- Render.startRendering: Perform rendering tasks for all available formats.
"""


class MP3:
    """Class responsible for handling MP3 file rendering."""

    def process(self):
        """Perform the task of rendering an MP3 file."""
        return "Processing MP3..."


class WAV:
    """Class responsible for handling WAV file rendering."""

    def process(self):
        """Perform the task of rendering a WAV file."""
        return "Processing WAV..."


class Data:
    """Class responsible for handling data rendering."""

    def process(self):
        """Perform the task of rendering data, such as analysis."""
        return "Processing analysis..."


class Render:
    """Facade class.

    Provides a simplified interface to multiple rendering types.
    """

    def __init__(self):
        """Initialize the facade.

        Create instances of MP3, WAV, and Data rendering classes.
        """
        self.mp3 = MP3()
        self.wav = WAV()
        self.data = Data()

    def startRendering(self):
        """Start rendering tasks for all encapsulated rendering classes.

        Outputs messages for each.
        """
        process_messages = []
        process_messages.append(self.mp3.process())
        process_messages.append(self.wav.process())
        process_messages.append(self.data.process())
        return "\n".join(process_messages)

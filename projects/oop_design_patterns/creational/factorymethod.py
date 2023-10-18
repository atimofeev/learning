"""Basic implementation of the Factory Method using abstract classes.

The Factory Method pattern provides an interface for creating instances of a
class, with its subclass deciding which class to instantiate. In this example,
we have an abstract base class `Plugin` that defines a common interface for
different types of plugins (`EffectPlugin`, `SynthPlugin`).

The `Creator` class contains the Factory Method (`Factory`) which takes a
`type` parameter and returns an instance of the corresponding subclass of
`Plugin`.

Classes:
- Plugin (ABC): An abstract base class that represents a generic plugin
interface.
- EffectPlugin: A concrete implementation of the Plugin abstract base class for
effect plugins.
- SynthPlugin: A concrete implementation of the Plugin abstract base class for
synth plugins.
- Creator: Contains the Factory Method for creating instances of Plugin
subclasses based on a type parameter.

Methods:
- Plugin.type: Abstract method that should be implemented by all subclasses to
return the type of the plugin.
- Creator.Factory(type): Static method that serves as a Factory Method for
creating Plugin instances.
"""

from abc import ABCMeta, abstractmethod


class Plugin(metaclass=ABCMeta):
    """Abstract base class for different types of plugins."""

    @abstractmethod
    def type():
        """Abstract method to return the type of the plugin.

        Raises:
            NotImplementedError: This method must be overridden by subclasses.
        """
        raise NotImplementedError


class EffectPlugin(Plugin):
    """Concrete class for Effect type plugins."""

    def __init__(self):
        """Initialize the EffectPlugin with its type set to 'Effect'."""
        self.type = "Effect"

    def type(self):
        """Return the type of this plugin.

        Returns:
            str: The type of the plugin ('Effect').
        """
        return self.type


class SynthPlugin(Plugin):
    """Concrete class for Synth type plugins."""

    def __init__(self):
        """Initialize the SynthPlugin with its type set to 'Synth'."""
        self.type = "Synth"

    def type(self):
        """Return the type of this plugin.

        Returns:
            str: The type of the plugin ('Synth').
        """
        return self.type


class Creator:
    """Contains the Factory Method for creating Plugin instances."""

    @staticmethod
    def Factory(type):
        """Create Plugin instances based on their type using Factory Method.

        Args:
            type (str): The type of plugin ('Effect' or 'Synth').

        Returns:
            Plugin: An instance of the appropriate Plugin subclass.
            None: If the type is not recognized.
        """
        if type == 'Effect':
            return EffectPlugin()
        elif type == 'Synth':
            return SynthPlugin()
        return None

"""Simplified version of the Abstract Factory design pattern.

The Abstract Factory design pattern is aimed at providing an interface for
creating families of related or dependent objects. In this example, we have a
single factory (`EQsFactory`) that produces objects (`EQs`) of multiple types
(`FabFilter`, `Waves`, and `UAD`). Each of these types is a subclass of a
common superclass (`EQ`), which ensures that they share a common interface.

The `EQsFactory` class aggregates various types of `EQ` objects upon its
initialization.
- `eqs`: a property method that returns the list of EQ objects aggregated in
the factory.

The `EQ` class serves as the base class for various types of EQ products.
- `__init__(self, bands, name)`: Initializes a new EQ object with a given
number of bands and a name.
- `getBands(self)`: Returns the number of bands in the EQ.

Subclasses `FabFilter`, `Waves`, and `UAD` extend the `EQ` base class.
- `__init__(self, bands, name)`: Calls the base class constructor to initialize
the EQ object.
- `getBands(self)`: Calls the base class method to return the number of bands
in the EQ.

Note:
While this example demonstrates the concept of creating multiple types of
related objects (`EQs`),
it does not fully encapsulate the idea of an Abstract Factory, which typically
deals with multiple families of products.
"""


class EQsFactory:
    """Factory class for creating multiple EQ objects."""

    def __init__(self):
        """Initialize the factory with predefined EQ objects."""
        self._eqsfactory = [FabFilter(5, "Pro Q"), UAD(4, "UAD"),
                            Waves(3, "Waves")]

    @property
    def eqs(self):
        """Return the list of EQ objects."""
        return self._eqsfactory


class EQ:
    """Base class for EQs (Equalizers)."""

    def __init__(self, bands, name):
        """Initialize EQ with number of bands and name."""
        self.bands = bands
        self.name = name

    def getBands(self):
        """Return the number of bands in the EQ."""
        return self.bands


class FabFilter(EQ):
    """Class for FabFilter EQs."""

    def __init__(self, bands, name):
        """Initialize EQ with number of bands and name."""
        super().__init__(bands, name)

    def getBands(self):
        """Return the number of bands in the EQ."""
        return super().getBands()


class Waves(EQ):
    """Class for Waves EQs."""

    def __init__(self, bands, name):
        """Initialize EQ with number of bands and name."""
        super().__init__(bands, name)

    def getBands(self):
        """Return the number of bands in the EQ."""
        return super().getBands()


class UAD(EQ):
    """Class for UAD EQs."""

    def __init__(self, bands, name):
        """Initialize EQ with number of bands and name."""
        super().__init__(bands, name)

    def getBands(self):
        """Return the number of bands in the EQ."""
        return super().getBands()

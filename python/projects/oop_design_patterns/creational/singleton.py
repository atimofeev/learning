"""Singleton class implementation of the Singleton design pattern.

The Singleton design pattern restricts a class from instantiating multiple
objects. It ensures that a class has only one instance and provides a way to
access that instance from within the codebase.
"""


class Singleton(object):
    """Implements the Singleton design pattern.

    This class is designed to serve as a base class for other classes that need
    to implement the Singleton design pattern. By inheriting from this class,
    a derived class ensures that only one instance of itself will exist.

    Attributes:
        __it__ : Class-level attribute that stores the single instance.

    Methods:
        __new__(cls, *args, **kwds): Custom implementation for instance
    creation.
        init(self, *args, **kwds): Initialization method for the singleton
    instance. Meant to be overridden.
    """

    def __new__(cls, *args, **kwds):
        """Create or return the singleton instance of the class.

        Checks for an existing instance of the class in the class-level
        attribute '__it__'. If it exists, the existing instance is returned.
        Otherwise, a new instance is created, initialized via the 'init'
        method, and returned.

        Args:
            *args: Variable-length argument list.
            **kwds: Arbitrary keyword arguments.

        Returns:
            The singleton instance of the class.
        """
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it
        cls.__it__ = it = object.__new__(cls)
        it.init(*args, **kwds)
        return it

    def init(self, *args, **kwds):
        """Initialize the singleton instance.

        Meant to be overridden in derived classes.
        This method is called when the singleton instance is created for the
        first time. It can be overridden to add any additional initialization
        logic.

        Args:
            *args: Variable-length argument list.
            **kwds: Arbitrary keyword arguments.
        """
        pass

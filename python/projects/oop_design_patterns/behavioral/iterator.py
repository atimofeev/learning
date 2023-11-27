
"""Iterator design pattern for traversing a collection of samples.

The Iterator pattern provides a way to access elements of a collection object
sequentially without exposing its underlying representation. In this example,
the `Samples` class serves as a collection of data samples that can be iterated
over.

Classes:
- Samples: Represents a collection of data samples.

Methods:
- Samples.__iter__: Returns the iterator object itself, initializing the index.
- Samples.__next__: Returns the next value from the data collection. Raises
StopIteration when finished.
"""


class Samples:
    """Collection class for samples."""

    def __init__(self, data):
        """Initialize Samples."""
        self.data = data

    def __iter__(self):
        """Iterate Samples."""
        self.index = 0
        return self

    def __next__(self):
        """Next item of Samples."""
        if self.index < (len(self.data)):
            result = self.data[self.index]
            self.index += 1
        else:
            raise StopIteration
        return result

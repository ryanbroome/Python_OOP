"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    # initialize the SerialGenerator to start out as 100 and the 
    def __init__(self, start=100):
        self.start = start
        self.count = 0
    # if first generate call return 100, otherwise return start += 1
    @classmethod
    def __repr__(self):
        """
        
        """
    def generate(self):
        if self.count == 0:
            self.count = self.count + 1
            return self.start
        elif self.count >= 1:
            self.count = self.count + 1
            self.start = self.start + 1
            return self.start
    # when called will reset the starting value t0 100
    def reset(self):
        self.start = 100
        self.count = 0
        return
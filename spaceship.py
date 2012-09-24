"""
The vast universe, in code.

'Fascinating'  - Spock

"""
import time
import math


class Space(list):
    """
    The vast emptiness of space.

    Anything that might contain a Thing with a coordinate might go here.
    It could be an empty void of space, it could be in local space around
    the Earth or it could be the space surrounding a star, black hole or other
    such bodies. The planets and stars would also require Things to represent
    them in their own surrounding space.
    """
    def __init__(self, name=""):
        """
        Create empty space.

        Giving a name to a vast stretch of nothingness seems to make it
        something.
        """
        super(Space, self).__init__()
        self.name = name
        self.ticks = 0

    def __str__(self):
        """
        Output some information.

        For being nothing, there certainly seems to be a lot of things to say
        about it.
        """
        output = "Space: \'{}\'".format(self.name)
        if self:
            output += " contains:\n"
            for thing in self:
                output += "{!s}\n".format(thing)
        return output

    def doTick(self, tick=0):
        """Increment tick count and execute doTick on all children."""
        self.ticks += 1
        for child in self:
            child.doTick(tick)


class Coordinate:
    """Represents a coordinate in 2d space"""
    def __init__(self, x=None, y=None):
        """Nothing too fancy, just x and y"""
        self.x = x
        self.y = y

    def __str__(self):
        """Output in standard (x,y) format"""
        return "({}, {})".format(self.x, self.y)

    def __nonzero__(self):
        """Nonzero if both points are defined."""
        if self.x is not None and self.y is not None:
            return 1
        return 0

    def __add__(self, other):
        """Add two valid coordinates."""
        if not self or not other:
            raise TypeError("Something ain't right...")
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Subtract two valid coordinates."""
        if not self or not other:
            raise TypeError("He's dead, Jim.")
        return Coordinate(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        """Coordinates are equal only when both points are equal."""
        if not self or not other:
            raise TypeError("Danger Will Robinson!")
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """Inverse __eq__"""
        return not self.__eq__(other)

    def __radd__(self, other):
        """Adds two valid coordinates."""
        return other.__add__(self)

    def __rsub__(self, other):
        """Subtracts two valid coordinates."""
        return other.__add__(self)


class Thing:
    """The things that fill the void"""
    def __init__(self, name="", x=None, y=None, location=None):
        """
            Create the thing from nothing, give it a name and put give it
            an imaginary place in imaginary space.
        """
        if x and not location and isinstance(x, Coordinate):
            location = x
            x = None
        if x and y and not location:
            location = Coordinate(x=x, y=y)
        self.location = location
        self.name = name
        self.angle = 0
        self.speed = 0
        self.ticks = 0

    def __str__(self):
        """Output what I am, who I am and where I am."""
        return "Thing: \'{}\' at {!s}".format(self.name, self.location)

    def __nonzero__(self):
        return self.location and isinstance(self.location, Coordinate)

    def doTick(self, tick=0):
        """Increment tick count."""
        self.ticks += 1
        if self.speed > 0:
            self.doMove()

    def doMove(self):
        """Move the thing"""
        #if not isinstance(self.location, Coordinate):
        #    self.location = Coordinate(0, 0)
        scale_x = math.cos(math.radians(self.angle))
        scale_y = math.sin(math.radians(self.angle))
        newLocation = Coordinate(int(self.speed * scale_x), int(self.speed * scale_y))
        self.location += newLocation


class Time(list):
    """Represent time as ticks separated by a delay."""
    def __init__(self, delay=0):
        """Set delay and tick count."""
        super(Time, self).__init__()
        self.delay = delay
        self.tick = 0

    def doTick(self):
        """Increment tick and execute doTick on all children."""
        self.tick += 1
        for child in self:
            child.doTick(self.tick)

    def run(self, limit=100):
        """Elapse time up to limit."""
        for x in range(1, limit + 1):
            if x != 1 and self.delay > 0:
                time.sleep(self.delay)
            self.doTick()

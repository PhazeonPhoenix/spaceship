"""
The vast universe, in code.

'Fascinating'  - Spock

this was not the repo i was looking for

"""

import time
import math


class Space(list):
    """
    The vast emptiness of space.

    Anything that might contain a Thing with a Vector might go here.
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


class Vector:
    """
    Represents a Vector in 2d space

    Based on the vector class defined at
    http://code.activestate.com/recipes/502252-physics/

    What is a vector?

    In physics, vectors describe the direction and the magnitude (or speed) of
    an amount of force. These can be described in many different ways using
    many different units of measurement. For example, a vector describes the
    direction and speed of a car driving west at 25 mph.

    Vectors are typically illustrated on a graph with a starting point (or
    origin) and the direction and magnitude of the vector as an arrow pointing
    in the correct direction and the length of the arrow indicating it's
    magnitude.

    In this implementation, vectors are given the relative origin of 0, 0 and an
    imaginary arrow drawn from the origin to the point defined in the vector
    describes it's direction and magnitude. This means that this Vector class
    can also double as a coordinate class, since a coordinate is also the
    location of a point relative to a shared or global origin.

    The alternative to a vector is a scalar. A scalar is a value that has
    magnitude but not direction. Temperature, mass and energy are examples of
    scalars in physics.
    """

    def __init__(self, x, y):
        """Initialize the Vector object."""
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        """Output in standard (x, y) format"""
        return "({:.1f}, {:.1f})".format(self.x, self.y)

    def __repr__(self):
        """Return the vector\'s representation."""
        return 'Vector({:.1f}, {:.1f})'.format(self.x, self.y)

    def __add__(self, other):
        """Return the sum of vector addition."""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Return the difference of vector subtraction."""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, number):
        """Return the product of vector multiplication."""
        return Vector(self.x * number, self.y * number)

    def __div__(self, number):
        """Return the quotient of vector division."""
        return Vector(self.x / number, self.y / number)

    def __eq__(self, other):
        """Compare Vectors for equality."""
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """Inverse __eq__"""
        return not self.__eq__(other)

    def __iadd__(self, other):
        """Execute addition in-place."""
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        """Execute subtraction in-place."""
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self, number):
        """Execute multiplication in-place."""
        self.x *= number
        self.y *= number
        return self

    def __idiv__(self, number):
        """Execute division in-place."""
        self.x /= number
        self.y /= number
        return self

    def __abs__(self):
        """Return the vector\'s magnitude."""
        return math.hypot(self.x, self.y)

    def unit(self):
        """
        Return the unit vector.

        The unit vector would be the resultant Vector if the magnitude of a
        Vector was reduced to 1.
        """
        return self / abs(self)


class Thing:
    """The things that fill the void"""
    def __init__(self, name="", x=None, y=None, location=None):
        """
            Create the thing from nothing, give it a name and put give it
            an imaginary place in imaginary space.
        """
        if x and not location and isinstance(x, Vector):
            location = x
            x = None
        if x and y and not location:
            location = Vector(x=x, y=y)
        self.location = location
        self.name = name
        self.angle = 0
        self.speed = 0
        self.ticks = 0

    def __str__(self):
        """Output what I am, who I am and where I am."""
        return "Thing: \'{}\' at {!s}".format(self.name, self.location)

    def __nonzero__(self):
        return self.location and isinstance(self.location, Vector)

    def doTick(self, tick=0):
        """Increment tick count."""
        self.ticks += 1
        if self.speed > 0:
            self.doMove()

    def doMove(self):
        """Move the thing"""
        #if not isinstance(self.location, Vector):
        #    self.location = Vector(0, 0)
        scale_x = math.cos(math.radians(self.angle))
        scale_y = math.sin(math.radians(self.angle))
        newLocation = Vector(int(self.speed * scale_x), int(self.speed * scale_y))
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

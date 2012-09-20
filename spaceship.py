"""
The vast universe, in code.

'Fascinating'  - Spock

"""


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
        if self.x != None and self.y != None:
            return 1
        return 0

    def __add__(self, other):
        if not self or not other:
            raise TypeError("Something ain't right...")
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not self or not other:
            raise TypeError("He's dead, Jim.")
        return Coordinate(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if not self or not other:
            raise TypeError("Danger Will Robinson!")
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        if not self or not other:
            raise TypeError("I've got a bad feeling about this...")
        return not self.__eq__(other)

    def __radd__(self, other):
        return other.__add__(self)

    def __rsub__(self, other):
        return other.__add__(self)


class Thing:
    """The things that fill the void"""
    def __init__(self, name="", location=None, x=None, y=None):
        """
            Create the thing from nothing, give it a name and put give it
            an imaginary place in imaginary space.
        """
        if x and y and not location:
            location = Coordinate(x=x, y=y)
        self.location = location
        self.name = name

    def __str__(self):
        """Output what I am, who I am and where I am."""
        return "Thing: \'{}\' at {!s}".format(self.name, self.location)

if __name__ == "__main__":
    milky_way = Space(name="Milky Way")
    milky_way.append(Thing(name="ship", x=5, y=10))
    point = Coordinate(x=2, y=5)
    milky_way.append(Thing(name="ship2", location=point))
    milky_way.append(Thing(name="ship3", location=point, x=9, y=3))

    print milky_way

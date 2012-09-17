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


class Thing:
    """The things that fill the void"""
    def __init__(self, name="", location=None, x=None, y=None, ):
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

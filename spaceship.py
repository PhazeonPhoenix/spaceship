class Space(list):
    """The vast emptiness of space."""
    def __init__(self, name=""):
        super(Space, self).__init__()
        self.name = name

    def __str__(self):
        output = "Space: \'{}\'".format(self.name)
        if self:
            output += " contains:\n"
            for thing in self:
                output += "{!s}\n".format(thing)
        return output


class Coordinate:
    """Represents a coordinate in 2d space"""
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __str__(self):
        return "{}, {}".format(self.x, self.y)


class Thing:
    """The things that fill the void"""
    def __init__(self, name="", location=None, x=None, y=None, ):
        if x and y and not location:
            location = Coordinate(x=x, y=y)
        self.location = location
        self.name = name

    def __str__(self):
        return "Thing: \'{}\' at {!s}".format(self.name, self.location)

if __name__ == "__main__":
    milky_way = Space(name="Milky Way")
    milky_way.append(Thing(name="ship", x=5, y=10))
    point = Coordinate(x=2, y=5)
    milky_way.append(Thing(name="ship2", location=point))
    milky_way.append(Thing(name="ship3", location=point, x=9, y=3))

    print milky_way

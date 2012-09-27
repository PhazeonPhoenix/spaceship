import unittest
import spaceship


class TestVector(unittest.TestCase):
    """Test Vector functions"""
    def test_instance(self):
        coord = spaceship.Vector(3, 6)
        self.assertEqual(3, coord.x)
        self.assertEqual(6, coord.y)

        coord = spaceship.Vector(y=3, x=6)
        self.assertEqual(6, coord.x)
        self.assertEqual(3, coord.y)

    def test_str(self):
        coord = spaceship.Vector(3, 4)
        self.assertEqual("(3.0, 4.0)", coord.__str__())

        coord = spaceship.Vector(-3, -4)
        self.assertEqual("(-3.0, -4.0)", coord.__str__())

        coord = spaceship.Vector(-3, 4)
        self.assertEqual("(-3.0, 4.0)", coord.__str__())

        coord = spaceship.Vector(3, -4)
        self.assertEqual("(3.0, -4.0)", coord.__str__())

    def test_repr(self):
        coord = spaceship.Vector(3, 4)
        self.assertEqual("Vector(3.0, 4.0)", coord.__repr__())

        coord = spaceship.Vector(-3, -4)
        self.assertEqual("Vector(-3.0, -4.0)", coord.__repr__())

        coord = spaceship.Vector(-3, 4)
        self.assertEqual("Vector(-3.0, 4.0)", coord.__repr__())

        coord = spaceship.Vector(3, -4)
        self.assertEqual("Vector(3.0, -4.0)", coord.__repr__())

    def test_add(self):
        coord1 = spaceship.Vector(3, 3)
        coord2 = spaceship.Vector(1, 1)
        coord3 = coord1.__add__(coord2)

        self.assertEqual(4, coord3.x)
        self.assertEqual(4, coord3.y)
        self.assertIsNot(coord1, coord3)
        self.assertIsNot(coord2, coord3)

        coord1 = spaceship.Vector(3, 3)
        coord2 = spaceship.Vector(-1, -1)
        coord3 = coord1.__add__(coord2)

        self.assertEqual(2, coord3.x)
        self.assertEqual(2, coord3.y)
        self.assertIsNot(coord1, coord3)
        self.assertIsNot(coord2, coord3)

    def test_sub(self):
        coord1 = spaceship.Vector(3, 3)
        coord2 = spaceship.Vector(1, 1)
        coord3 = coord1.__sub__(coord2)

        self.assertEqual(2, coord3.x)
        self.assertEqual(2, coord3.y)
        self.assertIsNot(coord1, coord3)
        self.assertIsNot(coord2, coord3)

        coord1 = spaceship.Vector(3, 3)
        coord2 = spaceship.Vector(-1, -1)
        coord3 = coord1.__sub__(coord2)

        self.assertEqual(4, coord3.x)
        self.assertEqual(4, coord3.y)
        self.assertIsNot(coord1, coord3)
        self.assertIsNot(coord2, coord3)

    def test_mul(self):
        coord1 = spaceship.Vector(3, 3)
        coord2 = coord1.__mul__(2)

        self.assertEqual(6, coord2.x)
        self.assertEqual(6, coord2.y)
        self.assertIsNot(coord1, coord2)

        coord1 = spaceship.Vector(6, 6)
        coord2 = coord1.__mul__(-2)

        self.assertEqual(-12, coord2.x)
        self.assertEqual(-12, coord2.y)
        self.assertIsNot(coord1, coord2)

        coord1 = spaceship.Vector(-3, -3)
        coord2 = coord1.__mul__(2)

        self.assertEqual(-6, coord2.x)
        self.assertEqual(-6, coord2.y)
        self.assertIsNot(coord1, coord2)

        coord1 = spaceship.Vector(-6, -6)
        coord2 = coord1.__mul__(-2)

        self.assertEqual(12, coord2.x)
        self.assertEqual(12, coord2.y)
        self.assertIsNot(coord1, coord2)

    def test_div(self):
        coord1 = spaceship.Vector(6, 6)
        coord2 = coord1.__div__(2)

        self.assertEqual(3, coord2.x)
        self.assertEqual(3, coord2.y)
        self.assertIsNot(coord1, coord2)

        coord1 = spaceship.Vector(-12, -12)
        coord2 = coord1.__div__(-2)

        self.assertEqual(6, coord2.x)
        self.assertEqual(6, coord2.y)
        self.assertIsNot(coord1, coord2)

        coord1 = spaceship.Vector(-6, -6)
        coord2 = coord1.__div__(2)

        self.assertEqual(-3, coord2.x)
        self.assertEqual(-3, coord2.y)
        self.assertIsNot(coord1, coord2)

        coord1 = spaceship.Vector(12, 12)
        coord2 = coord1.__div__(-2)

        self.assertEqual(-6, coord2.x)
        self.assertEqual(-6, coord2.y)
        self.assertIsNot(coord1, coord2)

    def test_eq(self):
        coord1 = spaceship.Vector(3, 4)
        coord2 = spaceship.Vector(3, 4)
        self.assertTrue(coord1.__eq__(coord2))

    def test_ne(self):
        coord1 = spaceship.Vector(3, 4)
        coord2 = spaceship.Vector(3, 4)
        self.assertFalse(coord1.__ne__(coord2))
    
    def test_iadd(self):
        coord1 = spaceship.Vector(3, 3)
        coord2 = spaceship.Vector(1, 1)
        coord3 = coord1.__iadd__(coord2)

        self.assertEqual(4, coord3.x)
        self.assertEqual(4, coord3.y)
        self.assertIs(coord1, coord3)
        self.assertIsNot(coord2, coord3)

        coord1 = spaceship.Vector(3, 3)
        coord2 = spaceship.Vector(-1, -1)
        coord3 = coord1.__iadd__(coord2)

        self.assertEqual(2, coord3.x)
        self.assertEqual(2, coord3.y)
        self.assertIs(coord1, coord3)
        self.assertIsNot(coord2, coord3)

    def test_isub(self):
        coord1 = spaceship.Vector(3, 3)
        coord2 = spaceship.Vector(1, 1)
        coord3 = coord1.__isub__(coord2)

        self.assertEqual(2, coord3.x)
        self.assertEqual(2, coord3.y)
        self.assertIs(coord1, coord3)
        self.assertIsNot(coord2, coord3)

        coord1 = spaceship.Vector(3, 3)
        coord2 = spaceship.Vector(-1, -1)
        coord3 = coord1.__isub__(coord2)

        self.assertEqual(4, coord3.x)
        self.assertEqual(4, coord3.y)
        self.assertIs(coord1, coord3)
        self.assertIsNot(coord2, coord3)

    def test_imul(self):
        coord1 = spaceship.Vector(3, 3)
        coord2 = coord1.__imul__(2)

        self.assertEqual(6, coord2.x)
        self.assertEqual(6, coord2.y)
        self.assertIs(coord1, coord2)

        coord1 = spaceship.Vector(6, 6)
        coord2 = coord1.__imul__(-2)

        self.assertEqual(-12, coord2.x)
        self.assertEqual(-12, coord2.y)
        self.assertIs(coord1, coord2)

        coord1 = spaceship.Vector(-3, -3)
        coord2 = coord1.__imul__(2)

        self.assertEqual(-6, coord2.x)
        self.assertEqual(-6, coord2.y)
        self.assertIs(coord1, coord2)

        coord1 = spaceship.Vector(-6, -6)
        coord2 = coord1.__imul__(-2)

        self.assertEqual(12, coord2.x)
        self.assertEqual(12, coord2.y)
        self.assertIs(coord1, coord2)

    def test_idiv(self):
        coord1 = spaceship.Vector(6, 6)
        coord2 = coord1.__idiv__(2)

        self.assertEqual(3, coord2.x)
        self.assertEqual(3, coord2.y)
        self.assertIs(coord1, coord2)

        coord1 = spaceship.Vector(-12, -12)
        coord2 = coord1.__idiv__(-2)

        self.assertEqual(6, coord2.x)
        self.assertEqual(6, coord2.y)
        self.assertIs(coord1, coord2)

        coord1 = spaceship.Vector(-6, -6)
        coord2 = coord1.__idiv__(2)

        self.assertEqual(-3, coord2.x)
        self.assertEqual(-3, coord2.y)
        self.assertIs(coord1, coord2)

        coord1 = spaceship.Vector(12, 12)
        coord2 = coord1.__idiv__(-2)

        self.assertEqual(-6, coord2.x)
        self.assertEqual(-6, coord2.y)
        self.assertIs(coord1, coord2)

    def test_abs(self):
        v = spaceship.Vector(3, 4)
        self.assertEqual(5, v.__abs__())

        v = spaceship.Vector(-3, 4)
        self.assertEqual(5, v.__abs__())

        v = spaceship.Vector(3, -4)
        self.assertEqual(5, v.__abs__())

        v = spaceship.Vector(-3, -4)
        self.assertEqual(5, v.__abs__())

    def test_unit(self):
        v = spaceship.Vector(3, 4)
        expected = spaceship.Vector(.6, .8)
        self.assertEqual(expected, v.unit())


class TestSpace(unittest.TestCase):
    def test_instance(self):
        space = spaceship.Space()
        self.assertTrue(isinstance(space, spaceship.Space))
        self.assertFalse(space.name)

        space = spaceship.Space("macrocosm")
        self.assertTrue(isinstance(space, spaceship.Space))
        self.assertEqual("macrocosm", space.name)

        space.name = "cosmos"
        self.assertEqual("cosmos", space.name)

    def test_str(self):
        space = spaceship.Space("Milky Way")
        self.assertEqual("Space: 'Milky Way'", space.__str__())
        sol = spaceship.Thing("Sol", x=3, y=3)
        space.append(sol)
        self.assertIn("contains", space.__str__())
        earth = spaceship.Thing("Earth", x=4, y=5)
        space.append(earth)
        self.assertEquals(3, space.__str__().count("\n"))

    def test_dotick(self):
        space = spaceship.Space("Earth's Orbit")
        moon = spaceship.Thing("Moon")
        space.append(moon)
        space.doTick(1)
        self.assertEqual(1, space.ticks)
        self.assertEqual(1, moon.ticks)


class TestThing(unittest.TestCase):
    def test_instance(self):
        ship = spaceship.Thing()
        self.assertTrue(isinstance(ship, spaceship.Thing))
        self.assertFalse(ship.name)
        self.assertFalse(ship.location)

        ship = spaceship.Thing("USS Enterprise")
        self.assertTrue(isinstance(ship, spaceship.Thing))
        self.assertEqual("USS Enterprise", ship.name)
        self.assertFalse(ship.location)

        ship = spaceship.Thing("Millennium Falcon", 3, 4)
        self.assertTrue(isinstance(ship, spaceship.Thing))
        self.assertEqual("Millennium Falcon", ship.name)
        self.assertTrue(isinstance(ship.location, spaceship.Vector))

        coord = spaceship.Vector(5, 2)
        ship = spaceship.Thing("Death Star", coord)
        self.assertTrue(isinstance(ship, spaceship.Thing))
        self.assertEqual("Death Star", ship.name)
        self.assertEqual(ship.location, coord)

        ship = spaceship.Thing("Bird of Prey", 3, 2, coord)
        self.assertTrue(isinstance(ship, spaceship.Thing))
        self.assertEqual("Bird of Prey", ship.name)
        self.assertEqual(ship.location, coord)

    def test_str(self):
        mars = spaceship.Thing("Mars", 1, 1)
        self.assertEqual("Thing: 'Mars' at (1.0, 1.0)", mars.__str__())

    def test_nonzero(self):
        planet = spaceship.Thing("Omicron Persei 8")
        self.assertFalse(planet.__nonzero__())

        planet.location = 33
        self.assertFalse(planet.__nonzero__())

        planet.location = spaceship.Vector(3, 2)
        self.assertTrue(planet.__nonzero__())

    def test_dotick(self):
        ship = spaceship.Thing("X Wing")
        ship.doTick(1)
        self.assertEqual(1, ship.ticks)

    def test_domove(self):
        ship = spaceship.Thing("UFO", 2, 2)
        ship.speed = 2
        ship.angle = 90
        ship.doMove()
        desiredLocation = spaceship.Vector(2, 4)
        self.assertEqual(ship.location, desiredLocation)

        ship.angle = 0
        ship.doMove()
        desiredLocation = spaceship.Vector(4, 4)
        self.assertEqual(ship.location, desiredLocation)

        ship.angle = 45
        ship.doMove()
        desiredLocation = spaceship.Vector(5, 5)
        self.assertEqual(ship.location, desiredLocation)

        ship.angle = 270
        ship.doMove()
        desiredLocation = spaceship.Vector(5, 3)
        self.assertEqual(ship.location, desiredLocation)


class TestTime(unittest.TestCase):
    def test_instance(self):
        time = spaceship.Time()
        self.assertTrue(isinstance(time, spaceship.Time))
        self.assertEqual(0, time.delay)
        self.assertEqual(0, time.tick)

        time = spaceship.Time(10)
        self.assertTrue(isinstance(time, spaceship.Time))
        self.assertEqual(10, time.delay)
        self.assertEqual(0, time.tick)

    def test_dotick(self):
        time = spaceship.Time()
        space = spaceship.Space("Universe")
        time.append(space)
        time.doTick()
        self.assertEqual(1, time.tick)
        self.assertEqual(1, time[0].ticks)

    def test_run(self):
        time = spaceship.Time(.01)
        space = spaceship.Space("Deep Space")
        ship = spaceship.Thing("USS Voyager")
        space.append(ship)
        time.append(space)

        time.run(5)
        self.assertEqual(5, time.tick)
        self.assertEqual(5, space.ticks)
        self.assertEqual(5, ship.ticks)


class TestFunctionality(unittest.TestCase):
    def test_flight(self):
        time = spaceship.Time()
        universe = spaceship.Space("The Universe")
        ship = spaceship.Thing("Asteroid", 2, 2)
        ship.angle = 90
        ship.speed = 2
        universe.append(ship)
        self.assertTrue(isinstance(ship.location, spaceship.Vector))
        time.append(universe)

        time.run(10)
        desiredLocation = spaceship.Vector(2, 22)
        self.assertEqual(ship.location, desiredLocation)

if __name__ == '__main__':
    unittest.main()

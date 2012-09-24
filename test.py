import unittest
import spaceship


class TestCoordinate(unittest.TestCase):
    """Test Coordinate functions"""
    def test_instance(self):
        coord = spaceship.Coordinate()
        self.assertIsNone(coord.x)
        self.assertIsNone(coord.y)

        coord = spaceship.Coordinate(3, 6)
        self.assertEqual(3, coord.x)
        self.assertEqual(6, coord.y)

        coord = spaceship.Coordinate(y=3, x=6)
        self.assertEqual(6, coord.x)
        self.assertEqual(3, coord.y)

    def test_nonzero(self):
        coord = spaceship.Coordinate()
        self.assertFalse(coord.__nonzero__())

        coord = spaceship.Coordinate(0, 0)
        self.assertTrue(coord.__nonzero__())

        coord = spaceship.Coordinate(1)
        self.assertFalse(coord.__nonzero__())

    def test_str(self):
        coord = spaceship.Coordinate(3, 4)
        self.assertEqual("(3, 4)", coord.__str__())

        coord = spaceship.Coordinate(-3, -4)
        self.assertEqual("(-3, -4)", coord.__str__())

        coord = spaceship.Coordinate(-3, 4)
        self.assertEqual("(-3, 4)", coord.__str__())

        coord = spaceship.Coordinate(3, -4)
        self.assertEqual("(3, -4)", coord.__str__())

    def test_add(self):
        coord1 = spaceship.Coordinate(3, 3)
        coord2 = spaceship.Coordinate(1)

        with self.assertRaises(TypeError):
            coord3 = coord1.__add__(coord2)

        coord1 = spaceship.Coordinate(3, 3)
        coord2 = spaceship.Coordinate(1, 1)
        coord3 = coord1.__add__(coord2)

        self.assertEqual(4, coord3.x)
        self.assertEqual(4, coord3.y)
        self.assertIsNot(coord1, coord3)
        self.assertIsNot(coord2, coord3)

        coord1 = spaceship.Coordinate(3, 3)
        coord2 = spaceship.Coordinate(-1, -1)
        coord3 = coord1.__add__(coord2)

        self.assertEqual(2, coord3.x)
        self.assertEqual(2, coord3.y)
        self.assertIsNot(coord1, coord3)
        self.assertIsNot(coord2, coord3)

    def test_sub(self):
        coord1 = spaceship.Coordinate(3, 3)
        coord2 = spaceship.Coordinate(1)

        with self.assertRaises(TypeError):
            coord3 = coord1.__sub__(coord2)

        coord1 = spaceship.Coordinate(3, 3)
        coord2 = spaceship.Coordinate(1, 1)
        coord3 = coord1.__sub__(coord2)

        self.assertEqual(2, coord3.x)
        self.assertEqual(2, coord3.y)
        self.assertIsNot(coord1, coord3)
        self.assertIsNot(coord2, coord3)

        coord1 = spaceship.Coordinate(3, 3)
        coord2 = spaceship.Coordinate(-1, -1)
        coord3 = coord1.__sub__(coord2)

        self.assertEqual(4, coord3.x)
        self.assertEqual(4, coord3.y)
        self.assertIsNot(coord1, coord3)
        self.assertIsNot(coord2, coord3)

    def test_radd(self):

        coord1 = spaceship.Coordinate(3, 3)
        coord2 = spaceship.Coordinate(1, 1)
        coord3 = coord1.__radd__(coord2)

        self.assertEqual(4, coord3.x)
        self.assertEqual(4, coord3.y)
        self.assertIsNot(coord1, coord3)
        self.assertIsNot(coord2, coord3)

    def test_rsub(self):

        coord1 = spaceship.Coordinate(3, 3)
        coord2 = spaceship.Coordinate(1, 1)
        coord3 = coord1.__rsub__(coord2)

        self.assertEqual(4, coord3.x)
        self.assertEqual(4, coord3.y)
        self.assertIsNot(coord1, coord3)
        self.assertIsNot(coord2, coord3)

    def test_eq(self):
        coord1 = spaceship.Coordinate(3, 3)
        coord2 = spaceship.Coordinate(1)

        with self.assertRaises(Exception):
            coord1.__eq__(coord2)

        coord1 = spaceship.Coordinate(3, 4)
        coord2 = spaceship.Coordinate(3, 4)
        self.assertTrue(coord1.__eq__(coord2))

    def test_ne(self):
        coord1 = spaceship.Coordinate(3, 3)
        coord2 = spaceship.Coordinate(1)

        with self.assertRaises(Exception):
            coord1.__ne__(coord2)

        coord1 = spaceship.Coordinate(3, 4)
        coord2 = spaceship.Coordinate(3, 4)
        self.assertFalse(coord1.__ne__(coord2))

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

class TestThing(unittest.TestCase):
    def test_instance(self):
        ship = spaceship.Thing();
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
        self.assertTrue(isinstance(ship.location, spaceship.Coordinate))

        coord = spaceship.Coordinate(5, 2)
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
        self.assertEqual("Thing: 'Mars' at (1, 1)", mars.__str__())

    def test_nonzero(self):
        planet = spaceship.Thing("Omicron Persei 8")
        self.assertFalse(planet.__nonzero__())

        planet.location = 33
        self.assertFalse(planet.__nonzero__())

        planet.location = spaceship.Coordinate(3, 2)
        self.assertTrue(planet.__nonzero__())

if __name__ == '__main__':
    unittest.main()

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
        coord2 = spaceship.Coordinate(1, 1)
        coord3 = coord1 + coord2

        self.assertEqual(4, coord3.x)
        self.assertEqual(4, coord3.y)
        self.assertIsNot(coord1, coord3)
        self.assertIsNot(coord2, coord3)

        coord1 = spaceship.Coordinate(3, 3)
        coord2 = spaceship.Coordinate(-1, -1)
        coord3 = coord1 + coord2

        self.assertEqual(2, coord3.x)
        self.assertEqual(2, coord3.y)

if __name__ == '__main__':
    unittest.main()

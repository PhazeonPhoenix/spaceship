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
        coord1 = spaceship.Coordinate(3, 4)
        coord2 = spaceship.Coordinate(3, 4)
        self.assertFalse(coord1.__ne__(coord2))


if __name__ == '__main__':
    unittest.main()

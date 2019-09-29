import unittest
from math import sqrt
from tests_homework.homework import Rectangle


class TestCases(unittest.TestCase):

    def setUp(self):
        self.rectangle1 = Rectangle(1, 1)
        self.rectangle2 = Rectangle(13, 5)
        self.rectangle3 = Rectangle(4, 3.5)

    def test_rectangle_perimeter(self):
        self.assertEqual(self.rectangle1.get_rectangle_perimeter(), 4)
        self.assertEqual(self.rectangle2.get_rectangle_perimeter(), 36)
        self.assertEqual(self.rectangle3.get_rectangle_perimeter(), 15)

    def test_rectangle_square(self):
        self.assertEqual(self.rectangle1.get_rectangle_square(), 1)
        self.assertEqual(self.rectangle2.get_rectangle_square(), 65)
        self.assertEqual(self.rectangle3.get_rectangle_square(), 14)

    def test_get_sum_of_corners(self):
        for i in range(1, 5):
            self.assertEqual(self.rectangle1.get_sum_of_corners(i), i * 90)
            self.assertEqual(self.rectangle2.get_sum_of_corners(i), i * 90)
            self.assertEqual(self.rectangle3.get_sum_of_corners(i), i * 90)

    def test_get_sum_of_invalid_num_of_corners(self):
        for i in range(5, 100):
            with self.assertRaises(ValueError):
                self.rectangle1.get_sum_of_corners(i)
                self.rectangle2.get_sum_of_corners(i)
                self.rectangle3.get_sum_of_corners(i)

    def test_get_rectangle_diagonal(self):
        self.assertEqual(self.rectangle1.get_rectangle_diagonal(), sqrt(2))
        self.assertEqual(self.rectangle2.get_rectangle_diagonal(), sqrt(194))
        self.assertEqual(self.rectangle3.get_rectangle_diagonal(), sqrt(28.25))

    def test_get_radius_of_circumscribed_circle(self):
        self.assertEqual(self.rectangle1.get_radius_of_circumscribed_circle(),
                         sqrt(0.5))
        self.assertEqual(self.rectangle2.get_radius_of_circumscribed_circle(),
                         sqrt(48.5))
        self.assertEqual(self.rectangle3.get_radius_of_circumscribed_circle(),
                         sqrt(7.0625))

    def test_get_radius_of_inscribed_circle(self):
        self.assertAlmostEqual(self.rectangle1.
                               get_radius_of_inscribed_circle(), 0.5)

    def test_get_radius_of_inscribed_circle_with_invalid_rectangle_param(self):
        with self.assertRaises(ValueError):
            self.rectangle2.get_radius_of_inscribed_circle()
            self.rectangle3.get_radius_of_inscribed_circle()


if __name__ == '__main__':
    unittest.main()

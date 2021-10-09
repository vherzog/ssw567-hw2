"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
from triangle import classify_triangle


class TestTriangleInputs(unittest.TestCase):
    """
    Test the inputs of the triangle function.
    """

    def test_invalid_string_input(self):
        """
        Test classify_triangle when input(s) are of type string.
        """
        self.assertEqual(classify_triangle('10', '7', '4'),
                         'InvalidInput', 'All inputs must be integers')

    def test_invalid_float_input(self):
        """
        Test classify_triangle when input(s) are of type float.
        """
        self.assertEqual(classify_triangle(10.0, 7.0, 4.0),
                         'InvalidInput', 'All inputs must be integers')

    def test_invalid_over_max_input(self):
        """
        Test classify_triangle when input(s) are slightly over maximum.
        """
        self.assertEqual(classify_triangle(201, 201, 201),
                         'InvalidInput', 'All inputs must be 0 < input <= 200')

    def test_invalid_at_max_input(self):
        """
        Test classify_triangle when input(s) are slightly over maximum.
        """
        self.assertNotEqual(classify_triangle(200, 200, 200),
                            'InvalidInput',
                            'All inputs must be 0 < input <= 200')

    def test_invalid_under_min_input(self):
        """
        Test classify_triangle when input(s) are slightly under minimum.
        """
        self.assertEqual(classify_triangle(0, 0, 0),
                         'InvalidInput', 'All inputs must be 0 < input <= 200')

    def test_invalid_at_min_input(self):
        """
        Test classify_triangle when input(s) are slightly under minimum.
        """
        self.assertNotEqual(classify_triangle(1, 1, 1),
                            'InvalidInput',
                            'All inputs must be 0 < input <= 200')


class TestTriangles(unittest.TestCase):
    """
    Test the outputs of the triangle function.
    """

    def test_invalid_sum_sides(self):
        """
        Test classify_triangle when inputs do not form a triangle.
        """
        self.assertEqual(classify_triangle(10, 7, 2),
                         'NotATriangle', '10,7,2 is not a triangle')
        self.assertEqual(classify_triangle(7, 10, 2),
                         'NotATriangle', '7,10,2 is not a triangle')
        self.assertEqual(classify_triangle(7, 2, 10),
                         'NotATriangle', '7,2,10 is not a triangle')

    def test_valid_equilateral_triangle(self):
        """
        Test classify_triangle when inputs for an equilateral triangle.
        """
        self.assertEqual(classify_triangle(1, 1, 1),
                         'Equilateral', '1,1,1 should be equilateral')

    def test_valid_right_triangle(self):
        """
        Test classify_triangle when inputs for a right triangle.
        """
        self.assertEqual(classify_triangle(3, 4, 5), 'Right',
                         '3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle(5, 3, 4), 'Right',
                         '5,3,4 is a Right triangle')
        self.assertEqual(classify_triangle(4, 5, 3), 'Right',
                         '4,5,3 is a Right triangle')

    def test_valid_scalene_triangle(self):
        """
        Test classify_triangle when inputs for a scalene triangle.
        """
        self.assertEqual(classify_triangle(4, 6, 9), 'Scalene',
                         '4,6,9 is a Scalene triangle')
        self.assertEqual(classify_triangle(9, 4, 6), 'Scalene',
                         '9,4,6 is a Scalene triangle')
        self.assertEqual(classify_triangle(6, 9, 4), 'Scalene',
                         '6,9,4 is a Scalene triangle')

    def test_valid_isosceles_triangle(self):
        """
        Test classify_triangle when inputs for an isosceles triangle.
        """
        self.assertEqual(classify_triangle(3, 2, 2),
                         'Isosceles', '3,2,2 is a Isosceles triangle')
        self.assertEqual(classify_triangle(2, 3, 2),
                         'Isosceles', '2,3,2 is a Isosceles triangle')
        self.assertEqual(classify_triangle(2, 2, 3),
                         'Isosceles', '2,2,3 is a Isosceles triangle')


if __name__ == '__main__':
    unittest.main()

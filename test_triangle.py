"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testInvalidStringInputA(self):
        self.assertEqual(classify_triangle('10', 7, 4),
                         'InvalidInput', 'All inputs must be integers')

    def testInvalidStringInputB(self):
        self.assertEqual(classify_triangle(10, '7', 4),
                         'InvalidInput', 'All inputs must be integers')

    def testInvalidStringInputC(self):
        self.assertEqual(classify_triangle(10, 7, '4'),
                         'InvalidInput', 'All inputs must be integers')

    def testInvalidFloatInputA(self):
        self.assertEqual(classify_triangle(10.0, 7, 4),
                         'InvalidInput', 'All inputs must be integers')

    def testInvalidFloatInputB(self):
        self.assertEqual(classify_triangle(10, 7.0, 4),
                         'InvalidInput', 'All inputs must be integers')

    def testInvalidFloatInputC(self):
        self.assertEqual(classify_triangle(10, 7, 4.0),
                         'InvalidInput', 'All inputs must be integers')

    def testInvalidOverMaxInputA(self):
        self.assertEqual(classify_triangle(201, 200, 200),
                         'InvalidInput', 'All inputs must be 0 < input <= 200')

    def testInvalidOverMaxInputB(self):
        self.assertEqual(classify_triangle(200, 201, 200),
                         'InvalidInput', 'All inputs must be 0 < input <= 200')

    def testInvalidOverMaxInputC(self):
        self.assertEqual(classify_triangle(200, 200, 201),
                         'InvalidInput', 'All inputs must be 0 < input <= 200')

    def testInvalidUnderMinInputA(self):
        self.assertEqual(classify_triangle(0, 1, 1),
                         'InvalidInput', 'All inputs must be 0 < input <= 200')

    def testInvalidUnderMinInputB(self):
        self.assertEqual(classify_triangle(1, 0, 1),
                         'InvalidInput', 'All inputs must be 0 < input <= 200')

    def testInvalidUnderMinInputC(self):
        self.assertEqual(classify_triangle(1, 1, 0),
                         'InvalidInput', 'All inputs must be 0 < input <= 200')

    def testInvalidSumSidesA(self):
        self.assertEqual(classify_triangle(10, 7, 2),
                         'NotATriangle', '10,7,2 is not a triangle')

    def testValidSumSidesA(self):
        self.assertEqual(classify_triangle(10, 7, 4),
                         'Scalene', '10,7,4 is a Scalene triangle')

    def testInvalidSumSidesB(self):
        self.assertEqual(classify_triangle(7, 10, 2),
                         'NotATriangle', '7,10,2 is not a triangle')

    def testValidSumSidesB(self):
        self.assertEqual(classify_triangle(7, 10, 4),
                         'Scalene', '7,10,4 is a Scalene triangle')

    def testInvalidSumSidesC(self):
        self.assertEqual(classify_triangle(7, 2, 10),
                         'NotATriangle', '7,2,10 is not a triangle')

    def testValidSumSidesC(self):
        self.assertEqual(classify_triangle(7, 4, 10),
                         'Scalene', '7,2,4 is a Scalene triangle')

    def testValidEquilateralTriangles(self):
        self.assertEqual(classify_triangle(1, 1, 1),
                         'Equilateral', '1,1,1 should be equilateral')

    def testValidRightTriangleA(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right',
                         '3,4,5 is a Right triangle')

    def testValidRightTriangleB(self):
        self.assertEqual(classify_triangle(5, 3, 4), 'Right',
                         '5,3,4 is a Right triangle')

    def testValidRightTriangleC(self):
        self.assertEqual(classify_triangle(4, 5, 3), 'Right',
                         '4,5,3 is a Right triangle')

    def testValidScaleneTriangleA(self):
        self.assertEqual(classify_triangle(4, 6, 9), 'Scalene',
                         '4,6,9 is a Scalene triangle')

    def testValidScaleneTriangleB(self):
        self.assertEqual(classify_triangle(9, 4, 6), 'Scalene',
                         '9,4,6 is a Scalene triangle')

    def testValidScaleneTriangleC(self):
        self.assertEqual(classify_triangle(6, 9, 4), 'Scalene',
                         '6,9,4 is a Scalene triangle')

    def testValidIsoscelesTriangleA(self):
        self.assertEqual(classify_triangle(3, 2, 2),
                         'Isosceles', '3,2,2 is a Isosceles triangle')

    def testValidIsoscelesTriangleB(self):
        self.assertEqual(classify_triangle(2, 3, 2),
                         'Isosceles', '2,3,2 is a Isosceles triangle')

    def testValidIsoscelesTriangleC(self):
        self.assertEqual(classify_triangle(2, 2, 3),
                         'Isosceles', '2,2,3 is a Isosceles triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

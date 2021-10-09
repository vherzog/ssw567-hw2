"""Simple python program to classify triangles.

Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

@author: jrr
@author: rk
"""


def validate_input(side_a, side_b, side_c):
    """
    Validate inputs of side_a, side_b, and side_c.

    return: bool
    """
    validity = True
    # verify that all 3 inputs are integers
    if not(isinstance(side_a, int)
           and isinstance(side_b, int)
           and isinstance(side_c, int)):
        validity = False
    # require that the input values be >= 0 and <= 200
    elif side_a > 200 or side_b > 200 or side_c > 200:
        validity = False
    elif side_a <= 0 or side_b <= 0 or side_c <= 0:
        validity = False
    return validity


def classify_triangle(side_a, side_b, side_c):
    """Fix the faulty logic below until the code passes all of you test cases.

    This function returns a string with the type of triangle from three integer
    values corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isosceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, return 'NotATriangle'
        If sum of any two sides equals the square of the 3rd, return 'Right'
    """
    if not validate_input(side_a, side_b, side_c):
        return "InvalidInput"

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (side_a + side_b < side_c) or \
        (side_b + side_c < side_a) or \
            (side_a + side_c < side_b):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if ((side_a ** 2) + (side_b ** 2)) == (side_c ** 2) or \
        ((side_b ** 2) + (side_c ** 2)) == (side_a ** 2) or \
            ((side_a ** 2) + (side_c ** 2)) == (side_b ** 2):
        return 'Right'
    if side_a == side_b and side_b == side_c and side_c == side_a:
        return 'Equilateral'
    if (side_a != side_b) and (side_b != side_c) and (side_a != side_c):
        return 'Scalene'
    return 'Isosceles'

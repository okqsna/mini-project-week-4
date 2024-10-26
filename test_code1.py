"""
application for checking
if circle is inscribed in a square.
"""
def check_circle(radius: float | int, side: float | int) -> bool:
    """
    function checks if circle is 
    inscribed in square by using 
    formula: r = a / 2

    :param radius: int, radius of a circle
    :param side: int, side of a square
    :return: bool, True if radius is equal 
    to half of the side of the square, False otherwise
    >>> check_circle(8, 16)
    True
    >>> check_circle(9, 3.5)
    False
    """
    if not isinstance(radius, float) or not isinstance(side, float)\
        or not isinstance(radius, int) or not isinstance(side, int):
        return None
    if radius < 0 or side < 0:
        return None
    return radius == side / 2

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

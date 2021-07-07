import math


def distance(x1, y1, x2, y2):
    """
    Calculates the euclidean distance between two points on a plane
    :param x1: The x-coordinate of the first point
    :param y1: The y-coordinate of the first point
    :param x2: The x-coordinate of the second point
    :param y2: The y-coordinate of the second point
    :return: a float that is the euclidean distance between the two
    points

    >>> distance(1,2,3,4)
    2.8284271247461903

    >>> distance(4,5,7,2)
    4.242640687119285
    """

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


if __name__ == '__main__':
    print("Calculating Euclidean Distance")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
dis = distance(x1, y1, x2, y2)
print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is: {dis}")


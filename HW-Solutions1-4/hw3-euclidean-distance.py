import math

def distance(x1, y1, x2, y2):
    """
    Calculates the euclidean distance between two points on a plane
    :param x1: The x-coordinate of the first point
    :param y1: The y-coordinate of the first point
    :param x2: The x-coordinate of the second point
    :param y2: The y-coordinate of the second point
    :return: a float that is the euclidean distance between the two points

    >>> distance(1.2, 3.4, 5.6, 7.8)
    6.222539674441618
    >>> distance(0, 0, 1, 1)
    1.4142135623730951
    """
    term1 = (x2 - x1) ** 2
    term2 = (y2 - y1) ** 2
    return math.sqrt(term1 + term2)

if __name__ == '__main__':
    print("Calculating Euclidean Distance")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is: "
          f"{distance(x1,y1,x2,y2)}")



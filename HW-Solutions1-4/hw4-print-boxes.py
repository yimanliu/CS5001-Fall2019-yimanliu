def print_box(s, width, height, filled = False):
    """
    Prints a box of width and height, where the total width is len(s) *
    width, and the total number of lines is height.
    :param s: the string that makes up the sides and top of the box (and
    inside, if it is a filled box)
    :param width: the width of the box, in multiples of len(s)
    :param height: the number of lines of height
    :param filled: an optional boolean. If filled is True, the box should be
    completely filled in. If it is false (default), the box should just have
    sides.
    :return: None
    >>> print_box("abc", 6, 4, filled=True)
    abcabcabcabcabcabc
    abcabcabcabcabcabc
    abcabcabcabcabcabc
    abcabcabcabcabcabc
    >>> print_box("X", 10, 6)
    XXXXXXXXXX
    X        X
    X        X
    X        X
    X        X
    XXXXXXXXXX

    """
    print(s * width)
    for i in range(height - 2):
        print(s, end='')
        if filled:
            print(s * (width - 2), end='')
        else:
            print(' ' * len(s) * (width - 2), end='')
        print(s)
    print(s * width)

if __name__ == "__main__":
    print_box('X', 10, 6)
    print()
    print_box('*', 4, 9, filled=True)
    print()
    print_box('abc', 6, 4)
    print()
    print_box('abc', 6, 4, filled=True)

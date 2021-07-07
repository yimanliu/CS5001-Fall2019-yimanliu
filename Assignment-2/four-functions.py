import math


# Four functions
def funcA(a_number):
    """
    funcA adds 42 to a_number (we can call this result "bigger_num")
    It then prints, "The number plus 42 is X.", where X is bigger_num.
    Then funcA calls funcB with bigger_num if the bigger_num is even,
    and calls funcC with bigger_num if bigger_num is odd.
    :param a_number: an integer
    :return: the number returned by either funcB or funcC

    >>> funcA(15)
    The number plus 42 is 57.
    The number is odd!
    56

    >>> funcA(25)
    The number plus 42 is 67.
    The number is odd!
    66
    """
    ret = a_number + 42
    print("The number plus 42 is {}.".format(ret))
    if ret % 2 == 0:
        return funcB(ret)
    elif ret % 2 != 0:
        return funcC(ret)


def funcB(value):
    """
    funcB calls funcD with value if value is greater than BIGNUM (defined below)
    If the number is not greater than BIGNUM, it prints "The number chosen
    was small and even."
    :param value: an even integer
    :return: if the number is not greater than BIGNUM, the return value will
    be 1 + value.
    Otherwise, the return value is the number returned by funcD

     >>> funcB(22)
     The number chosen was small and even.
     23
     >>> funcB(46)
     The number chosen was small and even.
     47
    """
    BIGNUM = 256
    if value > BIGNUM:
        return funcD(value)
    elif value <= BIGNUM:
        print("The number chosen was small and even.")
        return 1 + value


def funcC(value):
    """
    funcC prints "The number is odd!"
    :param value: an odd integer
    :return: value - 1

    >>> funcC(33)
    The number is odd!
    32
    >>> funcC(21)
    The number is odd!
    20
    """
    print("The number is odd!")
    return value - 1


def funcD(value):
    """
    funcD prints "Wow, that is a big number!"
    :param value: an integer
    :return: value * -1

    >>> funcD(23456)
    Wow, that is a big number!
    -23456

    >>> funcD(43256)
    Wow, that is a big number!
    -43256
    """
    print("Wow, that is a big number!")
    return value * -1


if __name__ == "__main__":
    for v in [13, 10000, 20, 1, 100, -5, -6]:
        print("Calling funcA({})".format(v))
        print("Return value from v == {}: {}".format(v, funcA(v)))
        print()

# end of program

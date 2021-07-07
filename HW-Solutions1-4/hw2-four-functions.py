# Four functions
def funcA(a_number):
    """funcA adds 42 to a_number (we can call this result "bigger_num")
       It then prints, "The number plus 42 is X.", where X is bigger_num.
       Then funcA calls funcB with bigger_num if the bigger_num is even,
       and calls funcC with bigger_num if bigger_num is odd.
       :param a_number: an integer
       :return: the number returned by either funcB or funcC
    """
    bigger_num = a_number + 42
    print("The number plus 42 is {}.".format(bigger_num))
    if bigger_num % 2 == 0:
        return funcB(bigger_num)
    else:
        return funcC(bigger_num)


def funcB(value):
    """
    funcB calls funcD with value if value is greater than BIGNUM (defined below)
    If the number is not greater than BIGNUM, it prints "The number chosen
    was small and even."
    :param value: an even integer
    :return: if the number is not greater than BIGNUM, the return value will
    be 1 + value.
    Otherwise, the return value is the number returned by funcD
    """
    BIGNUM = 256

    if value > BIGNUM:
        return funcD(value)
    else:
        print("The number chosen was small and even.")
        return 1 + value


def funcC(value):
    """
    funcC prints "The number is odd!"
    :param value: an odd integer
    :return: value - 1
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
    """
    print("Wow, that is a big number!")
    return -value;

if __name__ == "__main__":
    for v in [13, 10000, 20, 1, 100, -5, -6]:
        print("Calling funcA({})".format(v))
        print("Return value from v == {}: {}".format(v, funcA(v)))
        print()
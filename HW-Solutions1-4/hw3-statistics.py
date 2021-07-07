# functions to calculate the mean and standard deviation for a list of numbers

import math


def mean(number_list):
    """
    Calculates the mean for a list of values
    :param number_list: the list of values, which can be either ints or floats. E.g., [1, 5, 19, 23]
    :return: the mean of the values in the list

    >>> mean([1,5,19,23])
    12.0
    """
    if len(number_list) == 0:
        return None
    number_sum = sum(number_list)
    # the above line is equivalent to:
    # sum = 0
    # for n in number_list:
    #    sum += n

    return number_sum / len(number_list)


def stdev(number_list):
    """
    Calculates the standard deviation of a list of values
    :param number_list: the list of values, which can be either ints or floats. E.g., [1, 5, 19, 23]
    :return: the standard deviation of the values in the list

    >>> stdev([1,5,19,23])
    9.219544457292887
    """
    if len(number_list) == 0:
        return None

    list_mean = mean(number_list)

    # your code goes here
    sum_mean_diffs_sq = 0
    for val in number_list:
        sum_mean_diffs_sq += (val - list_mean)**2

    return math.sqrt(1 / len(number_list) * sum_mean_diffs_sq)


if __name__ == "__main__":
    numbers = []
    while True:
        next_num = input("Enter the next number in the list (blank line when you are done): ")
        if next_num == "":
            break
        numbers.append(int(next_num))

    print(f"The mean of your list of numbers is {mean(numbers)}")
    print(f"The standard deviation of your list of numbers is {stdev(numbers)}")

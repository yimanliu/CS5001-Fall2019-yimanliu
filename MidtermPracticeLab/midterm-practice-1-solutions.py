# practice midterm questions
# Answer the following questions or fill in the required code


# Question 1. What does the function below do? Put your answer into the empty
#             docstring
def mystery1(a):
    """
    Answer: Returns a + a
    :param a: an integer
    :return: the mystery result
    """
    a += a
    return a


# Question 2. What does the function below do? Put your answer into the empty
#             docstring
def mystery2(lst):
    """
    Answer: Returns all all but the last item in the list
    :param lst: A list of strings
    :return: the result
    """
    return lst[:-1]


# Question 3. What does the function below do? Put your answer into the empty
#             docstring
def mystery3(lst):
    """
    Answer: Creates a list from the items at the even indexes in the
    original list, and then appends the items at the odd indexes in the
    original list.
    :param lst: A list
    :return: the result
    """
    newlist = []
    for val in range(0, len(lst), 2):
        newlist.append(lst[val])

    for val in range(1, len(lst), 2):
        newlist.append(lst[val])

    return newlist


# Question 4. What does the function below do? Put your answer into the empty
#             docstring
def mystery4(lst_a, lst_b):
    """
    Answer: Prints out itemA:itemB for each element in both lists.
    :param lst_a: The first list
    :param lst_b: The second list
    :return: None
    """
    for v1, v2 in zip(lst_a, lst_b):
        print(f"{v1}:{v2}")


# Question 5a. Write a function that finds the smallest and largest number in
# a list and returns the values as a Tuple. E.g., if the list was
# [8, 2, 15, 5, 7, 1, 11], then the function will return (1, 15). You are not
# allowed to use the min() or max() functions to write this function.
# Question 5b. Write a doctest to check your answer.
def get_range(lst):
    """
    :param lst: A list
    :return: the smallest and largest element in the list, as a Tuple
    >>> get_range([14, 8, 5, 4, 23, 17, 25, 9, 11, 6, 23, 19])
    (4, 23)
    """
    min = lst[0]
    max = lst[0]
    for v in lst[1:]:
        if v < min:
            min = v
        if v > max:
            max = v
    return (min, max)

# Question 6. Write a function to open a file and count the number of lines
# in the file. If the file does not open correctly, return None, otherwise,
# return the line count. See the reference sheet for the error associated
# with opening a file.
def count_lines(filename):
    """
    :param filename: The file to open
    :return: None if the file does not open correctly, or the line count
    """
    try:
        with open(filename, "r") as f:
            return len(f.readlines())
    except FileNotFoundError:
        return None


# Question 7. What does the following recursive function do? If you are
# having trouble figuring it out, try it out on paper, one line at a time
# with a small value, like 4. Then try with -5, etc. Write your answer in the
# docstring below
def recursive_mystery(n):
    """
    Answer: Returns 3 * n
    :param value: the value
    :return: the return value
    """
    if n < 0:
        return -recursive_mystery(-n)
    if n == 0:
        return 0
    if n == 1:
        return 3
    return recursive_mystery(n - 1) + 3


# Question 8a: Write a list comprehension that returns the first n characters
# for each string in a list of strings, but only if the string is
# greater than or equal to n characters in length.
# Example:
# word_filter(['the quick brown fox jumps over the lazy dog'], 4) should return
# ['quic', 'brow', 'jump', 'over', 'lazy']
# Question 8b: Write a doctest for this function.
def word_filter(lst, n):
    """
    :param lst: A list of strings
    :param n: the minimum length of the string
    :return: a new list with the filtered values
    >>> word_filter(['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', \
    'lazy', 'dog'], 4)
    ['quic', 'brow', 'jump', 'over', 'lazy']
    """
    return [x[:n] for x in lst if len(x) >= n]


# Question 9: Write the output of the function below when called with
# "the cat in the hat"
def mystery5(input_str):
    """
    Answer:
    word 0:'the' and word 1:'cat' and word 2:'in' and word 3:'the' and word 4:'hat'.
    :param input_str: A string
    :return: None
    """
    words = input_str.split(' ')
    print('word', end='')
    for i, s in enumerate(words):
        print(f" {i}:'{s}'", end='')
        if i == len(words) - 1:
            print(".")
        else:
            print(" and word", end='')


# Question 10: Write a function that asks a user for a list of name/age
# key/value pairs, and then creates a dictionary with that data.
# For example:
# Please enter a name (blank line to finish): Chris
# Please enter Chris's age: 47
# Please enter a name (blank line to finish): Juno
# Please enter Juno's age: 2
# Please enter a name (blank line to finish): Jupiter
# Please enter Jupiter's age: 1
# Please enter a name (blank line to finish):
#
# The return value should be:
# {
#   'Chris': 47,
#   'Juno': 2,
#   'Jupiter': 1,
# }
def name_and_ages():
    """
    Asks for a list of name/age key/value pairs, puts them into a dictionary
    and returns the dict.
    :return: a dict with the key/value pairs entered by the user
    """
    d = {}
    while True:
        name = input("Please enter a name (blank line to finish): ")
        if name == '':
            break
        age = int(input(f"Please enter {name}'s age: "))
        d[name] = age
    return d


def main():
    # uncomment the lines below to check your answers
    print(f"Question 1: {mystery1(42)}")
    print()

    print(f"Question 2: {mystery2(['cat','dog','mouse','bat'])}")
    print()

    print(f"Question 3: "
         f"{mystery3(['apple', 'banana', 'chocolate','dragonfruit','eggs'])}")
    print()

    print("Question 4: ")
    print(mystery4(['cat', 'dog', 'mouse', 'bat'], ['milk', 'kibble', 'cheese',
                                            'fruit']))
    print()

    print("Question 5:")
    print(get_range([14, 8, 5, 4, 23, 17, 25, 9, 11, 6, 23, 19]))
    print()

    print("Question 6:")
    print(count_lines('no-file.txt'))
    print(count_lines('declaration-of-independence.txt'))
    print()

    print("Question 7:")
    print(recursive_mystery(5))
    print(recursive_mystery(0))
    print(recursive_mystery(-12))
    print()

    print("Question 8:")
    print(word_filter(['the', 'quick', 'brown', 'fox', 'jumps', 'over',
                       'the', 'lazy', 'dog'], 4))
    print()

    print("Question 9:")
    mystery5('the cat in the hat')
    print()

    print("Question 10:")
    d = name_and_ages()
    for name in sorted(d.keys()):
        print(f"{name} is {d[name]} year(s) old.")


if __name__ == "__main__":
    main()
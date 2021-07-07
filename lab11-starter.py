import math
import queue


def find_str(pat, txt):
    """
    Returns the index of the first occurrence of pat in txt, and -1 if
    pat is not contained in txt
    :param pat: the string pattern to search for
    :param txt: the text to search through
    :return: the index of the first occurrence of pat in txt, -1 if not found
    >>> find_str("cat", "the cat in the hat")
    4
    >>> find_str("aab", "aaaaab")
    3
    >>> find_str("abcd", "abc")
    -1
    """
    for i in range(len(txt) - len(pat) + 1):
        found = True
        for c, c_to_find in zip(txt[i:], pat):
            if c != c_to_find:
                found = False
                break
        if found:
            return i
    return -1


def find_str_all(pat, txt, overlap=True):
    """
    Returns a list of all the indexes of the occurrences of pat in txt, and an
    empty list if pat is not contained in txt
    :param overlap:
    :param pat: the string pattern to search for
    :param txt: the text to search through
    :return: a list of all the indexes of pat in txt
    >>> find_str_all("cat", "the cat in the cat and the cat")
    [4, 15, 27]

    >>> find_str_all("aba", "abacdababa")
    [0, 5, 7]

    >>> find_str_all("aaa", "aaaaaaaaaa")
    [0, 1, 2, 3, 4, 5, 6, 7]

    """
    # TODO: // modify the following so it finds all the elements
    all_matches = []
    i = 0
    while i < len(txt) - len(pat) + 1:
        found = True
        for c, c_to_find in zip(txt[i:], pat):
            if c != c_to_find:
                found = False
                break
        if found:
            all_matches.append(i)
            if not overlap:
                i += len(pat)
            else:
                i += 1
        else:
            i += 1

    if len(all_matches) == 0:
        return -1
    return all_matches


def insertion_sort(lst):
    """
    Sorts the list using insertion sort
    :param lst: a list
    :return: None
    >>> lst = [9, 5, 10, 8, 12, 11, 14, 2, 22, 43]
    >>> insertion_sort(lst)
    >>> print(lst)
    [2, 5, 8, 9, 10, 11, 12, 14, 22, 43]
    >>> lst = [6, 5, 4, 3, 2, 1]
    >>> insertion_sort(lst)
    >>> print(lst)
    [1, 2, 3, 4, 5, 6]
    >>> lst = [13, 45, 1, 3, 2, 8]
    >>> insertion_sort(lst)
    >>> print(lst)
    [1, 2, 3, 8, 13, 45]
    >>> lst = [23, 13, 3, 33, 43, 53]
    >>> insertion_sort(lst)
    >>> print(lst)
    [3, 13, 23, 33, 43, 53]
    """
    # TODO: Write the insertion sort function
    for i in range(1, len(lst)):
        for j in range(i, 0, -1):
            if lst[j] < lst[j - 1]:
                temp = lst[j - 1]
                lst[j - 1] = lst[j]
                lst[j] = temp


def radix_sort(lst):
    """
    Sorts lst in place using the radix sort algorithm
    :param lst: a list
    :return: None
    >>> lst = [1, 9999999, 10000000, 10, 100, 999, 99999, 999999]
    >>> radix_sort(lst)
    >>> print(lst)
    [1, 10, 100, 999, 99999, 999999, 9999999, 10000000]
    """
    # TODO: (Bonus) Write radix sort, or copy radix sort from here:
    #  http://course.ccs.neu.edu/cs5001f19-sf/static/code/radix-sort.py
    #  and go through it very carefully
    queues = [queue.Queue() for x in range(10)]
    # determine the maximum number of digits in the list
    max_digits = 0
    for num in lst:
        max_digits = max(max_digits, int(math.log10(num) + 1))
    for i in range(max_digits):
        # sort by next digit
        for num in lst:
            digit_to_check = (num % (10 ** (i + 1))) // (10 ** i)
            queues[digit_to_check].put(num)
        # remove from all queues back into the list
        lst.clear()
        for q in queues:
            while not q.empty():
                lst.append(q.get())


def main():
    print("Tests:")
    print(find_str("cat", "the cat in the hat"))
    print("Should print: 4")
    print(find_str("aab", "aaaaab"))
    print("Should print: 3")
    print(find_str("abcd", "abc"))
    print("Should print: -1")
    print()

    print(find_str_all("cat", "the cat in the cat and the cat"))
    print("Should print: [4, 15, 27]")

    print(find_str_all("aba", "abacdababa"))
    print("Should print: [0, 5, 7]")

    print(find_str_all("aaa", "aaaaaaaaaa"))
    print("Should print: [0, 1, 2, 3, 4, 5, 6, 7]")
    print()

    lst = [9, 5, 10, 8, 12, 11, 14, 2, 22, 43]
    print(f"Original list: {lst}")
    insertion_sort(lst)
    print(f"Sorted list:   {lst}")
    print()

    lst = [1, 9999999, 10000000, 10, 100, 999, 99999, 999999]
    print(f"Original list: {lst}")
    radix_sort(lst)
    print(f"Sorted list:   {lst}")


if __name__ == "__main__":
    main()

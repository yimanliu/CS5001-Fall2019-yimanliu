def character_indexes(s, characters):
    """
    Prints a list of the indexes for each character in the characters list.
    For example:
    string_search("a long time ago", ['a', 'l', 'r', 'g', 'o'] would print:
    a is found at 0, 12
    l is found at 2
    r is not in the string
    g is found at 5, 13
    o is found at 3, 14
    :param s: a string
    :param characters: an iterable (e.g., list, tuple, etc.) with characters to
    search for
    :return:
    >>> character_indexes("a long time ago", ['a', 'l', 'r', 'g', 'o'])
    a is found at 0, 12
    l is found at 2
    r is not in the string
    g is found at 5, 13
    o is found at 3, 14
    >>> character_indexes("aaabbabbcbabab", ['a','b','c','d'])
    a is found at 0, 1, 2, 5, 10, 12
    b is found at 3, 4, 6, 7, 9, 11, 13
    c is found at 8
    d is not in the string
    """
    for c in characters:
        startIndex = 0
        while True:
            nextPos = s.find(c, startIndex)
            if nextPos == -1:
                if startIndex == 0:
                    print(f"{c} is not in the string")
                else:
                    print()
                break
            if startIndex == 0:
                print(f"{c} is found at {nextPos}", end='')
            else:
                print(f", {nextPos}", end='')
            startIndex = nextPos + 1


if __name__ == "__main__":
    character_indexes("a long time ago", ['a', 'l', 'r', 'g', 'o'])
    print()
    character_indexes("aaabbabbcbabab", ['a','b','c','d'])
    print()
    character_indexes("mississippi massachusetts",
                      sorted(list(set("mississippi massachusetts"))))

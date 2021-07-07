def filter_words(wordlist, min_length, max_length, letters):
    """
    Returns a list of words that meets the requirements based on min_length,
    max_length, and letters, as follows:
    The list should only contain words that are between min_length and
    max_length (inclusive). The words must contain all the letters in the
    letters list (but can have other letters, too).
    :param wordlist: A list of words
    :param min_length: the minimum length of a word in the list
    :param max_length: the maximum length of a word in the list
    :param letters: the only letters that can be in the words
    :return: a list that meets the filtering requirements
    >>> with open("words.txt") as f:
    ...    wordlist = f.readlines()
    >>> wordlist = [x[:-1].lower() for x in wordlist]
    >>> filter_words(wordlist, 3, 10, ['a','r','t','m'])
    ['agreement', 'democrat', 'democratic', 'important', 'majority', \
'market', 'material', 'matter', 'military', 'treatment']
    """
    length_filtered_list = [x for x in wordlist if min_length <= len(x) <=
                       max_length]
    final_list = []
    for word in length_filtered_list:
        word_ok = True
        for c in letters:
            if c not in word:
                word_ok = False
                break
        if word_ok:
            final_list.append(word)
    return final_list


if __name__ == "__main__":
    with open("words.txt") as f:
        wordlist = f.readlines()
    wordlist = [x[:-1].lower() for x in wordlist]
    print(filter_words(wordlist, 3, 10, ['a','r','t','m']))
    print(filter_words(wordlist, 3, 10, ['a', 'x']))

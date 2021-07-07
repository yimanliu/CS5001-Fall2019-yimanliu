# Author Lei Feng, Yiman Liu

CHARACTERS_IN_ALPHABET = 26


def encrypt(plaintext, shift_amount):
    """
    Encrypt string plaintext using a Caesar cipher by shift_amount
    :param plaintext: the string to encrypt
    :param shift_amount: an integer between 0 and 25
    :return: the ciphertext string, with each character shifted by shift_amount.

    >>> encrypt("hello", 1)
    'ifmmp'
    >>> encrypt("secret", 18)
    'kwujwl'
    """
    if not (0 < shift_amount < CHARACTERS_IN_ALPHABET):
        shift_amount = 1
    # your code goes here
    s = ''
    for ch in plaintext:
        if ch.isalpha():
            ch_num = ord(ch.lower())
            letter_between = ch_num - ord('a')
            letter_shift = (letter_between + shift_amount) % 26
            shift_letter = chr(letter_shift + ord('a'))
            s += shift_letter
        else:
            s += ch
    return s


def decrypt(ciphertext, shift_amount):
    """
    Decrypts string ciphertext using a Caesar cipher when the original shift
    was shift_amount Assumption: ciphertext will be in lowercase :param
    ciphertext: the string to decrypt :param shift_amount: an integer between
    0 and 25 :return: the decrypted string

    >>> decrypt("ifmmp", 1)
    'hello'
    >>> decrypt('kwujwl', 18)
    'secret'
    """
    if not (0 < shift_amount < CHARACTERS_IN_ALPHABET):
        shift_amount = 1
    # your code goes here
    s = ''
    for ch in ciphertext:
        if ch.isalpha():
            ch_num = ord(ch.lower())
            letter_between = ch_num - ord('a')
            if (letter_between - shift_amount) >= 0:
                letter_shift = (letter_between - shift_amount) % 26
            else:
                letter_shift = (letter_between + (26 - shift_amount)) % 26
            shift_letter = chr(letter_shift + ord('a'))
            s += shift_letter
        else:
            s += ch
    return s


def slide(string, slide_num):
    """
    slide string
    :param string:
    :param slide_num:
    :return: slide result

    >>> slide("great",3)
    'eatgr'
    >>> slide("cool",5)
    'lcoo'
    """
    my_list = [None] * len(string)
    for i in range(0, len(string)):
        my_list[(i + slide_num) % len(string)] = string[i]
    return ''.join(my_list)


def run_test(string):
    """
    run our test
    :param string:
    :return: test result

    >>> run_test("tcxlsr")
    sbwkrq
    ravjqp
    qzuipo
    python
    oxsgnm
    >>> run_test("fbjxtrj")
    eaiwsqi
    dzhvrph
    cyguqog
    bxftpnf
    awesome
    """
    for i in range(1, 6):
        print(decrypt(string, i))


if __name__ == "__main__":
    print("Let's Encrypt!")
    print(encrypt("He1234llo", 1))
    print(encrypt("secret", 18))
    print(decrypt(encrypt("He1234llo", 25), 25))  # should print "hello"
    print(decrypt(encrypt("secret", 7), 7))  # should print "secret"

    run_test("itgcvlqd")
    run_test("fbjxtrj")
    run_test("tcxlsr")

    print(slide(encrypt("decryption", 4), 1))

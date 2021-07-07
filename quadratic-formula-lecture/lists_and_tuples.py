if __name__ == "__main__":
    my_list = [37, 39, 0, 43, 8, -15, 23, 0, -5, 30, -10, -34, 30, -5, 28, 9,
               18, -1, 31, -12]
    print(my_list)

    # create a list called "positives" that contains all the positive values
    # in my_list
    positives = [x for x in my_list if x > 0]
    print(positives)

    # create a list called "negatives" that contains all the negative values
    # in my_list
    negatives = [x for x in my_list if x < 0]
    print(negatives)

    # create a list called "triples" that triples all the values of my_list
    triples = [x * 3 for x in my_list]
    print(triples)

    # create a list called "odd_negatives" that contains the negative
    # value of all the odd values of my_list
    odd_negatives = [-x for x in my_list if not x % 2 == 0]
    print(odd_negatives)

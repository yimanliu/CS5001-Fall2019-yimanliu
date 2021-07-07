if __name__ == '__main__':
    print("Branch Practice")
    num = int(input("Please type an integer: "))

    if num < 0:
        print("You typed a negative number, {}. I will make it "
              "positive.".format(num))
        print("abs({}) is {}".format(num, abs(num)))
        num = abs(num)
    else:
        print("You typed a positive number, {}.".format(num))

    double_num = int(input("Please type double {}: ".format(num)))

    if num * 2 == double_num:
        print("Yes, double {} is {}.".format(num, double_num))
    else:
        print("I'm sorry, but double {} is {}.".format(num, 2 * num))

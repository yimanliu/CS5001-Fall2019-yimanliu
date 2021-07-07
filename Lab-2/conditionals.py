# Author: Tiezhou Duan, Bernard Ekezie, Yiman Liu

import random

if __name__ == "__main__":
    # constants
    BEGIN = 0
    END = 5

    num1 = random.randint(BEGIN, END)
    print("This is a random number between {} and {}: {}".format(BEGIN,
                                                                 END, num1))
    num2 = random.randint(BEGIN, END)
    print("The second random number between {} and {} is {}.".format(BEGIN,
                                                                     END, num2))

    if num1 < num2:
        print("The largest number is {}.".format(num2))
    elif num1 > num2:
        print("The largest number is {}.".format(num1))
    else:
        print("The numbers are the same.")

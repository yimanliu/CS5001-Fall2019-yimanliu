import math

if __name__ == '__main__':
    print("Branch Practice")

num1 = int(input("Please type an integer: "))
num = num1
if num1 < 0:
    print("You typed a negative number, {}. I will make it positive.".format(
        num1))
    num1 = abs(num1)
    print("abs({}) is {}".format(num, abs(num1)))
elif num1 > 0:
    print("You typed a positive number, {}.".format(num1))


num2 = int(input("Please type double {}: ".format(num1)))
if num2 == num1 * 2:
    print("Yes, double {} is {}.".format(num1, num2))
elif num2 != num1 * 2:
    print("I'm sorry, but double {} is {}.".format(num1, num1 * 2))

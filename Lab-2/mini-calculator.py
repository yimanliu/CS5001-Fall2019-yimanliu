# Author: Tiezhou Duan, Bernard Ekezie, Yiman Liu

import math


def calculate(operation, num1, num2=0):
    """Performs the mathematical operation on num1 and num2.
       Returns the result of the operation.

       >>> calculate('+', 3, 4)
       7

       >>> calculate('-', 4, 2)
       2

       >>> calculate('*', 3, 4)
       12

       >>> calculate('/', 8, 4)
       2.0

       >>> calculate('sqrt', 25)
       5.0

       >>> calculate('reciprocal', 2)
       0.5
    """
    # your code here!
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    elif operation == "sqrt":
        return math.sqrt(num1)
    elif operation == "reciprocal":
        return 1 / num1
    else:
        return None


if __name__ == "__main__":
    operation = input("What would you like to do (choices: +, -, *, /, sqrt, "
                      "reciprocal)? ")
    if operation == 'sqrt' or operation == 'reciprocal':
        num1 = float(input("Number? "))
        result = calculate(operation, num1)
    else:
        num1 = float(input("First Number? "))
        num2 = float(input("Second number? "))
        result = calculate(operation, num1, num2)

    print("Result:")
    print("    {}".format(result))

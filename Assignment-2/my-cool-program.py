import math

"""conditionals, two functions, and two doctests for each
"""
USDTOEUR = 0.741
EURTOCAD = 1.366
CADTOUSD = 0.995


def transaction(ans, money):
    """
    If clients confirm their deals, we will call function arbitrage()
    If clients cancel their deals, we will end this transaction
    :param ans: YES or NO?
    :param money: the money clients want to deal with us
    :return:1 if clients want this deal; -1 if clients cancel this deal

    >>> transaction("YES", 1000)
    1
    >>> transaction("NO", 1000)
    Your transaction has been cancelled.
    -1
    """
    if ans == "YES":
        return 1
    elif ans == "NO":
        print("Your transaction has been cancelled.")
        return -1


def arbitrage(dollars):
    """
    buying currency in one place and selling them immediately in another place
    :param dollars:the amount of money clients want to deal with us
    :return:The amount of money clients have after the arbitrage

    >>> arbitrage(1000)
    Your money is now 741.0000 EUR
    Your money is now 1012.2060 CAD
    Your money is now 1007.1450 USD
    Wow, you made 7.1450 dollars!
    1007.1449700000002

    >>> arbitrage(30000000)
    Your money is now 22230000.0000 EUR
    Your money is now 30366180.0000 CAD
    Your money is now 30214349.1000 USD
    Wow, you made 214349.1000 dollars!
    30214349.100000005
    """
    EUR = dollars * USDTOEUR
    print("Your money is now {:0.4f} EUR".format(EUR))
    CAD = EUR * EURTOCAD
    print("Your money is now {:0.4f} CAD".format(CAD))
    USD = CAD * CADTOUSD
    print("Your money is now {:0.4f} USD".format(USD))
    if USD > dollars:
        print("Wow, you made {:0.4f} dollars!".format(USD - dollars))
    elif USD < dollars:
        print("Sorry, maybe you can try next time.")
    else:
        print("Don't give up, we still have chance!")
    return USD


if __name__ == "__main__":
    num1 = float(input("How much USD do you want to deal?"))
    print("Are you sure you want to deal {} USD with us?".format(num1))
    ans = input("Please confirm your transaction here: YES or NO? ")
    if transaction(ans, num1) > 0:
        arbitrage(num1)

# Change making program
def print_change(change_list):
    """
    Prints out the change in the form:
    d dollars, q quarters, m dimes, n nickels, p pennies
    :param change_list: A list in the form [dollars, quarters, dimes,
    nickels, pennies]
    :return: None
    doctests:

    >>> print_change([7, 2, 0, 1, 2])
    7 dollars, 2 quarters, 0 dimes, 1 nickel, 2 pennies
    >>> print_change([1, 1, 1, 1, 1])
    1 dollar, 1 quarter, 1 dime, 1 nickel, 1 penny
    >>> print_change([1, 1, 1, 1, 0])
    1 dollar, 1 quarter, 1 dime, 1 nickel, 0 pennies
    >>> print_change([0, 0, 0, 0, 0])
    0 dollars, 0 quarters, 0 dimes, 0 nickels, 0 pennies
    """
    change_names = ["dollar", "quarter", "dime", "nickel", "pennie"]
    count = 0
    for (a, b) in zip(change_list, change_names):
        if a == 1:
            if count == 4:
                print(f"{a} penny")
            else:
                print(f"{a} {b}, ", end='')
        else:
            if count == 4:
                print(f"{a} {b}s")
            else:
                print(f"{a} {b}s, ", end='')
        count += 1


def print_dollars_cents(change_list):
    """
    Combines and prints a list in the form [dollars, quarters, dimes, nickels,
    pennies] into a form: $XX.yy.
    :param change_list:
    :return: None
    doctests:

    >>> print_dollars_cents([7, 2, 0, 1, 2])
    $7.57
    >>> print_dollars_cents([6, 3, 7, 5, 8])
    $7.78
    """
    coin_values = [100, 25, 10, 5, 1]
    cents = 0
    for (a, b) in zip(change_list, coin_values):
        cents += a * b
    d, c = divmod(cents, 100)
    print(f"${d:01d}.{c:02d}")


def make_change(bill_amount_in_dollars, dollars_cost, cents_cost):
    """
    Calculates the change required for a bill in the amount of bill_amount,
    given that the item costs dollars_cost and cents_cost
    e.g., if bill_amount is 20, and the item has a dollars_cost of 12 and a
    cents_cost of 43, the change would be (in cents): 2000 - 1243 = 757 cents,
    which is 7 dollars and 57 cents. The return value would be [7, 2, 0, 1,
    2] for 7 dollars, 2 quarters, 0 dimes, 1 nickel, and 2 pennies.
    :param bill_amount_in_dollars: integer bill denomination in dollars
    :param dollars_cost: integer amount of dollars the item costs
    :param cents_cost: integer amount of cents the item costs
    :return: a list in the form of [dollars, quarters, dimes, nickels, pennies]
    doctests:

    >>> make_change(20, 12, 43)
    [7, 2, 0, 1, 2]
    >>> make_change(30, 21, 55)
    [8, 1, 1, 1, 4]
    """
    change_dol = bill_amount_in_dollars - dollars_cost - float(cents_cost / 100)
    dollar = int(change_dol / 1)
    quarter = int((change_dol - dollar) / 0.25)
    dime = int((change_dol - dollar - quarter * 0.25) / 0.10)
    nickel = int((change_dol - dollar - quarter * 0.25 - dime * 0.10) / 0.05)
    pennies = int((change_dol - dollar - quarter * 0.25 - dime * 0.10 -
                   nickel * 0.05) / 0.01)
    List = [dollar, quarter, dime, nickel, pennies]
    return List


if __name__ == "__main__":
    change = make_change(20, 12, 43)
    print_change(change)
    print_dollars_cents(change)
    change = make_change(50, 28, 14)
    print_change(change)
    print_dollars_cents(change)

# end starter code

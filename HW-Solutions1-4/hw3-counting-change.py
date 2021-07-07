# Change making program

def print_change(change_list):
    """
    Prints out the change in the form:
    d dollars, q quarters, m dimes, n nickels, p pennies
    :param change_list: A list in the form [dollars, quarters, dimes,
    nickels, pennies]
    :return: None

    >>> print_change([7, 2, 0, 1, 2])
    7 dollars, 2 quarters, 0 dimes, 1 nickel, 2 pennies

    >>> print_change([1, 1, 1, 1, 1])
    1 dollar, 1 quarter, 1 dime, 1 nickel, 1 penny
    """
    # special case for penny / pennies
    change_names = ["dollar", "quarter", "dime", "nickel"]
    for num_coins, change_name in zip(change_list, change_names):
        print(f"{num_coins} {change_name}", end='')
        if num_coins == 1:
                print(", ", end='')
        else:
                print("s, ", end='')
    if change_list[4] == 1: # pennies
        print("1 penny")
    else:
        print(f"{change_list[4]} pennies")



def print_dollars_cents(change_list):
    """
    Combines and prints a list in the form [dollars, quarters, dimes, nickels,
    pennies] into a form: $XX.yy.
    :param change_list:
    :return: None

    >>> print_dollars_cents([7, 2, 0, 1, 2])
    $7.57
    >>> print_dollars_cents([10, 10, 10, 10, 10])
    $14.10
    >>> print_dollars_cents([1, 0, 0, 0, 1])
    $1.01
    """
    coin_values = [100, 25, 10, 5, 1]
    total_cents = 0
    for num_coins, coin_value in zip(change_list, coin_values):
       total_cents += num_coins * coin_value
    dollars, cents = divmod(total_cents, 100)
    print(f"${dollars}.{cents:02d}")



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
    """
    total_change_cents = dollars_cost * 100 + cents_cost
    remaining_change_in_cents = (bill_amount_in_dollars * 100 -
                                 total_change_cents)
    coin_types = [100, 25, 10, 5, 1]
    coins_to_return = []
    for coin in coin_types:
        num_coins, remaining_change_in_cents  = divmod(
            remaining_change_in_cents, coin)
        coins_to_return.append(num_coins)
    return coins_to_return


if __name__ == "__main__":
    change = make_change(20, 12, 43)
    print_change(change)
    print_dollars_cents(change)

    change = make_change(50, 28, 14)
    print_change(change)
    print_dollars_cents(change)

def read_friends(filename):
    """
    Reads in a Dwarf Facebook list from filename. Returns a dict,
    with each dwarf as the keys, and a list of dwarfs as the value,
    representing the dwarf's friends.
    The file should be formatted as follows:

    dwarf_name1 friend1 friend2 friend3 ...
    dwarf_name2 friend1 friend2 friend3 ...
    ...

    The names will be space-separated.

    A particular Dwarf's dict key/value might look like this:
    dwarf_friends = {
        'Happy': ['Dopey', 'Bashful', 'Sneezy', 'Sleepy', 'Doc', 'Grumpy'],
    }

    :param filename: The file name of the file to read from
    :return: A dict of dwarf friends
    """
    database = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line[:-1]
                name = line.split()
                database[''.join(name[:1])] = name[1:]
        return database
    except FileNotFoundError:
        print(f"Could not open the database file, '{filename}'")
        return None


def print_friends(friend_database, dwarf):
    """
    Prints out the friends for a particular dwarf from friend_database. The list
    should print as follows, for example:
    Happy, your friends are:
    Dopey
    Bashful
    Sneezy
    Sleepy
    Doc
    Grumpy

    :param friend_database The database of friends
    :param dwarf: The dwarf whose friends will get printed
    :return: True if the dwarf is in the database, False otherwise
    """
    if dwarf in friend_database:
        print(f'{dwarf}, your friends are: ')
        for friend in friend_database[dwarf]:
            print(friend)
        return True
    else:
        return False


def add_friend(friend_database, dwarf, new_friend):
    """
    Adds new_friend to the dwarf's friend list, but only if the friend is not
    already a friend
    :param friend_database:
    :param dwarf: The dwarf who is adding a new friend
    :param new_friend: The new friend to add
    :return: True if the friend was added, False otherwise
    """
    friend_list = friend_database[dwarf]
    if new_friend in friend_list:
        print(f'{new_friend} is already in your friend list. No change made!')
        return False
    else:
        friend_database[dwarf].append(new_friend)
        return True


def unfriend(friend_database, dwarf, current_friend):
    """
    Unfriends current_friend from dwarf's friend list.
    :param friend_database: The database of friends
    :param dwarf: The dwarf whose friend will be unfriended
    :param current_friend: The friend of the dwarf who will be unfriended
    :return: True if the dwarf had the friend, False if the dwarf did not
    have the friend
    """
    friend_list = friend_database[dwarf]
    try:
        friend_list.remove(current_friend)
        return True
    except ValueError:
        print(f'{current_friend} is not your friend! No change made.')
        return False


def save_friends(friend_database, filename):
    """
    Saves friend_database to filename
    :param friend_database: The friend database
    :param filename: The file to save the database to
    :return: True if the database was saved, False otherwise
    """
    f = open(filename, "w")
    for dwarf, friends in friend_database.items():
        f.write(dwarf + ' ')
        f.write(' '.join(friends))
        f.write('\n')


def get_choice():
    print('Please choose an option below: ')
    print('     P: Print friend list')
    print('     A: Add a friend')
    print('     U: Unfriend someone')
    print('     Q: Quit')
    return input("Your selection? (P/A/U/Q): ")


def main():
    FILENAME = "dwarfs.txt"
    database = read_friends(FILENAME)
    if database is not None:
        while True:
            dwarf = ''
            print("Please login. Enter a blank line to quit.")
            print()
            while True:
                dwarf = input("login: ")
                if dwarf == '':
                    print("Goodbye!")
                    quit()
                if dwarf not in database:
                    print("Username unknown.")
                else:
                    break

            print(f"Hello, {dwarf}! Welcome to Facebook and the Seven Dwarfs")
            print()

            while True:
                option = get_choice()
                if option == 'p':
                    print_friends(database, dwarf)
                elif option == 'a':
                    new_friend = input("Who do you want to add as a friend? ")
                    add_friend(database, dwarf, new_friend)
                elif option == 'u':
                    current_friend = input("Who do you want unfriend? ")
                    unfriend(database, dwarf, current_friend)
                elif option == 'q':
                    break
                save_friends(database, FILENAME)


if __name__ == "__main__":
    main()

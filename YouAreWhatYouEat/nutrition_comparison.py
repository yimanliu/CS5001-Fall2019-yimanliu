import csv
import matplotlib.pyplot as plt
import numpy as np
plt.ion()


def parse_csv(filename, key_columns=1):
    """
    Creates a dictionary from a csv file. The dictionary's keys will be the
    values in the first key_columns of the file (in a tuple, unless there is
                                                                    only a single column, in which case it is just that column as the key),
    with the remaining values in each row as a list. Will attempt to convert
    values first to an int, then a float, then leave as a string
    :param filename: the filename with the csv
    :param key_columns: the number of columns to use as the key (in a tuple)
    :return: the dictionary
    """
    data = {}
    with open(filename) as f:
        filereader = csv.reader(f, delimiter=",", quotechar='"')
        header = next(filereader)
        for row in filereader:
            # attempt to convert each element to an int, then to a float,
            # otherwise, leave as string
            for idx, c in enumerate(row):
                try:
                    row[idx] = int(row[idx])
                except ValueError:
                    try:
                        row[idx] = float(row[idx])
                    except ValueError:
                        pass
            if key_columns == 1:
                data[row[0]] = row[1:]
            else:
                data[tuple(row[0:key_columns])] = row[key_columns:]
    return data


def read_database():
    """
    Reads in the files in the database, one at a time
    :return: the database
    """
    files = ['FOOD_DES', 'NUT_DATA', 'NUTR_DEF', 'WEIGHT']
    database = {}
    for file in files:
        if file == 'WEIGHT' or file == 'NUT_DATA':
            database[file] = parse_csv(file + '.csv', 2)
        else:
            database[file] = parse_csv(file + '.csv')
    return database


def autolabel(rects, ax):
    """Attach a text label above each bar in *rects*, displaying its height.
       Used by the bargraph function
    """
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


def bargraph(title, y_label, bar_labels, bar_data, bars_per_graph=5):
    """
    Produces bar graphs for nutrients and foods. If the number of nutrients
    (bar_labels) is greater than bars_per_graph, then there multiple graphs
    will be drawn.
    :param title: The title of the graph
    :param y_label: The label for the y-axis
    :param bar_labels: The list of nutrients
    :param bar_data: The food data dictionary, which is comprised of food
    descriptions as the keys, and lists of nutrients amounts as the values. The
    list of nutrients must have the same number of elements as bar_labels,
    and be in the same order.
    :param bars_per_graph: How many bars per graph will be shown.
    :return: None, though the user must click on a graph and then press a
    keyboard key to end the function.
    """
    print(f"Number of nutrients to compare: {len(bar_labels)}")
    for chart in range((len(bar_labels) - 1) // bars_per_graph + 1):
        first = chart * bars_per_graph
        last = (chart + 1) * bars_per_graph
        if last > len(bar_labels):
            last = len(bar_labels)

        print(f"Displaying nutrients {first} - {last - 1}")

        x = np.arange(len(range(first, last)))  # the label locations
        width = 0.7 / len(bar_data)  # the width of the bars

        fig, ax = plt.subplots()
        all_rects = []
        left_x = (len(bar_data) * width / 2) - width / 2
        for bar_offset, bd_key in enumerate(bar_data):
            bd_val = bar_data[bd_key][first:last]
            all_rects.append(ax.bar(x - left_x + bar_offset * width,
                                    bd_val, width,
                                    label=bd_key))

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel(y_label)
        ax.set_title(title)
        ax.set_xticks(x)
        ax.set_xticklabels(bar_labels[first:last], rotation='vertical')
        ax.legend()

        for rect in all_rects:
            autolabel(rect, ax)

        fig.tight_layout()

        # plt.show()
        plt.draw()
        plt.pause(0.001)
    keyboard_click = False
    while not keyboard_click:
        keyboard_click = plt.waitforbuttonpress()


def get_weight(database, ndb_no):
    """
    Allows the user to choose what amount of a food item to use for the
    comparison. For example, if a user has selected "Apples, raw, granny
    smith, with skin", then the choices will be:
     1: 1 cup, sliced
     2: 1 large
     3: 1 medium
     4: 1 small
    and the user should choose one.
    :param database: the food database
    :param ndb_no: the database ndb number for the food
    :return: the entry in the weight database that the user chose. This will
    be a list with the amount, the description, and the gram weight of the
    selection, e.g., [1, "cup, sliced", 151]
    """
    print("Please choose an amount:")
    seq = 1
    while True:
        try:
            w_details = database['WEIGHT'][(ndb_no, seq)]
            print(f"\t {seq}: {w_details[0]} {w_details[1]}")
            seq += 1
        except KeyError:
            break
    choice = int(input("Your choice: "))
    return database['WEIGHT'][(ndb_no, choice)]


def get_nutrients(database, ndb_no):
    """
    Gets the nutrients for a food from the database
    :param database: the database
    :param ndb_no: the ndb number for the food
    :return: a list of the nutrients in the food
    """
    nutrients = []
    for nutr_no in range(1000):
        try:
            nutr_val = database['NUT_DATA'][(ndb_no, nutr_no)][0]
            if nutr_val == 0:
                continue  # don't bother listing nutrients where the
                # expected amount is 0
            # get nutrient info
            units = database['NUTR_DEF'][nutr_no][0]
            nutr_desc = database['NUTR_DEF'][nutr_no][1]
            # print(f"{nutr_val}{units} of {nutr_desc}")
            nutrients.append([nutr_val, units, nutr_desc])
        except KeyError:
            pass
    return nutrients


def search_for_food(database):
    """
    Queries the user for food items, one at a time. Lists the items from the
    database that match a query, and then lets the user choose one of the foods.
    Repeats the process until the user types "!" to indicate that they have
    finished selecting foods.
    :param database: the database
    :return: a list of the foods selected by the user.
    """
    foods = []
    while True:
        search_term = input("What food would you like to search for? "
                            "(<return> for all, ! to finish):")
        if search_term == '!':
            break
        matches = []
        for key, val in database['FOOD_DES'].items():
            if search_term in val[1].lower():
                matches.append((key, val))
        print("The following foods match:")
        for idx, key_val in enumerate(matches):
            print(f"\t{idx + 1}: {key_val[1][1]}")  # long description
        choice = input("Which food would you like to add? (<enter> for none): ")
        if choice == '':
            print()
            continue
        full_choice = matches[int(choice) - 1]
        ndb_no, details = full_choice
        food_details = {
            'ndb_no': ndb_no,
            'details': details,
            'weight': get_weight(database, ndb_no),
            'nutrients': get_nutrients(database, ndb_no)
        }
        print(f"Added: {food_details['details'][1]}")
        weight = food_details['weight']
        print(f"       {weight[0]} {weight[1]}")
        print(f"       with {len(food_details['nutrients'])} nutrients")
        foods.append(food_details)
    return foods


def graph_nutrients(foods, nutrient_list):
    """
    Sets up the necessary food dictionary in order to be able to graph
    the nutrient comparisons. First, creates a dict with all the foods as
    keys and empty lists as values. Second, traverses the list of nutrients
    and appends the value for that nutrient for each food. If a food doesn't
    have a particular nutrient, append 0 for the value. Finally,
    calls bargraph to create the graphs.
    :param foods: a list of food dictionaries
    :param nutrient_list: a list of nutrients
    :return: None
    """
    # We need a dictionary of foods,
    # with each food having its own list of nutrients
    food_graph_dict = {}
    for food in foods:
        food_graph_dict[food['details'][1]] = []

    # now, we need to walk through all the nutrients, and add the amount to
    # each food in the food_graph_dict
    for nutrient in nutrient_list:
        for food in foods:
            found_nutrient = False
            for individual_nutrient in food['nutrients']:
                if individual_nutrient[2] == nutrient:
                    food_graph_dict[food['details'][1]].append(
                        individual_nutrient[0])
                    found_nutrient = True
                    break
            if not found_nutrient:
                food_graph_dict[food['details'][1]].append(0)
    bargraph('Nutrient Comparison', 'value', nutrient_list, food_graph_dict)


def choose_nutrients(foods):
    """
    Creates a set of all nutrients for all foods in the foods list. Then,
    prints out the list of nutrients to compare, and then asks the user to
    type in a comma-separated list of the nutrient indexes. Populates a new
    list of the nutrients to compare and returns it.
    :param foods: the list of foods
    :return: the list of nutrients to compare
    """
    # create a set of nutrients
    nutrients_set = set()
    for food in foods:
        for individual_nutrient in food['nutrients']:
            nutrients_set.add(individual_nutrient[2])
    nutrients_list = list(nutrients_set)
    print("These are the nutrients in the foods to compare:")
    for idx, nutrient in enumerate(nutrients_list):
        print(f"{idx + 1}: {nutrient}")
    chosen_indices = input("Please provide a comma-separated list of the "
                           "nutrients you would like (e.g., 1, 22, 28, "
                           "30): ").split(',')
    chosen_indices = [int(x) for x in chosen_indices]
    chosen_nutrients = [nutrients_list[x - 1] for x in chosen_indices]
    print(chosen_nutrients)
    return chosen_nutrients


def main():
    """
    Calls functions to (1) read in the database, (2) search for the foods
    the user wants to compare, (3) lets the user choose which nutrients to
    compare, and (4) graphs the food / nutrient comparisons.
    :return: None
    """
    database = read_database()
    foods = search_for_food(database)
    nutrients = choose_nutrients(foods)
    graph_nutrients(foods, nutrients)


if __name__ == "__main__":
    main()

# practice final questions
# Answer the following questions or fill in the required code
import math


# Question 1: What does the following function print out?
def mystery1():
    word = "xyz123!@#"
    for i in range(len(word) - 1, -2, -1):
        print(i, word[i], end='')
        if word[i].isdigit():
            for j in range(int(word[i])):
                print("*", end='')
        print()


# 8 #
# 7 @
# 6 !
# 5 3 ***
# 4 2 **
# 3 1 *
# 2 Z
# 1 Y
# 0 X
# -1 #


# Question 2: When mystery2b() is called below, what prints out?
def mystery2a(a):
    if a.isdigit():
        print(a)


def mystery2b():
    data1 = "5,10,15"
    for item in data1:
        mystery2a(item)
    print("----")
    data2 = data1.split(",")
    for item in data2:
        mystery2a(item)


"""
5
1
0
1
5
----
5
10
15
"""


# Question 3: When mystery3() is called below, what prints out?
def mystery3():
    code = {6: ["t", "g"], 14: ["p", "q"], 15: ["c", "d"], 9: ["o", "a"]}
    data = "5,0:3,1:2,0"
    splitdata = data.split(":")
    for item in splitdata:
        splititem = item.split(",")
        print(code[int(splititem[0]) * 3][int(splititem[1])], end="")
    print()


"""
cat
"""

# Question 4:
"""
Write a FUNCTION called “valid_n_number” that determines if a NEU Student ID is valid. For the purpose of this 
question a valid NEU Student ID is defined as follows:
    • exactly 9 characters long
    • begins with the uppercase character ‘N’
    • all characters beside the beginning ‘N’ character must be numbers
Your function should accept a test “N number” as an ARGUMENT (String) and RETURN a status value (Boolean). 
There are five doctests in the function that should pass.
"""


def valid_n_number(neu_id):
    """
    Determines if neu_id is a valid NEU ID.
    :param neu_id: a string
    :return: True if the ID is valid, False if the ID is not valid
    >>> valid_n_number("N123")
    False

    >>> valid_n_number("N1234567890")
    False

    >>> valid_n_number("P12345678")
    False

    >>> valid_n_number("NXYZ!5678")
    False

    >>> valid_n_number("N12345678")
    True
    """
    # TODO: Your code here
    if len(neu_id) == 9:
        if neu_id[0] == 'N':
            for i in range(1, 9):
                if not neu_id[i].isdigit():
                    return False
            return True
        else:
            return False
    else:
        return False


# Question 5
"""
Write a program that asks the user to enter in 5 NEU Student ID numbers. Ensure that the ID numbers that the 
user enters are valid (use your function from question 4) and that they do not enter duplicate IDs. 
Let the user know if they make a mistake. When you have collected 5 IDs print them out in ascending order (you should
use the list's sort function). 

Here’s a sample running of this program:
Enter a N Number: N12345678
Enter a N Number: N123
Invalid N Number
Enter a N Number: P12345678 
Invalid N Number
Enter a N Number: N12345678 
Duplicate N Number
Enter a N Number: N00000003
Enter a N Number: N00000001
Enter a N Number: N00000002
Enter a N Number: N00000000

Your N-Numbers:

N00000000 
N00000001 
N00000002 
N00000003 
N12345678
"""


def get_five_ids():
    """
    Asks the user for 5 id numbers, and tells the user when they make a mistake. After 5 legitimate NEU Ids
    have been entered, print them in ascending order.
    :return: None
    """
    # TODO: Your code here
    id_set = set()
    while True:
        user_id = input("Enter a N Number: ")
        if valid_n_number(user_id):
            if user_id in id_set:
                print("Duplicate N Number")
            else:
                id_set.add(user_id)
        else:
            print("Invalid N Number")
        if len(id_set) == 5:
            break
    print()
    lst = list(id_set)
    lst.sort()
    print("Your N-Numbers:")
    print()
    for i in range(len(lst)):
        print(lst[i])


# Question 6
"""
Given the data file below (datafile.txt) with four lines of text, what will be stored in datafile2.txt after 
mystery4("datafile.txt") has been run? datafile.txt:
snow
snowflake
sled
sledding
"""


def mystery4(filename):
    with open(filename, "r") as f:
        data = f.read()

    x = data.split("\n")
    new_file = filename.split(".")[0] + '2' + filename.split(".")[1]
    with open(new_file, "w") as newf:
        for i in x:
            if len(i) % 2 == 0:
                newf.write(i + "!\n")
            else:
                newf.write(i + "?\n")


"""
snow!
snowflake?
sled!
sledding！
"""

# Question 7
"""
The Shape class, shown below defines a shape, such as a rectangle, circle, 
octagon, etc. All shapes have four attributes: x (the x-coordinate of the 
bottom left corner of the shape), y (the y-coordinate of the bottom left 
corner of the shape), width, and height. All of the properties have a default
float value of 0.0.

Shapes have a __str__ function that describes a shape in the following way:
[x,y,width,height]

Shapes have an __eq__ function that compares all four attributes and 
returns true if they are the same, *and* if they are of the same class type. 
To determine if an object is a type of a particular class, you can use the 
isinstance function, like this:

isinstance(some_object, Rectangle)

Shapes have a calculate_area method that returns the area.

Fill in the details for the two classes below -- Rectangle, and Circle.

Hints: 1) a Rectangle is created with the same arguments as a default Shape, 
so it's __init__ function simply needs to call super() with its parameters.
       2) a Circle only has three parameters: x, y, and radius. The width and
height of a Circle are both twice the radius.
       3) the area of a rectangle is the width times the height
       4) the area of a circle is pi * r * r. You should use the math 
       module's PI constant to represent pi. 
"""


class Shape:
    def __init__(self, x, y, width, height):
        # TODO Your code here
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        """
        Form: [x,y,width,height]
        :return: a string in the above form
        """
        # TODO Your code here
        return f'[{self.x},{self.y},{self.width},{self.height}]'


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        # TODO Your code here
        super().__init__(x, y, width, height)

    def __eq__(self, other):
        # TODO Your code here
        return (self.x == other.x and
                self.y == other.y and
                self.width == other.width and
                self.height == other.height and
                isinstance(other, Rectangle))

    def calculate_area(self):
        # TODO Your code here
        return self.width * self.height


class Circle(Shape):
    def __init__(self, x, y, radius):
        # TODO Your code here
        super().__init__(x, y, radius * 2, radius * 2)

    def __eq__(self, other):
        # TODO Your code here
        return (self.x == other.x and
                self.y == other.y and
                self.width == other.width and
                self.height == other.height and
                isinstance(other, Circle))

    def calculate_area(self):
        # TODO Your code here
        return math.pi * self.width / 2 * self.width / 2


# Question 8
"""
A stack can be used to determine if a sentence or a line of code has "matched 
parentheses", meaning that for every open parenthesis, "(", there is a 
corresponding close parenthesis, ")". The way it works is that a string is 
read in character by character and any time a left paren is seen, 
it is pushed onto the stack. When a right paren is seen, it is popped off the
stack. If, at the end of the sentence the following conditions are true, 
then there are matched parentheses:
1. The stack was never popped when empty
2. The stack is currently empty

Given the following stack class, write a function, "matched_parens(s)" that 
returns True if there are matched parentheses, and False if there are not 
matched parentheses.
"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def empty(self):
        return len(self.stack) == 0


def matched_parens(s):
    """
    Determines if a string, s, has matched parentheses
    :param s: a string
    :return: True if the string has matched parentheses, False if it does not

    >>> matched_parens("(this is okay)")
    True

    >>> matched_parents("(not okay")
    False

    >>> matched_parens("((not okay)")
    False

    >>> matched_parens("okay (((yup).).)")
    True
    """
    # TODO: Your code here
    stack = Stack()
    for c in s:
        if c == '(':
            stack.push('(')
        elif c == ')':
            if stack.empty():
                return False
            else:
                stack.pop()
    return stack.empty()


# Question 9
"""
The Queue data structure is similar to a stack, except that it is a 
"first-in-first-out" abstraction. In other words, the first element enqueued
on a queue is the first element dequeued, and so-forth.

Using a list as the underlying container, complete the code for the Queue 
class below:
"""


class Queue:
    def __init__(self):
        # TODO Your code here
        self.queue = []

    def enqueue(self, value):
        """
        Places value into the back of the queue
        :param value: a value
        :return: None
        """
        # TODO Your code here
        self.queue.append(value)

    def dequeue(self):
        """
        Removes and returns the value at the front of the queue, or None if
        the queue is empty
        :return: The value at the front of the queue, or None if the queue is
        empty
        """
        # TODO Your code here
        if len(self.queue) == 0:
            return None
        else:
            return self.queue.pop(0)

    def front(self):
        """
        Returns but does not remove the front element of the queue. If the
        queue is empty, returns None. The queue is unchanged after this
        method is called
        :return: The front element in the queue, or None if the queue is empty
        """
        # TODO Your code here
        if len(self.queue) == 0:
            return None
        else:
            return self.queue[0]

    def empty(self):
        """
        Returns True if the queue is empty, False otherwise
        :return: True if the queue is empty, False if it has elements
        """
        # TODO Your code here
        return len(self.queue) == 0


# Question 10
"""
Describe in 100 words or less how quicksort works.
"""

"""
1. pick a random pivot, and use this pivot partitions this list
Partition: element less than pivot will be placed on pivot's left side
and element greater than pivot will be placed on pivot's right side
After partitioning, all the elements on the left side are less than this pivot, 
and all the elements on the right side are greater than this pivot. 
This pivot is in correct place!
2. recursively partition the remaining left part and right part
until the left part and right part only have one element left, which is sorted!
"""

# Question 11
"""
Write the insertion_sort(lst) function below, which uses an 
insertion sort to sort a list from lowest to highest value.
"""


def insertion_sort(lst):
    """
    Sorts a list in-place using the insertion sort algorithm.
    :param lst: a list
    :return: None (the list is sorted in-place)
    """
    for i in range(1, len(lst)):
        for j in range(i, 0, -1):
            if lst[j] < lst[j - 1]:
                swap(lst, j, j - 1)
            else:
                break


def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


# Question 12
"""
The following binary_search(lst, value) function uses a binary search to 
locate a value in a list. Based on the code, answer the following questions:
1. What must be true of lst for the function to correctly find a value?
2. After the third time through the while loop in the function, what will the 
value of "low" be for the following function call?
    binary_search([1, 4, 18, 23, 56, 80, 90, 91, 95, 100], 23) 
"""


def binary_search(lst, value):
    low = 0  # the low index
    high = len(lst) - 1  # the high index
    while low <= high:
        mid = (low + high) // 2  # the middle value
        if lst[mid] < value:
            low = mid + 1
        elif lst[mid] > value:
            high = mid - 1
        else:  # found!
            return mid
    return -1


"""
1. The list has to be sorted
2. low = 2
"""


def main():
    # uncomment the lines below to check your answers
    print(f"Question 1:")
    mystery1()
    print()
    #
    print(f"Question 2:")
    mystery2b()
    #
    print(f"Question 3:")
    mystery3()
    print()
    #
    print(f"Question 4:")
    test1 = valid_n_number("N123")
    test2 = valid_n_number("N1234567890")
    test3 = valid_n_number("P12345678")
    test4 = valid_n_number("NXYZ!5678")
    test5 = valid_n_number("N12345678")
    print(test1, test2, test3, test4, test5)
    print()
    #
    # get_five_ids()
    # print()
    #
    mystery4("datafile.txt")
    print()
    r1 = Rectangle(5, 10, 20, 30)
    r2 = Rectangle(0, 0, 4, 3)
    r3 = Rectangle(5, 10, 20, 30)
    c1 = Circle(0, 0, 10)
    c2 = Circle(1, 1, 10)
    print(r1, r2, r3, c1, c2)
    # [5, 10, 20, 30][0, 0, 4, 3][5, 10, 20, 30][0, 0, 20, 20][1, 1, 20, 20]
    print(r1.calculate_area())  # 600
    print(c1.calculate_area())  # 314.1592653589793
    print(r1 == r2)  # False
    print(r1 == r3)  # True
    print(c1 == c2)  # False
    print(c2 == c2)  # True
    print()
    #
    print(matched_parens("(this is okay)"))
    print(matched_parens("(not okay"))
    print(matched_parens("((not okay)"))
    print(matched_parens("okay (((yup).).)"))
    print()
    #
    queue = Queue()
    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')
    queue.enqueue('d')
    queue.enqueue('e')
    print(queue.front())
    while not queue.empty():
        print(queue.dequeue())

    lst = [8, 4, 3, 1, 2, 7, 5]
    insertion_sort(lst)
    print(lst)


if __name__ == "__main__":
    main()

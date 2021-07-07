import programB


def whoami():
    return "I'm programC!"

def count_up(count):
 if count < 0:
    return
 count_up(count - 1)
 print(count)

if __name__ == "__main__":
    b = programB.whoami()
    c = whoami()
    print("b == {}".format(b))
    print("c == {}".format(c))
    print(2 / 2)

fib = [0, 1, 1, 2, 3, 5, 8, 13, 21]
print(fib[:-1])

str = 'what'
temp = list(str)
temp[0] = 'h'
str = ''.join(temp)
print(str)

phonebook = {'Chris': '685-6587', 'Jenny': '867-5309', 'John': '867-5309',
             'Becky': '434-2221'}

lst = list(phonebook.keys())
print(lst)

count_up(6)

with open("test.txt", "r") as f:
    lines = f.readline()

lines = lines[::-1]
with open("test.txt", "w") as f:
    for line in lines:
        f.write(line)
import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

ans1 = ((-b) + math.sqrt((pow(b, 2) - 4 * a * c))) / (2 * a)
ans2 = ((-b) - math.sqrt((pow(b, 2) - 4 * a * c))) / (2 * a)

print("solution 1: {}".format(ans1))
print("solution 1: {}".format(ans2))

num = int(input("number: "))

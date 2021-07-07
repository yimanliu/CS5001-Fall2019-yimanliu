# part 1
animal = input("What is your favorite animal? ")
num_animals = int(input("How many {}s would you like? ".format(animal)))
print("I like {}s, too! But, {} is a lot of {}s! Maybe you should just "
      "have {:.0f}!".format(animal, num_animals, animal, num_animals / 2))
# part 2
print()
flower = "Daisy"
car = "Volkswagen"
planet = "Earth"
Language = "Python"
pi = 3.1415926535
radius_of_planet_in_km = 6371
tablespoons_per_cup = 16
print("My name is {1} and I drive a {0} with a {1} painted "
      "on it.".format(car, flower))
print("The circumference of {} is {:.2f} "
      "kilometers.".format(planet, pi * 2 * radius_of_planet_in_km))
a1 = 10
b1 = float(a1 / tablespoons_per_cup)
a2 = 100
b2 = float(a2 / tablespoons_per_cup)
a3 = 1000
b3 = float(a3 / tablespoons_per_cup)
print("tablespoons    :    cups")
print("%11.0f    :%8.2f" % (a1, b1))
print("%11.0f    :%8.2f" % (a2, b2))
print("%11.0f    :%8.2f" % (a3, b3))
print("In {}, I know how to put two curly braces next to each other, "
      "like this {{}}.".format(Language))

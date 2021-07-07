animal = input("What is your favorite animal? ")
num_animals = int(input("How many {}s would you like? ".format(animal)))
print("I like {}s, too! But, {} is a lot of {}s! Maybe you should just have {:.0f}!".format(animal, num_animals, animal, num_animals / 2))

print()
flower = "Daisy"
car = "Volkswagen"
planet = "Earth"
language = "Python"
pi = 3.1415926535
radius_of_planet_in_km = 6371
tablespoons_per_cup = 16

# flower = "Marigold"
# car = "Ford"
# planet = "Jupiter"
# language = "Java"
# pi = 3.14
# radius_of_planet_in_km = 69911
# tablespoons_per_cup = 12

print("My name is {0} and I drive a {1} with a {0} painted on it.".format(flower, car))
print("The circumference of {} is {:.2f} kilometers.".format(planet, 2 * pi * radius_of_planet_in_km))
print("{:>11} : {:>5}".format("tablespoons", "cups"))
print("{:>11d} : {:5.2f}".format(10, 10 / tablespoons_per_cup ))
print("{:>11d} : {:5.2f}".format(100, 100 / tablespoons_per_cup))
print("{:>11d} : {:5.2f}".format(1000, 1000 / tablespoons_per_cup))
print("In {}, I know how to put two curly braces next to each other, like this {{}}.".format(language))

a = 5
b = 3
print(divmod(a, b))
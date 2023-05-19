# ------10.1------

kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McMoy", "Chief Medical Offcer", 2266]

class Dog:
    
    # Class attribute
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        self.name = name
        self.age= age

# ------10.2------

class Dog:
    pass

Dog()  # <__main__.Dog object at 0x0000023D2FF10640>
Dog()  # <__main__.Dog object at 0x0000023D2FF71930>
a = Dog()
b = Dog()
a == b  # False
class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

        
# Dog()  # TypeError
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

buddy.name  # 'Buddy'
buddy.age  # 9
miles.name  # 'Miles'
miles.age  # 4
buddy.species  # 'Canis familiaris'

buddy.age = 10
buddy.age  # 10
miles.species  #  'Canis familiaris'
miles.species = "Felis silvestris"
miles.species  # 'Felis silvestris'

class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles", 4)
miles.description()  # 'Miles is 4 years old'
miles.speak("Woof Woof")  # 'Miles says Woof Woof'
miles.speak("Bow Wow")  # 'Miles says Bow Wow'

print(miles)  # <__main__.Dog object at 0x000001FB95992350>


class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
##    # Instance method
##    def description(self):
##        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles", 4)
print(miles)  # Miles is 4 years old


######
#1.
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

philo = Dog("Philo", 5, "brown")
print(f"{philo.name}'s coat is {philo.coat_color}.")

#2.

class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    #3.
    def drive(self, number):
        self.mileage = self.mileage + number
        

blue = Car("blue", 20_000)
red = Car("red", 30_000)

for car in (blue, red):
    print(f"The {car.color} car has {car.mileage:,} miles")

green_car = Car("green", 0)
green_car.drive(100)
print(green_car.mileage)

######

# ------10.3------

##class Dog:
##    species = "Canis familiaris"
##    def __init__(self, name, age, bread):
##        self.name = name
##        self.age = age
##        self.bread = bread
##
##    def __str__(self):
##        return f"{self.name} is {self.age} years old"
##
##    def speak(self, sound):
##        return f"{self.name} says {sound}"
##
##miles = Dog("Miles", 4, "Jack Russell Terrier")
##buddy = Dog("Buddy", 9, "Dachshund")
##jack = Dog("Jack", 3, "Bulldog")
##jim = Dog("Jim", 5, "Bulldog")
##
##buddy.speak("Yap")
##jim.speak("Woof")
##jack.speak("Woof")


class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks: {sound}"


class JackRusselTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRusselTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

miles.species  # 'Canis familiaris'
buddy.name  # 'Buddy'
print(jack)  # Jack is 3 years old
jim.speak("Woof")  # 'Jim says Woof'
type(miles)  # <class '__main__.JackRusselTerrier'>
isinstance(miles, Dog)  # True
isinstance(miles, Bulldog)  # False
isinstance(jack, Dachshund)  # False

class JackRusselTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"
#        return super().speak(sound)

jim = Bulldog("Jim", 5)
jim.speak("Woof")  # 'Jim barks: Woof'

miles = JackRusselTerrier("Miles", 4)
miles.speak()  # 'Miles says Arf'
without_super = miles.speak("Grr")  # 'Miles says Grr'

class JackRusselTerrier(Dog):
    def speak(self, sound="Arf"):
#        return f"{self.name} says {sound}"
        return super().speak(sound)

miles = JackRusselTerrier("Miles", 4)
with_super = miles.speak()  # 'Miles says Arf'
print(without_super)
print(with_super)

######
#1.
class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)
#2.

class Rectangle():

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Rectangle):

    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        
test_square = Square(4)

######


# ------10.4------
#Farma
#1 rodzic
#3 dzieci
#walking, running, eating , slleping

class Animal:
    

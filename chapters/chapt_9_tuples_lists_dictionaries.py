# ------9.1------

my_first_tuple = (1, 2, 3)
my_first_tuple #  (1, 2, 3)
type(my_first_tuple) #  <class 'tuple'>

empty_tuple = () #  
type(empty_tuple) #  <class 'tuple'>

x = (1)
type(x) #  <class 'int'>

x = (1,)
type(x) #  <class 'tuple'>

tuple("Python") #  ('P', 'y', 't', 'h', 'o', 'n')

#tuple(1, 2, 3) #   TypeError
#tuple(1) #  TypeError
tuple() #  ()

numbers = (1, 2, 3)
 
len(numbers) #  3
name = "David" 
name[1] #  'a'
values = (1, 3, 5, 7, 9)
values[2] #  5

name[2:4] #  'vi'

values[2:4] #  (5, 7)

# values[0] = 2 #  TypeError
# see: https://realpython.com/courses/immutability-python/

vowels = tuple("aeiou")
for vowel in vowels:
    print(vowel.upper())

coordinates = 4.21, 9.29
type(coordinates) #  <class 'tuple'>

x, y = coordinates
x #  4.21
y #  9.29

name, age, occupation = "David", 34, "programmer"
name #  'David'
age #  34
occupation #  'programmer'
# a, b, c, d = 1, 2, 3 #  ValueError
# a, b, c = 1, 2, 3, 4 #  ValueError

vowels #  ('a', 'e', 'i', 'o', 'u')
"o" in vowels #  True
"x" in vowels #  False

def adder_subtractior(num1, num2):
    return (num1 + num2, num1 - num2)

adder_subtractior(3, 2) #  (5, 1)

######
#1.
cardinal_numbers = ("first", "second", "third")

#2.
cardinal_numbers[1] # 'second'

#3.
position1, position2, position3 = cardinal_numbers
position1
'first'
position2
'second'
position3
'third'

#4.
my_name = tuple("Paulina")

#5.
"x" in my_name #  False

#6.
my_name[1:] #  ('a', 'u', 'l', 'i', 'n', 'a')
######

# ------9.2------


colors = ["red", "yellow", "green", "blue"]
colors #  ['red', 'yellow', 'green', 'blue']
type(colors) #  <class 'list'>
colors #  ['red', 'yellow', 'green', 'blue']

list((1, 2, 3)) #  [1, 2, 3]
list("Python") #  ['P', 'y', 't', 'h', 'o', 'n']

groceries = "eggs, milk, cheese"
grocery_list = groceries.split(", ")
grocery_list #  ['eggs', 'milk', 'cheese']

"a;b;c".split(";") #  ['a', 'b', 'c']
"The quick brown fox".split(" ") #  ['The', 'quick', 'brown', 'fox']
"abbaabba".split("ba") #  ['ab', 'ab', '']
"abbaabba".split("c") #  ['abbaabba']


numbers = [1, 2, 3, 4]
numbers[1] #  2
numbers[1:3] #  [2, 3]

"Bob" in numbers #  False

for number in numbers:
    if number % 2 == 0:
        print(number)
        
#2
#4
        
colors #  ['red', 'yellow', 'green', 'blue']
colors[0] = "burgundy"
colors #  ['burgundy', 'yellow', 'green', 'blue']

colors = ["red", "yellow", "green", "blue"]
colors[1:3] = ["orange", "megenta", "aqua"]
colors #  ['red', 'orange', 'megenta', 'aqua', 'blue']

colors #  ['red', 'orange', 'megenta', 'aqua', 'blue']
colors[1:4] = ["yellow", "green"]
colors #  ['red', 'yellow', 'green', 'blue']

#list.insert()
colors #  ['red', 'yellow', 'green', 'blue']
colors.insert(1, "orange")
colors #  ['red', 'orange', 'yellow', 'green', 'blue']

colors.insert(10, "violet")
colors #  ['red', 'orange', 'yellow', 'green', 'blue', 'violet']

colors #  ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
colors.insert(-1, "indigo")
colors #  ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

#list.pop()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
color = colors.pop(3)
color #  'green'
colors #  ['red', 'orange', 'yellow', 'blue', 'indigo', 'violet']

#colors.pop(10) #  IndexError: 
colors.pop(-1) #  'violet'
colors #  ['red', 'orange', 'yellow', 'blue', 'indigo']
colors.pop() #  'indigo'
colors #  ['red', 'orange', 'yellow', 'blue']

#list.append()
colors.append("indygo")
colors # ['red', 'orange', 'yellow', 'blue', 'indygo']

colors.pop() #  'indygo'
colors # ['red', 'orange', 'yellow', 'blue']

colors.insert(len(colors), "indygo")
colors #  ['red', 'orange', 'yellow', 'blue', 'indygo']

colors #  ['red', 'orange', 'yellow', 'blue', 'indygo']
colors.extend(["violet", "ultraviolet"])
colors #  ['red', 'orange', 'yellow', 'blue', 'indygo', 'violet', 'ultraviolet']

colors.pop() #  'ultraviolet'
colors.pop() #  'violet'
colors #  ['red', 'orange', 'yellow', 'blue', 'indygo']
colors.extend(("violet", "ultraviolet"))
colors #  ['red', 'orange', 'yellow', 'blue', 'indygo', 'violet', 'ultraviolet']

nums =[1, 2, 3, 4, 5]
total = 0
for number in nums:
    total = total + number
    
total #  15
sum([1, 2, 3, 4 ,5]) #  15
#sum([1, 2, 3, "four" ,5]) #  TypeError
min([1, 2, 3, 4 ,5]) #  1
max([1, 2, 3, 4 ,5]) #  5


numbers = (1, 2, 3, 4, 5)
squares = [num**2 for num in numbers]
squares #  [1, 4, 9, 16, 25]

squares = []
for num in numbers:
    squares.append(num**2)

squares #  [1, 4, 9, 16, 25]

str_numbers = ["1.5", "2.3", "5.25"]
float_numbers = [float(value) for value in str_numbers]
float_numbers #  [1.5, 2.3, 5.25]

######
#1.
food = ["rice", "beans"]
#2.
food.append("broccoli")
food #  ['rice', 'beans', 'broccoli']
#3.
food.extend(["bread", "pizza"])
food #  ['rice', 'beans', 'broccoli', 'bread', 'pizza']
#4.
print(food[:2]) #  ['rice', 'beans']
#5.
print(food[len(food)-1]) #  pizza
print(food[-1]) #  pizza
#6.
breakfast = "eggs, fruit, orange    juice".split(", ")
#7.
len(breakfast) == 3
#8.
lengths = [len(eat) for eat in breakfast]
######

# ------9.3------


two_by_two = [[1, 2], [3, 4]]
len(two_by_two) #  2
two_by_two[0] #  [1, 2]
two_by_two[1] #  [3, 4]
two_by_two[1][0] #  3


animals = ["lion", "tiger", "frumious Brandersnatch"]
large_cats = animals
large_cats #  ['lion', 'tiger', 'frumious Brandersnatch']
large_cats.append("Tigger")
large_cats #  ['lion', 'tiger', 'frumious Brandersnatch', 'Tigger']
animals #  ['lion', 'tiger', 'frumious Brandersnatch', 'Tigger']

animals = ["lion", "tiger", "frumious Brandersnatch"]
large_cats = animals[:]
large_cats #  ['lion', 'tiger', 'frumious Brandersnatch']
large_cats.append("leopard")
large_cats #  ['lion', 'tiger', 'frumious Brandersnatch', 'leopard']
animals #  ['lion', 'tiger', 'frumious Brandersnatch']

#shallow copy
matrix1 = [[1, 2], [3, 4]]
matrix2 = matrix1[:]
matrix2[0] = [5, 6]
matrix2 #  [[5, 6], [3, 4]]
matrix1 #  [[1, 2], [3, 4]]

matrix2[1][0] = 1
matrix2 #  [[5, 6], [1, 4]]
matrix1 #  [[1, 2], [1, 4]]

#deep copy
matrix1 #  [[1, 2], [1, 4]]
import copy
matrix3 = copy.deepcopy(matrix1)
matrix3[1][0] = 3
matrix3 #  [[1, 2], [3, 4]]
matrix1 #  [[1, 2], [1, 4]]


colors = ["red", "yellow", "green", "blue"]
colors.sort()
colors #  ['blue', 'green', 'red', 'yellow']
numbers = [1, 10, 5, 3]
numbers.sort()
numbers #  [1, 3, 5, 10]

colors = ["red", "yellow", "green", "blue"]
colors.sort(key=len)
colors #  ['red', 'blue', 'green', 'yellow']

def get_second_element(item):
    return item[1]

items = [(4, 1), (1, 2), (-9, 0)]
items.sort(key=get_second_element)
items #  [(-9, 0), (4, 1), (1, 2)]

######
#1.
data = ((1,2), (3, 4))

#2.
i = 1
for item in data:
    print(f"Row {i} sum: {sum(item)}")
    i = i + 1

#3.
numbers = [4, 3, 2, 1]

#4.
copy_numbers = numbers[:]

#5.
numbers.sort()
######

# ------9.4------
#challenge

def enrollment_stats(list_of_list_with_universities):
    
#    enrolled_students = []
#    annual_tuition_fees = []

#    for item in list_of_list_with_universities:
#        for i in range(len(item)):
#            if i == 1:
#                enrolled_students.append(item[i])
#            elif i == 2:
#                annual_tuition_fees.append(item[i])       
#                    
#    return enrolled_students, annual_tuition_fees

    total_students = []
    total_tuition = []

    for university in list_of_list_with_universities:
        total_students.append(university[1])
        total_tuition.append(university[2])

    return total_students, total_tuition

def mean(values):
    """Return the mean value in the list `values`"""
    return sum(values) / len(values)

def median(values):
    """Return the median value of the list `values`"""
    values.sort()
    if len(values) % 2 == 1:
        center_index = int(len(values) / 2)
        return values[center_index]
    else:
        left_center_index = (len(values) - 1) // 2
        right_center_index = (len(values) + 1) // 2
        return mean([values[left_center_index], values[right_center_index]])


universities = [
    ['California Institutr of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusets Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
    ]

totals = enrollment_stats(universities)

print("\n")
print("*****" * 6)
print(f"Total students:   {sum(totals[0]):,}")
print(f"Total tuition:  $ {sum(totals[1]):,}")
print(f"\nStudent mean:     {mean(totals[0]):,.2f}")
print(f"Student median:   {median(totals[0]):,}")
print(f"\nTuition mean:   $ {mean(totals[1]):,.2f}")
print(f"Tuition median: $ {median(totals[1]):,}")
print("*****" * 6)
print("\n")

# ------9.5------
#challenge

import random

noun = [
    "fossil",
    "horse",
    "aardvark",
    "judge",
    "chef",
    "mango",
    "extrovert",
    "gorilla",
]
verb = [
    "kicks",
    "jingles",
    "bounces",
    "slurps",
    "meows",
    "explodes",
    "curdles",
]
adjective = [
    "furry",
    "balding",
    "incredulous",
    "fragrant",
    "exuberant",
    "glistening",
]
preposition = [
    "against",
    "after",
    "into",
    "beneath",
    "upon",
    "for",
    "in",
    "like",
    "over",
    "within",
]
adverb = [
    "curiously",
    "extravagantly",
    "tantalizingly",
    "furiously",
    "sensuously",
]

def choice_3_element(list_with_string):
    """Rettn 3 random element not repeat itself from list with string"""
    string1 = random.choice(list_with_string)
    string2 = random.choice(list_with_string)
    string3 = random.choice(list_with_string)

    while string1 == string2:
        string2 = random.choice(list_with_string)

    while string1 == string3 or string2 == string3:
        string3 = random.choice(list_with_string)
    
    return string1, string2, string3


def make_poem(list_noun, list_verb, list_adjective, list_preposition, list_adverb):
    """Create a randomly generated poem, returned as a multi-line string."""
    noun1, noun2, noun3 = choice_3_element(list_noun)
    verb1, verb2, verb3 = choice_3_element(list_verb)
    adj1, adj2, adj3 = choice_3_element(list_adjective)

    prep1 = random.choice(list_preposition)
    prep2 = random.choice(list_preposition)
    if prep1 == prep2:
        prep2 = random.choice(list_preposition)
    
    adverb1 = random.choice(list_adverb)
    przedimek = ""
    if adverb1[0] in  ["a", "e", "i", "o", "u", "y"]:
        article = "An"
    else:
        article = "A"

    if "aeiou".find(adj1[0]) != -1:  # First letter is a vowel
        article = "An"
    else:
        article = "A"

    print(f"{article} {adj1} {noun1}")
    print(f"{article} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}")
    print(f"{adverb1}, the {noun1} {verb2}")
    print(f"the {noun2} {verb3} {prep2} a {adj3} {noun3}\n")

#    poem = (
#        f"{article} {adj1} {noun1}\n\n"
#        f"{article} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}\n"
#        f"{adverb1}, the {noun1} {verb2}\n"
#        f"the {noun2} {verb3} {prep2} a {adj3} {noun3}"
#    )

#    return poem


make_poem(noun, verb, adjective, preposition, adverb)
#poem = make_poem(noun, verb, adjective, preposition, adverb)
#print(poem)

# ------9.6------

capitals = {
    "California": "Sacramento",
    "New York": "Albany",
    "Texas": "Austin",
    }

key_value_pairs = (
    ("California", "Sacramento"),
    ("New York", "Albany"),
    ("Texas", "Austin")
    )

capitals_2 = dict(key_value_pairs)

capitals["Texas"] #  'Austin'

capitals_list = ["Sacramento", "Albany", "Austin"]
capitals_list[0] #  'Sacramento'
capitals_list[2] #  'Austin'

capitals["Colorado"] = "Denver"
capitals #  {'California': 'Sacramento', 'New York': 'Albany',
         #   'Texas': 'Austin', 'Colorado': 'Denver'}
capitals["Texas"] = "Houston"
capitals #{'California': 'Sacramento', 'New York': 'Albany',
         # 'Texas': 'Houston', 'Colorado': 'Denver'}

del capitals["Texas"]
capitals # {'California': 'Sacramento', 'New York': 'Albany',
         # 'Colorado': 'Denver'}

#error
#capitals["Arizona"] #  KeyError: 'Arizona'

"Ariozna" in capitals #  False
"California" in capitals #  True

if "Ariozna" in capitals:
    print(f"The capital of Arizona is {capitals['Arizona']}.")

"Sacramento" in capitals # False

for key in capitals:
    print(key)

# California
# New York
# Colorado

for state in capitals:
    print(f"The capital of {state} is {capitals[state]}.")

# The capital of California is Sacramento.
# The capital of New York is Albany.
# The capital of Colorado is Denver.

capitals.items() # dict_items([('California', 'Sacramento'), ('New York', 'Albany'), ('Colorado', 'Denver')])
type(capitals.items()) #  <class 'dict_items'>

for state, capital in capitals.items():
     print(f"The capital of {state} is {capital}.")
#The capital of California is Sacramento.
#The capital of New York is Albany.
#The capital of Colorado is Denver.

capitals[50] = "Hnonlulu"
capitals #  {'California': 'Sacramento', 'New York': 'Albany', 'Colorado': 'Denver', 50: 'Hnonlulu'}

#error:
#capitals[[1, 2, 3]] = "Bad" #  TypeError: unhashable type: 'list'

states = {
    "California": {
        "capital": "Sacramento",
        "flower": "California Poppy"
        },
    "New York": {
        "capital": "Albany",
        "flower": "Rose"
        },
    "Texas": {
        "capital": "Austin",
        "flower": "Bluebonnet"
        }
    }

states["Texas"] #  {'capital': 'Austin', 'flower': 'Bluebonnet'}
states["Texas"]['flower'] #  'Bluebonnet'

######
#1.
captains = {}
#2.
captains["Enterprice"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"
#3.
if "Enterprice" not in captains:
    captains["Enterprice"] = "unknown"
if "Discovery" not in captains:
    captains["Discovery"] = "unknown"
#4.
for ship, captain in captains.items():
    print(f"The {ship} is captained by {captain}.")
#5.
del captains["Discovery"]
captains #  {'Enterprice': 'Picard', 'Voyager': 'Janeway', 'Defiant': 'Sisko'}

#6.
captains_2 = dict((
    ("Enterprice", "Picard"),
    ("Voyager", "Janeway"),
    ("Defiant", "Sisko")
    ))
######

# ------9.7------
#challenge
# see: chapt_9_capitals.py

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

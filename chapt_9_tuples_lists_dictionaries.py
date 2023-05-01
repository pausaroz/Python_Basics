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

# ------6.1------
len  # <built-in function len>
type(len)  # <class 'builtin_function_or_method'>

# don't do that:
len = "I'm not the len you're liiking for."
type(len)  # <class 'str'>

len  # "I'm not the len you're liiking for."
del len
len  # <built-in function len>

num_lettters = len("four")
num_lettters  # 4

return_value = print("What do I return?")  # What do I return?
return_value  #
type(return_value)  # <class 'NoneType'>
print(return_value)  # None

# ------6.2------

def multiply(x, y):  # Function signature
    # F. body
    product = x * y
    return product
    # any code appears below the return will never run
    print("You cant't see me!")

num = multiply(1, 3)
print(num)  # 3

def greet(name):
    print(f"Hello, {name}!")


greet("Dave")  # Hello, Dave!
return_value = greet("Dave")  # Hello, Dave!
print(return_value)  # None

help(len)
# Help on built-in function len in module builtins:
#
# len(obj, /)
#     Return the number of items in a container.


help(multiply)
# Help on function multiply in module __main__:
# 
# multiply(x, y)


# docstring

def multiply(x, y): 
    """Return the product of two numbers x and y."""
    product = x * y
    return product
    
######

def cube(number):
    """Return the cube of the input number."""
    cube_num = num**3  # pow(num, 3)
    return cube_num

print(cube(3))

######

# ------6.3------

# see file: f_and_l_temperature.py

# ------6.4------

n = 1
while n < 5:
    print(n)
    n = n + 1

# while n < 6:
#    print(n)
## press it to force python to quit: CTRL + C

num = float(input("Enter a positive number: "))

while num <= 0:
    print("That's not a positive number!")
    num = float(input("Enter a positive number: "))

for letter in "Python":
    print(letter)

word = "Python"
index = 0
while index < len(word):
    print(word[index])
    index = index + 1

for l in range(3):
    print("Python")

for l in range(10, 20):
    print(l * l)

amount = float(input("Enter an amount: "))

for num_people in range(2, 6):
    print(f"{num_people} people: ${amount / num_people:,.2f} each")

for l in range(1, 4):
    for j in range(4, 7):
        print(f"l = {l} and j = {j}")

######

# 1.
for number_int in range(2, 11):
    print(number_int)

# 2.
number_int = 2
while number_int <= 10:
    print(number_int)
    number_int = number_int + 1

# 3.

def doubles(number):
    """Return the result of multiplying an input number by 2."""
    return number * 2

num_to_duble = int(input("Enter a number: "))

for i in range(3):
    num_to_duble = doubles(num_to_duble)
    print(num_to_duble)

######

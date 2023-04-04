print("Integers and floating-point numbers")
# three built-in numeric data types:
# integers np: 2
# float-point numbers np: 1.0, -2,27
# complex numbers

type(1)  # <class'int'>
# integer literal:
num = 25
# It is not an integer literal
# because the integer value is created from a string:
int("25")  # 25

# large numbers:
1000000    # 1000000
1_000_000  # 1000000
# not like that:
# 1,000,000

# float-point numbers:
type(1.0)    # <class'float'>
float("1.24")  # 1.24

# floating-point literals
1000000.0    # 1000000.0
1_000_000.0  # 1000000.0
1e6          # 1000000.0

# E notation (exponential notation - notacja wykładnicza)
# 1e6 is equivalent to 1x 10^6 10 do potęgi 6

200000000000000000.0  # 2e+17
1e-4                  # 0.0001

# The maximum floating-point number depends on your system,
# but something like 2e400 ought to be well beyond most machines' capabilities.
# Maksymalna liczba zmiennoprzecinkowa zależy od twojego systemu,
# ale coś takiego jak 2e400 powinno znacznie wykraczać poza możliwości większości maszyn
2e400  # inf
# inf - infinity (nieskończoność)

n = 2e400
n  # inf
type(n) # <class 'float'>
n = -2e400
n  # -inf
type(n) # <class 'float'>


#############################
print("1.")
num1 = 25000000
num2 = 2_5000_000
print(f"""{num1},
{num2}""")
print("2.")
num = 175e+3

print("Arithmetic operations and expressions")

# Addition
1 + 2  # 2
1.2 + 2  # 3.0

# Subtraction
1 - 1  # 0
5.0 - 3  # 2.0

# look confusing: 
1 - -3  # 4
1 --3  # 4
1- -3  # 4
1--3  # 4

# it is easier to understand:
1 - (-3)  # 4

# Multiplication
3 * 3  # 9
2 * 8.0  # 16.0

# Division - return float
9 / 3  # 3.0
5.0 / 2  # 2.5

# can't
# 1 / 0

# Integer division
9 // 3  # 3
5.0 // 2  # 2.0
-3 // 2  # -2

# The // operator first divides the number on the left by
# the number on the right and then rounds down to an integer.
# for example
-3 // 2
# return: -2
# First, -3 is divided by 2 to get -1.5.
# Then -1.5 is rounded down to -2.
3 // 2
# returns: 1
# because both numbers are positive.

# Exponents - Wykładniki
# You can raise a number to a power using the ** operator:
2 ** 2  # 4
2 ** 3  # 8
2 ** 4  # 16

3 ** 1.5  # 5.196152422706632
9 ** 0.5  # 3.0

2 ** -1  # 0.5
# 2 ** -1 == 1 / (2 ** 1) == 1 / 2 == 0.5
2 ** -2  # 0.25
# 2 ** -2 == 1 / (2 ** 2 ) == 1 / 4 == 0.25


# The modulus oparator
# returns the remainder of diving
# zwraca reszte z dzielenia
5 % 3  # 2
20 % 7  # 6
16 % 8  # 0

# can't
# 1 % 0

5 % -3  # -1
-5 % 3  # 1
-5 % -3  # -2
# These results are shocking at first glance
# but look at equation:

# r = equation (równanie, wzór)
# x = number
# y = number

# r = x - (y * (x // y))
# to find
5 % -3
# pyton do
# 5 - (-3 ( 5 // -3))
# 5 - (-3 * (-2))
# 5 - (6)
# 5 - 6
# -1

# Arithmetic expressions
2*3 -1  # 5
4/2 + 2**3  # 10.0
-1 + (-3*2 + 4)  # -3

# order of operations
# 1. *, /, //, %
# 2. +, -
# PEP 8 says the following about whitespace in complex expressions:
# If operators with different priorities are used,
# consider adding whitespace around the operators with the lowest priority(ies).
# Use your own judgment; however, never use more than one space, and always have the same amount of whitespace on both sides of a binary operator.
2*3 - 1

# Another good practice is to use parentheses
(2 * 3) -1

print("Make python to lie to you")
0.1 + 0.2  # 0.30000000000000004
# it's not a bug!. It's a floating-point reppresentation error

print("Math functions and number methods")
# 3 mathematical functions most common

# round() for rounding numbers to some number of decimal places
# abs() for getting the absolute value of a number
# pow() for raising a number to some power

# the round() function
round(2.3)  # 2
round(2.7)  # 3
# some unexpected behavior when the number ends in .5
round(2.56)  # 3
round(2.5)  # 2
round(3.5)  # 4

# Python 3 rounds numbers according to a strategy called
# rounding ties to even.

# A tie is any number whose last digit is five.
# tie: 2.5, .1415
# not tie: 1.37
# When you round ties to even,
# you first look at the digit one decimal place to
# the left of the last digit in the tie.
# If that digit is odd, then you round up.
# That's why 2.5 rounds down to 2 and 3.5 rounds up to 4

#two argument to round()
round(3.14159, 3)  # 3.142
round(2.71828, 2)  # 2.72

round(2.675, 2)  # 2,67
# expected value: 2.68
# to understand, read: https://en.wikipedia.org/wiki/IEEE_754#Roundings_to_nearest

# the abc() function
abs(3)  # 3
abs(-5.0)  # 5
abs(-111 + 100)  # 11
# abs () always returns a positive number

# the pow() function
pow(2, 3)  # 8
# 2 * 2 * 2 == 2 ** 3 == 8
pow(2, -2)  # 0.25

pow(2, 3, 4)  # 0
(2 ** 3) % 4 == 0

# check if a float is integral
num = 2.5
num.is_integer()  # False
num = 2.0
num.is_integer()  # True

########
num_1 = float(input("Enter a number: "))
print(f"""{num_1} rounded to 2 decimal places is {round(num_1, 2)}
The absolute value of {num_1} is {abs(num_1)}""")
num_2 = float(input("Enter another number: "))
num_3 = num_1 - num_2
print(f"The diffrence between {num_1} and {num_2} is an integer? {num_3.is_integer()}")

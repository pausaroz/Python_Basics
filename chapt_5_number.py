# ------5.1------

type(1)  # <class 'int'>
num = 25
int("25")  # 25

1000000  # 1000000
1_000_000  # 1000000

type(1.0)  # <class 'float'>
float("1.25")  # 1.25

1000000.0  # 1000000.0
1_000_000.0  # 1000000.0

1e6  # 1000000.0
200000000000000000.0  # 2e+17

1e-4  # 0.0001
2e400  # inf
n = 2e400
n  # inf
type(n)  # <class 'float'>
-2e400  # -inf

###########
num1 = 25000000
num2 = 2_5000_000
print(f"""{num1},
{num2}""")
num = 175e+3
2e+309
###########

# ------5.2------

1 + 2  # 3
1.0 + 2  # 3.0
1 - 1  # 0
5.0 - 3  # 2
-3  # -3
1 --3  # 4
1- -3  # 4
1- -3  # 4
1 - (-3)  # 4

3 * 3  # 9
2 * 8.0  # 16.0

9 / 3  # 3.0
5.0 / 2  # 2.5

int(9 / 3)  # 3
int(5.0 / 2)  # 2

9 // 3  # 3
5.0 // 2  # 2.0
-3 // 2  # -2 :because -3 / 2 = -1,5, then -1.5 is rounded down to -2

# error:
# 1 / 0

2 ** 2  # 4
2 ** 3  # 8
2 ** 4  # 16
3 ** 1.5  # 5.196152422706632
9 ** 0.5  # 3.0

2 ** -1  # 0.5
2 ** -2  # 0.25

20 % 7  # 6
16 % 8  # 0

# error
# 1 % 0

5 % -3  # -1
-5 % 3  # 1
-5 % -3  # -2
# x - ( y * (x // y))
#5 % -3 = 5 - (-3 ( 5 // -3)) = 5 - ( -3 * -2) = 5 - 6 = -1
#-5 % 3 = -5 - (3 (-5 // 3 )) = -5 - (3 *  -2 = -5 - -6 = 1
#-5 % -3 = -5 - (-3 (-5 // -3)) = -5 - (-3 * 1 ) = -5 - -3 = -2

2*3 - 1  # 5
4/2 + 2**3  # 10.0
-1 + (-3*2 + 4)  # -3

# ------5.3------
# go to file: number_exponent.py

# ------5.4------

0.1 + 0.2  # 0.30000000000000004

# ------5.5------
round(2.3)  # 2
round(2.5)  # 2
round(3.5)  # 4

# to understand, read: https://en.wikipedia.org/wiki/IEEE_754#Roundings_to_nearest

round(3.14159, 3)  # 3.142
round(2.71828, 2)  # 2.72

# error:
# round(2.65, 1.4)

round(2.675, 2)  # 2.67 :expected value: 2.68

abs(3)  # 3
abs(-5.0)  # 5.0

pow(2, 3)  # 8
pow(2, -2)  # 0.25
pow(2, 3, 4)  # 0
# pow(2, 3, 4) == 2**3 % 4 == 8 % 4 ==  0

num = 2.5
num.is_integer()  # False
num = 2.0
num.is_integer()  # True

#######
num_1 = float(input("Enter a number: "))
print(f"""{num_1} rounded to 2 decimal places is {round(num_1, 2)}
The absolute value of {num_1} is {abs(num_1)}""")
num_2 = float(input("Enter another number: "))
num_3 = num_1 - num_2
print(f"The diffrence between {num_1} and {num_2} is an integer? {num_3.is_integer()}")
#######

# ------5.6------
n = 9.125
f"The value of n is {n}"  # 'The value of n is 9.125'
f"The value of n is {n:.2f}"  # 'The value of n is 9.12'

n = 9.126
f"The value of n is {n:.2f}"  # 'The value of n is 9.13'
f"The value of n is {n:.1f}" # 'The value of n is 9.1'

n = 1
f"The value of n is {n:.2f}"  # 'The value of n is 1.00'
f"The value of n is {n:.3f}"  # 'The value of n is 1.000'

n = 1234567890
f"The value of n is {n:,}"  # 'The value of n is 1,234,567,890'

n = 1234.56
f"The value of n is {n:,.2f}"  # 'The value of n is 1,234.56'

balance = 2000.0
spent = 256.35
remaining = balance - spent
remaining  # 1743.65
f"After spending ${spent:.2f}, I was left with $ {remaining:,.2f}"
# 'After spending $256.35, I was left with $ 1,743.65'

ratio = 0.9
f"Over {ratio:.1%} of Pythonistas say 'Real Python rocks!'"
# "Over 90.0% of Pythonistas say 'Real Python rocks!'"
f"Over {ratio:.2%} of Pythonistas say 'Real Python rocks!'"
# "Over 90.00% of Pythonistas say 'Real Python rocks!'"
# for more information:
# https://docs.python.org/3/library/string.html#format-string-syntax_

######
f"{3**.123:.3f}"
f"{150000:,.2f}"
f"{2/10:.0%}"  # '20%'
######

# ------5.6------
n = 1 + 2j
n  # (1+2j)
n.real  # 1.0
n.imag  # 2.0
n.conjugate()  # (1-2j)

a = 1 + 2j
b = 3 - 4j
a + b  # (4-2j)
a - b  # (-2+6j)
a * b  # (11+2j)
a ** b  # (932.1391946432212+95.9465336603415j)
a / b  # (-0.2+0.4j)

# error:
# a // b # TypeError

x = 42
x.real  # 42
x.imag  # 0
x.conjugate()  # 42
y = 3.14
y.real  # 3.14
y.imag  # 0.0
y.conjugate()  # 3.14


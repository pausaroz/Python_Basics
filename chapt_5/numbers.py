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






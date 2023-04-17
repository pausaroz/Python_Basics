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


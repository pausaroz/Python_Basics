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

num = multiply(1, 3)
print(num)  # 3

type("Hello") # Can use this in interactive window (IDLE)
string3 = "We're #1!"
string4 = 'I said. "Put it over by the llama."'
# text = "She said, "What time is it?"" # SyntaxError: invalid syntax
# zakomentuj linie kodu = alt + 3
# odkomentuj linie kodu = alt + 4

text = "She said, \"What time is it?\""
print(text)  # She said, "What time is it?"

len(text) # Determine the Length of a String.
# Multiline Strings
# The PEP 8 style guide recommends that each line of Python code
# contain no more than seventy-nine characters—including spaces.

paragraph_using_blackslash_method = "This planet has—or rather had—a problem, which was \
this: most of the people living on it were unhappy for pretty much \
of the time. Many solutions were suggested for this problem, but \
most of these were largely concerned with the movements of small \
green pieces of paper, which is odd because on the whole it wasn't \
the small green pieces of paper that were unhappy."

paragraph_using_triple_quoted = """This planet has—or rather had—a problem, which was
this: most of the people living on it were unhappy for pretty much
of the time. Many solutions were suggested for this problem, but
most of these were largely concerned with the movements of small
green pieces of paper, which is odd because on the whole it wasn't
the small green pieces of paper that were unhappy."""
print(" ")

print("Using triple quoted")
print("""An example of a ...
string that spans across multiple lines ...
and also preserves whitespace.""")
print(" ")

print("Using blackslash method")
print("Przykład ... \
string z  ... \
backslash.")
print(" ")

print("Concatenation, indexing and slicing")
print("Concatenation")
string1 = "abra"
string2 = "cadabra"
magic_string = string1 + string2
print(magic_string) # abracadabra
print("indexing")
flavor = "fig pie"
flavor[1] # 'i'
# 'f''i''g'' ''p''i''e'
#  0  1  2  3  4  5  6
#
#"negative indices"
# 'f''i''g'' ''p''i''e'
# -7 -6 -5 -4 -3 -2 -1
flavor[-7] # 'f'
user_input = "Jak dłuci ciąg wpiszesz drogi userze"

final_index = len(user_input) - 1
last_character = user_input[final_index]

# Getting the final character with the index -1 takes
# less typing and doesn’t require an intermediate
# step to calculate the final index:
last_character = user_input[-1]
print(" ")

print("slicing")
# need a string containing just the first three letters of
# the string "fig pie".
first_three_letters = flavor[0] + flavor[1] + flavor[2]
first_three_letters # 'fig'

# better way:

print(" ")
# flavor = "fig pie"
flavor[0:3] # 'fig'

# | f | i | g |   | p | i | e |
# 0   1   2   3   4   5   6   7
print(flavor[0:3])  # 'fig'
print(flavor[:3])   # 'fig'
print(flavor[3:7])  # ' pie'
print(flavor[3:])   # ' pie'
print(flavor[:])    # 'fig pie'

# It’s important to note that,
# unlike with string indexing,
# Python won’t raise an IndexError when you try to slice between boundaries
# that fall outside the beginning or ending boundaries of a string: 
print(flavor[:14])  # 'fig pie'
print(flavor[13:15])# ''
#Note
empty_string1 = ""
non_empty_string1 = " "
non_empty_string2 = "  "
non_empty_string3 = "        "

# the boundaries labeled with negative numbers
# | f | i | g |   | p | i | e |
# -7  -6  -5  -4  -3  -2  -1
print("n")
print(flavor[-7:-4]) # 'fig'
print(flavor[-7:0])  # ''
print(flavor[-7:])   # 'fig pie'

# Strings are immutable - Ciągi są niezmienne
word = "goal"
# This:
# >>> word[0] = "f"
# Python throws a TypeError and tells you that str objects
# don’t support item assignment. 

# If you want to alter a string, then you must create an entirely new string.
# Jeśli chcesz zmienić ciąg, to musisz stworzyć zupełnie nowy ciąg.
# word = "goal"
word = "f" + word[1:]
word  # 'foal' 

print("String Methods")

# Converting string case
"Jean-Luc Picard".lower() # 'jean-luc picard'
name = "Jean-Luc Picard"
name.upper()  # 'JEAN-LUC PICARD'

# len() is a stand-alone function.
len(name) # 15

# Removing Whitespace From a String
# There are three string methods that you can use to remove whitespace
# from a string:

# 1. .rstrip() # removes whitespace from the right side of a string:
name = "Jean-Luc Picard "
name           # 'Jean-Luc Picard '
name.rstrip()  # 'Jean-Luc Picard'
# 2. .lstrip() # removes whitespace from the left-hand side of the string:
name = " Jean-Luc Picard"
name           # ' Jean-Luc Picard'
name.lstrip()  #  'Jean-Luc Picard'
# 3. .strip()  # remove whitespace from both the left and the right sides of the string
name = " Jean-Luc Picard "
name           #' Jean-Luc Picard '
name.strip()   #'Jean-Luc Picard'

# Determine If a String Starts or Ends With a Particular String
# Określenie, czy ciąg znaków zaczyna się lub kończy określonym ciągiem znaków
# .startswith() and .endswith().
starship = "Enterprise"
starship.startswith("en")  # False
starship.startswith("En")  # True

starship.endswith("rise")  # True
# Just like .startswith(), the .endswith() method is case sensitive:
starship.endswith("risE")  # False

print("String Methods and Immutability - Metody łańcuchowe i niezmienność")

name = "Picard"
name.upper() # 'PICARD'
name         # 'Picard' 

name = "Picard"
name = name.upper()
name         # 'PICARD' 

print("""Use IDLE to Discover Additional String MethodsRecall
               """)
# IDLE can help you find new string methods. To see how,
# first assign a string literal to a variable in the interactive window:
# >>> starship = "Enterprise"
# Next, type starship followed by a period, but do not hit Enter.
# You should see the following in the interactive window:
# >>> starship.
# Now wait for a couple of seconds. IDLE displays a list of every string method,
# which you can scroll through using the arrow keys.
# A related shortcut in IDLE is the ability to use Tab to automatically
# fill in text without having to type long names. For instance,
# if you type only starship.u and hit Tab, then IDLE automatically
# fills in starship.upper because only one method that begins with
# a u belongs to starship.

print("Interact With User Input")
prompt = "Hey, what's up? "
user_input = input(prompt)
print("You said: " + user_input.upper())

user_input = input("Please enter some text: ")
print("You entered: ", user_input)

lowercase_input = user_input.lower()
print("Your text in lowercase: ", lowercase_input)

num_chars = len(user_input)
print("Number of characters in your text: ", num_chars)

user_input = input("Tell me your password: ")
print("The first letter ypu entered was: " + user_input[0].upper())

print("Working With Strings and Numbers ")
# Using Strings With Arithmetic Operators
num = '2'
num + num  # '22'

# You can multiply strings by a number
num = '12'
num * 3  # '121212'
3 * num  # '121212'

# You can NOT multiply strings by a string
# '12' * '3'  # TypeError: can't multiply sequence by non-int of type 'str'

# You can NOT add a string and a number?
# "3" + 3  # TypeError: can only concatenate str (not "int") to str

# Converting Strings to Numbers
num = input("Enter a number to be doubled: ")
doubled_num = num * 2
print(doubled_num)  # '22'

# you must convert them from a string type to a number type.
# There are two functions that you can use to do this:
# int() # stands for integer and converts objects into whole numbers
# float() #stands for floating-point number and converts objects
# into numbers with decimal points
int("12")    # 12
float("12")  # 12.0

# you can’t change a string that looks like a floating-point number
# into an integer
# because you would lose everything after the decimal point ( because it would result in a loss of precision.)
# int("12.0")  # ValueError: invalid literal for int() with base 10: '12.0' 

num = input("Enter a number to be doubled: ")
doubled_num = float(num) * 2
print(doubled_num)

# Converting Numbers to Strings
num_pancakes = 10
# "I am going to eat " + num_pancakes + " pancakes."  # TypeError: can only concatenate str (not "int") to str 
"I am going to eat " + str(num_pancakes) + " pancakes."

total_pancakes = 10
pancakes_eaten = 5
"Only " + str(total_pancakes - pancakes_eaten) + " pancakes left." #  'Only 5 pancakes left.' 


num_1 = input("Enter first number: ")
num_2 = input("Enter secind number: ")
result = "The product of " + num_1 + " and " + num_2 + " is " + str(float(num_1)*float(num_2))
print(result)

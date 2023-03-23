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

# ------4.1------
print(type("Hello, world"))
pharse = "Hello, world"
print(type(pharse))

string1 = 'Hello, world'
string2 = "1234"
string3 = "We're #1!"
string4 = 'I said, "Put it over by the llama."'

# error
# text = "She said, "What time is it?""

text = "She said, \"What time is it?\""
print(text)
print(len("abc"))
letters = "abc"
print(len(letters))

paragraph = "Lorem ipsum dolor sit amet, \
consectetur adipiscing elit. \
Nam ornare nulla ut erat dapibus, eu luctus nisl tincidunt."
print(paragraph)

paragraph = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit.
Nam ornare nulla ut erat dapibus, eu luctus nisl tincidunt."""

print(paragraph)

# ------4.2------

string1 = "abra"
string2 = "cadabra"
magic_string = string1 + string2
print(magic_string)

first_name = "Arthur"
last_name = "Dent"
full_name = first_name + " " + last_name
print(full_name)

flavor = "fig pie"

# | f | i | g |   | p | i | e |
# -----------------------------
# | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
# -----------------------------
# |-7 |-6 |-5 |-4 |-3 |-2 |-1 |

flavor[1]
flavor[0]
print(flavor)
print(flavor[1])
print(flavor[0])
print(flavor[-1])
first_tree_leeters = flavor[0] + flavor[1] + flavor[2]
print(first_tree_leeters)
print(flavor[0:3])
print(flavor[:3])

# | f | i | g |   | p | i | e |
# -----------------------------
# 0   1   2   3   4   5   6   7
# -----------------------------
#-7  -6  -5  -4  -3  -2   -1 
print(flavor[3:])
print(flavor[:])
print(flavor[-7:-4])
print(flavor[-7:0])
print(flavor[-7:])

word = "goal"
# error:
# word[0] = "f"
word = "f" + word[1:]

# ------4.3------

"Arthur Dent".lower()
full_name.lower()
full_name.upper()
len(full_name)

"  name".lstrip()
"name  ".rstrip()
"  name  ".strip()

starship = "Enterprice"
starship.startswith("en")  # False
starship.startswith("En")  # True
starship.endswith("rice")  # True
starship.endswith("ricE")  # False

# ------4.4------

prompt = "Hey, what's up? "
user_input = input(prompt)
print("You said: " + user_input)

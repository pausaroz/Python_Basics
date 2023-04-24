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

###########
user_input = input("Please enter some text: ")
print("You entered: ", user_input)

lowercase_input = user_input.lower()
print("Your text in lowercase: ", lowercase_input)

num_chars = len(user_input)
print("Number of characters in your text: ", num_chars)

###########

# ------4.5------

###########
user_input = input("Tell me your password: ")
print("The first letter ypu entered was: " + user_input[0].upper())
###########

# ------4.6------

num = "2"
num + num # '22'
num = '12'
num * 3  # '121212'
3 * num  # '121212'

# error
# "12" * "3"
# "3" + 3
num = input("Enter a number to be doubled: ")
doubled_num = num * 2
print(doubled_num)

int("12")   # 12
float("12")  # 12.0

# error:
# int("12.0")

num = input("Enter a number to be doubled: ")
doubled_num = float(num) * 2
print(doubled_num)

num_pancakes = 10
# error:
# "I am going to eat " + num_pancakes + " pancakes."
"I am going to eat " + str(num_pancakes) + " pancakes."  # 'I am going to eat 10 pancakes.'
total_pancakes = 10
pancakes_eaten = 5
"Only " + str(total_pancakes - pancakes_eaten) + " pancakes left."  # 'Only 5 pancakes left.'

# ------4.7------

name = "Zaphod"
heads = 2
arms = 3

name + " has " + str(heads) + " heads and " + str(arms) + " arms"  # 'Zaphod has 2 heads and 3 arms'
a = f"{name} has {heads} heads and {arms} arms"  # 'Zaphod has 2 heads and 3 arms'

n = 3
m = 4
f"{n} times {m} is {n*m}"  # '3 times 4 is 12'

# in python version earlier than 3.6 f" {}" dont work
# this work:
"{} has {} heads and {} arms".format(name, heads, arms)  # 'Zaphod has 2 heads and 3 arms'
pharse = "the surprise is in here somewhere"
pharse.find("somewhere")  # 4
pharse.find("soberokde")  # -1
"the surprise is in here somewhere".find("SURPRISE")  # -1
"I put a string in your string".find("string")  # 8

# error:
# "My number is 555-555-555".find(5)

"My number is 555-555-555".find("5")
my_story = "I'm telling you the truth; nothing but the truth!"
my_story.replace("the truth", "lies")  # "I'm telling you lies; nothing but lies!"
my_story  # "I'm telling you the truth; nothing but the truth!"
my_story = my_story.replace("the truth", "lies")  # "I'm telling you lies; nothing but lies!"
my_story  # "I'm telling you lies; nothing but lies!"


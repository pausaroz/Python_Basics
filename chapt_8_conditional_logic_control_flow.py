# ------8.1------
type(True) #  <class 'bool'>
type(False) #  <class 'bool'>

1 == 1 #  True
3 > 5  # False

False
"a" == "a" #  True
"a" == "b" #  False
"a" < "b" #  True
"a" > "b" #  False

######
# 1.
1 <= 1 #  True
1 != 1 #  False
1 != 2 #  True
"good" != "bad" #  True
"good" != "Good" #  True
123 == "123" # False

# 2.
3 != 4 #  True
10 >= 5 #  True
"jack" <= "jill" #  True
42 != "42" #  True

######

# ------8.2------

1 < 2 and 3 < 4 #  True
2 < 1 and 4 < 3 #  False
1 < 2 and 4 < 3 #  False
2 < 1 and 3 < 4 #  False

True and True #  True
True and False #  False
False and True #  False
False and False #  False

1 < 2 or 3 < 4 #  True
2 < 1 or 4 < 3 #  False
1 < 2 or 4 < 3 #  True
2 < 1 or 3 < 4 #  True

True or True #  True
True or False #  True
False or True #  True
False or False #  False

not True # False
not False # True

not True == False #  True
#False == not True #  SyntaxError: invalid syntax

#operator order of precedence (highest to lowest)
#1. <, <=, ==, >=, >
#2. not
#3. and
#4. or
False == (not True) #  True

True and not (1 != 1) #  True
#True and not (False)
#True and True

("A" != "A") or not (2 >= 3) #  True
#(False) or not (False)
#False or True

True and False == True and False #  False
(True and False) == (True and False) # True

######

#1.
True
(1 <= 1) and (1 != 1) #  False
not (1 != 2) #  False
("good" != "bad") or False #  True
("good" != "Good") and not (1 == 1) #  False

#2.
False == (not True)  # True
True and False == (True and False) # True
not (True and "A" == "B") # True
######

# ------8.3------

if 2 + 2 == 4:
    print("2 and 2 is 4") #  2 and 2 is 4

if 2 + 2 == 5:
    print("Is this the mirror universe?") #


grade = 95

if grade >= 70:
    print("You passed the class!")

print("Thank you for attenting.")
# You passed the class!
# Thank you for attenting.

grade = 40

if grade >= 70:
    print("You passes the class!")

if grade < 70:
    print("You did not pass the class :(")

print("Thank you fot attending")

grade = 40

if grade >= 70:
    print("You passed the class!")
else:
    print("You did not pass the class :(")

print("Thank you fot attending")

grade = 85  # 1

if grade >= 90:  # 2
    print("You passed the class with an A.")
elif grade >= 80:  # 3
    print("You passed the class with a B.")
elif grade >= 70:  # 4
    print("You passed the class with a C.")
else:  # 5
    print("You did not pass the class :(")

print("Thank you fot attending")  # 6

#-------
#-------
sport = input("Enter a sport: ")
p1_score = int(input("Enter player 1 score: "))
p2_score = int(input("Enter player 2 score: "))
#-------

#I
# 1
if sport.lower() == "basketball":
    if p1_score == p2_score:
        print("The game is a draw.")
    elif p1_score > p2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
# 2
elif sport.lower() == "golf":
    if p1_score == p2_score:
        print("The game is a draw.")
    elif p1_score < p2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
# 3
else:
    print("Unknown sport.")

#II
if p1_score == p2_score:
    print("The game is a draw.")
elif sport.lower() == "basketball":
    if p1_score > p2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
elif sport.lower() == "golf":
    if p1_score < p2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
else:
    print("Unknown sport.")

#III
#sport = sport.lower()
#p1_wins_bball = (sport == "basketball") and (p1_score > p2_score)
#p1_wins_golf = (sport == "golf") and (p1_score < p2_score)
#p1_wins = player1_wins_basketball or player1_wins_golf

sport = sport.lower()
if p1_score == p2_score:
    print("The game is a draw.")
elif (sport == "basketball") or (sport == "golf"):
    p1_wins_bball = (sport == "basketball") and (p1_score > p2_score)
    p1_wins_golf = (sport == "golf") and (p1_score < p2_score)
    p1_wins = p1_wins_bball or p1_wins_golf
    if p1_wins:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
else:
    print("Unknown sport.")
#-------
#-------
######
print("1.")
user_word = input("Enter a word: ")
if len(user_word) < 5:
    print("Your input is less than 5 characters long.")
elif len(user_word) > 5:
    print("Your input is greather than 5 characters long.")
else:
    print("Your input is 5 characters long.")

print("2.")
my_guess = input("I'm thinking of a number beetween 1 and 10 Guess witch one. ")
i = True
while i:
    my_guess = input("Guess a num: ")
    if my_guess == "3":
        print("You win!")
        i = False
    else:
        print("You lose.")
    
######

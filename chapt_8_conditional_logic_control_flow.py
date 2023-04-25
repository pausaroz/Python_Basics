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

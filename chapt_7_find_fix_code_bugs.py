## ------7.1------
#
#for i in range(1,4):
#    j = i * 2
#    print(f"i is {i} and j is {j}")
#
## click in menu IDLE : Debug > Debugger
#
## click STEP, OVER, OUT
#
## in editor window right-click > Set Breakpoints / Clear Breakpoints
## then click GO in DEBUGGER CONTROL

# ------7.2------
###def add_underscores(word):
###    new_word = "_"
###    for i in range(len(word)):
###        new_word = word[i] + "_"
###    return new_word
##
##def add_underscores(word):
##    new_word = "_"
##    for i in range(len(word)):
##        new_word = new_word + word[i] + "_"
##    return new_word
##
#def add_underscores(word):
#    new_word = "_"
#    for i in range(len(word)):
#        new_word = word[i] + "_"
#        print(f"i = {i}; new_word = {new_word}")
#    return new_word
#
#refactoring:
#
def add_underscores(word):
    new_word = "_"
    for letter in word:
        new_word = new_word + letter + "_"
    return new_word

pharse = "hello"
print(add_underscores(pharse))

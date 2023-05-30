#main.py
##
##import helpers.string, helpers.math
##
##num_a = 5
##num_b = 8
##
##print(helpers.string.shout(f"the area of a {num_a}-by-{num_b} reactangle is \
##{helpers.math.area(num_a, num_b)}"))


from helpers.string import shout
from helpers.math import area


length = 5
width = 8
message = f"The area of a {length}-by-{width} rectangle is {area(length, width)}"
print(shout(message))

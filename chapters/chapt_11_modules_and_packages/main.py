# ------11.1------

###main.py
##import adder
###import <module> as <other_name>
###from <module> import <name>
##
##value = adder.add(2, 2)
##print(value)
##
##double_value = adder.double(value)
##print(double_value)

##import adder as a
##
##value = a.add(2, 2)
##print(value)
##
##double_value = a.double(value)
##print(double_value)

from adder import add, double

value = add(2, 2)
print(value)

double_value = double(value)
print(double_value)

##import datetime
##datetime.datetime(2020, 2, 2)

##import datetime as dt
##dt.datetime(2020, 2, 2)

from datetime import datetime
datetime(2020, 2, 2)

######
#2
import greeter
greeter.greet("Real Python")
######

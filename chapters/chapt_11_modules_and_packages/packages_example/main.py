#main.py
# ------11.2------
##import mypackage.module1
##import mypackage.module2
### import <package_name>.<module_name>
##
##mypackage.module1.greet("Pythonista")
##mypackage.module2.depart("Pythonista")
##

#import <package>
#import <package> as <other_name>
#from <package> import <module>
#from <package> import <module> as <other_name>

##from mypackage import module1, module2
##
##module1.greet("Pythonista")
##module2.depart("Pythonista")

##from mypackage import module1 as m1, module2 as m2
##
##module1.greet("Pythonista")
##module2.depart("Pythonista")

##from mypackage.module1 import greet
##from mypackage.module2 import depart
##
##greet("Pythonista")
##depart("Pythonista")

from mypackage.module1 import greet
from mypackage.mysubpackage.module3 import people

for person in people:
    greet(person)

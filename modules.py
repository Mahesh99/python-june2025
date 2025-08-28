# import mymodule

# mymodule.hello()
# mymodule.add(5, 20)
# print(mymodule.first_5_primes)



# import mymodule as mm

# mm.hello()
# mm.add(5, 20)


# from mymodule import hello, greet, first_5_primes

# hello()
# greet("Alice")
# print(first_5_primes)
# add(1,2) # will give error


# from mymodule import *
# hello()
# add(2,3)
# print(first_5_primes)


# from mymodule import add as a, greet, primetest as pt, first_5_primes as f5p
# a(2,3)
# print(f5p)

# __name__="__main__"
import mymodule
import random

print(__name__)
print(mymodule.__name__)

# modules
# 1.built-in modules
# -- random, math, time, sys
# 2.user-defined modules

import math
print(math.cos(math.degrees(60)))
# print(math.radians(57.2958))
print(math.degrees(1))

import sys
# print(sys.version)
# print(sys.platform)
print("path",sys.path)
